#!/usr/bin/env python3
"""
SUSHI Build & Validate - Local Testing Script

This script replicates the GitHub Actions workflow for building and validating
FHIR Shorthand (FSH) files using SUSHI locally.

Usage:
    python3 sushi_build_validate.py [--verbose] [--no-cache]
    
Options:
    --verbose       Enable verbose debugging output
    --no-cache      Don't use cached FHIR packages
"""

import subprocess
import sys
import os
import json
import re
from pathlib import Path
from typing import Tuple, List, Dict, Optional
import argparse
from datetime import datetime


class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class SushiBuildValidator:
    """Main class for SUSHI build and validation"""
    
    def __init__(self, verbose: bool = False, use_cache: bool = True):
        self.verbose = verbose
        self.use_cache = use_cache
        self.workspace_root = Path(__file__).parent.parent
        self.ig_path = self.workspace_root / "no-basis"
        self.fsh_generated = self.ig_path / "fsh-generated"
        self.resources_path = self.fsh_generated / "resources"
        self.sushi_log = self.ig_path / "sushi-output.log"
        
        self.error_count = 0
        self.warning_count = 0
        self.total_resources = 0
        self.profile_count = 0
        self.valueset_count = 0
        self.codesystem_count = 0
        self.instance_count = 0
        
    def print_header(self, text: str, char: str = "="):
        """Print a formatted header"""
        print(f"\n{Colors.BOLD}{Colors.OKCYAN}{text}{Colors.ENDC}")
        print(char * len(text))
        
    def print_success(self, text: str):
        """Print success message"""
        print(f"{Colors.OKGREEN}✅ {text}{Colors.ENDC}")
        
    def print_error(self, text: str):
        """Print error message"""
        print(f"{Colors.FAIL}❌ {text}{Colors.ENDC}")
        
    def print_warning(self, text: str):
        """Print warning message"""
        print(f"{Colors.WARNING}⚠️  {text}{Colors.ENDC}")
        
    def print_info(self, text: str):
        """Print info message"""
        print(f"{Colors.OKBLUE}ℹ️  {text}{Colors.ENDC}")
        
    def print_debug(self, text: str):
        """Print debug message if verbose is enabled"""
        if self.verbose:
            print(f"{Colors.OKCYAN}DEBUG: {text}{Colors.ENDC}")
            
    def run_command(self, cmd: List[str], cwd: Optional[Path] = None, 
                   capture_output: bool = False) -> Tuple[int, str, str]:
        """Run a shell command and return exit code, stdout, stderr"""
        if self.verbose:
            self.print_debug(f"Running: {' '.join(cmd)}")
            
        try:
            result = subprocess.run(
                cmd,
                cwd=cwd or self.ig_path,
                capture_output=capture_output,
                text=True
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            self.print_error(f"Command failed: {e}")
            return 1, "", str(e)
            
    def check_environment(self) -> bool:
        """Check if required tools are installed"""
        self.print_header("🔍 Checking Environment")
        
        # Check Node.js
        exit_code, stdout, _ = self.run_command(
            ["node", "--version"], 
            capture_output=True
        )
        if exit_code == 0:
            self.print_success(f"Node.js: {stdout.strip()}")
        else:
            self.print_error("Node.js not found - required for SUSHI")
            return False
            
        # Check NPM
        exit_code, stdout, _ = self.run_command(
            ["npm", "--version"],
            capture_output=True
        )
        if exit_code == 0:
            self.print_success(f"NPM: {stdout.strip()}")
        else:
            self.print_error("NPM not found")
            return False
            
        # Check Python
        self.print_success(f"Python: {sys.version.split()[0]}")
        
        # Check SUSHI
        exit_code, stdout, _ = self.run_command(
            ["npx", "fsh-sushi", "--version"],
            capture_output=True
        )
        if exit_code == 0:
            self.print_success(f"SUSHI: {stdout.strip()}")
        else:
            self.print_warning("SUSHI not found - will be installed by npx")
            
        # Check paths
        self.print_info(f"Workspace: {self.workspace_root}")
        self.print_info(f"IG Path: {self.ig_path}")
        
        if not self.ig_path.exists():
            self.print_error(f"IG directory not found: {self.ig_path}")
            return False
            
        return True
        
    def display_directory_info(self):
        """Display directory structure information"""
        if not self.verbose:
            return
            
        self.print_header("📂 Directory Structure")
        
        self.print_debug("IG directory contents:")
        for item in sorted(self.ig_path.iterdir()):
            print(f"  {item.name}{'/' if item.is_dir() else ''}")
            
        fsh_input = self.ig_path / "input" / "fsh"
        if fsh_input.exists():
            fsh_files = list(fsh_input.rglob("*.fsh"))
            self.print_info(f"Found {len(fsh_files)} FSH files")
            if self.verbose:
                for fsh_file in sorted(fsh_files)[:10]:
                    print(f"  {fsh_file.relative_to(self.ig_path)}")
                if len(fsh_files) > 10:
                    print(f"  ... and {len(fsh_files) - 10} more")
                    
    def run_sushi_build(self) -> bool:
        """Run SUSHI to compile FSH files"""
        self.print_header("🍣 Running SUSHI Build")
        
        self.print_info(f"Working directory: {self.ig_path}")
        
        # Prepare SUSHI command
        cmd = ["npx", "fsh-sushi", "."]
        if not self.use_cache:
            cmd.append("--require-latest")
        else:
            cmd.append("--require-latest")
            
        self.print_info(f"Command: {' '.join(cmd)}")
        print()
        
        # Run SUSHI and capture output
        try:
            with open(self.sushi_log, "w") as log_file:
                process = subprocess.Popen(
                    cmd,
                    cwd=self.ig_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1
                )
                
                # Stream output to both console and log file
                for line in process.stdout:
                    print(line, end='')
                    log_file.write(line)
                    
                process.wait()
                exit_code = process.returncode
                
        except Exception as e:
            self.print_error(f"SUSHI execution failed: {e}")
            return False
            
        print()
        if exit_code == 0:
            self.print_success(f"SUSHI build completed successfully (exit code: 0)")
            return True
        else:
            self.print_error(f"SUSHI build failed (exit code: {exit_code})")
            return False
            
    def analyze_sushi_output(self) -> bool:
        """Analyze SUSHI output for errors and warnings"""
        self.print_header("📊 Analyzing SUSHI Output")
        
        if not self.sushi_log.exists():
            self.print_warning("No SUSHI output log found")
            return True
            
        with open(self.sushi_log, 'r') as f:
            content = f.read()
            
        # Try to extract error/warning counts from SUSHI summary
        error_match = re.search(r'(\d+)\s+Errors?', content)
        warning_match = re.search(r'(\d+)\s+Warnings?', content)
        
        if error_match:
            self.error_count = int(error_match.group(1))
        else:
            # Fallback: count lines with "error"
            self.error_count = content.lower().count('error')
            
        if warning_match:
            self.warning_count = int(warning_match.group(1))
        else:
            # Fallback: count lines with "warn"
            self.warning_count = content.lower().count('warn')
            
        print(f"\n📈 Statistics:")
        print(f"  - Errors: {self.error_count}")
        print(f"  - Warnings: {self.warning_count}")
        
        # Extract and display SUSHI results box
        results_match = re.search(
            r'(={60,}.*?SUSHI RESULTS.*?={60,})',
            content,
            re.DOTALL
        )
        if results_match:
            print(f"\n📦 SUSHI Results Summary:")
            print(results_match.group(1))
            
        return self.error_count == 0
        
    def verify_generated_resources(self) -> bool:
        """Verify that SUSHI generated resources correctly"""
        self.print_header("🔎 Verifying Generated Resources")
        
        if not self.fsh_generated.exists():
            self.print_error("fsh-generated directory not found!")
            if self.verbose:
                self.print_debug("Looking for any generated output...")
                for item in self.ig_path.rglob("*generated*"):
                    print(f"  Found: {item}")
            return False
            
        self.print_success("fsh-generated directory exists")
        
        if not self.resources_path.exists():
            self.print_error("fsh-generated/resources directory not found!")
            return False
            
        self.print_success("fsh-generated/resources directory exists")
        
        # Count resources by type
        print()
        self.print_debug("Counting resources by type...")
        
        json_files = list(self.resources_path.glob("*.json"))
        self.total_resources = len(json_files)
        
        self.profile_count = len(list(self.resources_path.glob("StructureDefinition-*.json")))
        self.valueset_count = len(list(self.resources_path.glob("ValueSet-*.json")))
        self.codesystem_count = len(list(self.resources_path.glob("CodeSystem-*.json")))
        
        # Instances = all JSON files except profiles, valuesets, codesystems, and IG
        ig_files = len(list(self.resources_path.glob("ImplementationGuide-*.json")))
        self.instance_count = (self.total_resources - self.profile_count - 
                              self.valueset_count - self.codesystem_count - ig_files)
        
        print(f"\n📊 Resource counts:")
        print(f"  - Total resources: {self.total_resources}")
        print(f"  - Profiles/Extensions: {self.profile_count}")
        print(f"  - ValueSets: {self.valueset_count}")
        print(f"  - CodeSystems: {self.codesystem_count}")
        print(f"  - Instances: {self.instance_count}")
        
        if self.total_resources == 0:
            self.print_warning("No resources were generated!")
            return False
            
        # Check includes directory
        includes_path = self.fsh_generated / "includes"
        if includes_path.exists():
            self.print_success("Generated includes directory exists")
        else:
            self.print_warning("No includes directory generated")
            
        return True
        
    def validate_json_structure(self) -> bool:
        """Validate all generated JSON files"""
        self.print_header("🧪 Validating JSON Structure")
        
        if not self.resources_path.exists():
            self.print_warning("fsh-generated/resources directory not found - skipping")
            return True
            
        json_files = list(self.resources_path.glob("*.json"))
        
        if not json_files:
            self.print_warning("No JSON files found")
            return True
            
        print(f"\nStarting validation of {len(json_files)} JSON files...")
        print()
        
        valid_count = 0
        invalid_count = 0
        invalid_files = []
        
        for json_file in sorted(json_files):
            filename = json_file.name
            
            if self.verbose:
                print(f"{'─' * 40}")
                print(f"Validating: {filename}")
                
            try:
                with open(json_file, 'r') as f:
                    json.load(f)
                valid_count += 1
                if self.verbose:
                    print(f"  {Colors.OKGREEN}✅ Valid JSON{Colors.ENDC}")
            except json.JSONDecodeError as e:
                invalid_count += 1
                invalid_files.append(filename)
                if self.verbose:
                    print(f"  {Colors.FAIL}❌ Invalid JSON{Colors.ENDC}")
                    print(f"  Error: {e}")
                else:
                    self.print_error(f"Invalid JSON: {filename}")
                    print(f"    Error: {e}")
                    
        print()
        print("=" * 41)
        print("JSON Validation Summary:")
        print(f"  {Colors.OKGREEN}✅ Valid JSON files: {valid_count}{Colors.ENDC}")
        print(f"  {Colors.FAIL}❌ Invalid JSON files: {invalid_count}{Colors.ENDC}")
        print("=" * 41)
        
        if invalid_count > 0:
            print()
            self.print_error(f"JSON validation FAILED - {invalid_count} invalid file(s)")
            return False
        else:
            print()
            self.print_success("All generated JSON files are valid")
            return True
            
    def check_common_issues(self):
        """Check for common issues in SUSHI output"""
        self.print_header("📋 Checking for Common Issues")
        
        if not self.sushi_log.exists():
            self.print_warning("No SUSHI output log to analyze")
            return
            
        with open(self.sushi_log, 'r') as f:
            content = f.read()
            
        issues_found = False
        
        # Check for "could not be found" errors
        not_found = re.findall(r'.*could not be found.*', content, re.IGNORECASE)
        if not_found:
            self.print_warning("Found 'could not be found' errors:")
            for line in not_found[:5]:  # Show first 5
                print(f"  {line.strip()}")
            if len(not_found) > 5:
                print(f"  ... and {len(not_found) - 5} more")
            issues_found = True
            
        # Check for profiles without instances
        no_instances = re.findall(r'.*No instances defined.*', content, re.IGNORECASE)
        if no_instances:
            self.print_info("Profiles without instances (informational):")
            for line in no_instances[:5]:
                print(f"  {line.strip()}")
            if len(no_instances) > 5:
                print(f"  ... and {len(no_instances) - 5} more")
            issues_found = True
            
        # Check for duplicates
        duplicates = re.findall(r'.*duplicate.*', content, re.IGNORECASE)
        if duplicates:
            self.print_warning("Found duplicate definitions:")
            for line in duplicates[:5]:
                print(f"  {line.strip()}")
            if len(duplicates) > 5:
                print(f"  ... and {len(duplicates) - 5} more")
            issues_found = True
            
        # Check for circular dependencies
        circular = re.findall(r'.*circular.*', content, re.IGNORECASE)
        if circular:
            self.print_warning("Found circular dependencies:")
            for line in circular:
                print(f"  {line.strip()}")
            issues_found = True
            
        if not issues_found:
            self.print_success("No common issues found")
            
    def generate_summary(self, success: bool):
        """Generate a summary report"""
        self.print_header("📊 Build & Validation Summary", "=")
        
        print()
        if success:
            print(f"{Colors.BOLD}{Colors.OKGREEN}✅ Build Status: SUCCESS{Colors.ENDC}")
        else:
            print(f"{Colors.BOLD}{Colors.FAIL}❌ Build Status: FAILED{Colors.ENDC}")
            
        print()
        print("┌─────────────────────┬───────┐")
        print("│ Metric              │ Count │")
        print("├─────────────────────┼───────┤")
        print(f"│ Errors              │ {self.error_count:5} │")
        print(f"│ Warnings            │ {self.warning_count:5} │")
        print(f"│ Total Resources     │ {self.total_resources:5} │")
        print(f"│ Profiles/Extensions │ {self.profile_count:5} │")
        print(f"│ ValueSets           │ {self.valueset_count:5} │")
        print(f"│ CodeSystems         │ {self.codesystem_count:5} │")
        print(f"│ Instances           │ {self.instance_count:5} │")
        print("└─────────────────────┴───────┘")
        print()
        
        if success:
            print(f"{Colors.OKGREEN}{'=' * 41}")
            print(f"✅ Build completed successfully!")
            print(f"✅ No errors found")
            print(f"{'=' * 41}{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}{'=' * 41}")
            print(f"❌ Build FAILED - errors detected")
            print(f"❌ Review the output above")
            print(f"{'=' * 41}{Colors.ENDC}")
            
        print()
        self.print_info(f"SUSHI log saved to: {self.sushi_log}")
        self.print_info(f"Generated resources: {self.resources_path}")
        
    def run(self) -> int:
        """Run the complete validation workflow"""
        start_time = datetime.now()
        
        print(f"{Colors.BOLD}{Colors.HEADER}")
        print("=" * 60)
        print("🍣 SUSHI Build & Validate - Local Testing")
        print("=" * 60)
        print(f"{Colors.ENDC}")
        print(f"Started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Step 1: Check environment
        if not self.check_environment():
            self.print_error("Environment check failed")
            return 1
            
        # Step 2: Display directory info
        self.display_directory_info()
        
        # Step 3: Run SUSHI build
        sushi_success = self.run_sushi_build()
        
        # Step 4: Analyze SUSHI output
        analysis_success = self.analyze_sushi_output()
        
        # Step 5: Verify generated resources
        resources_success = self.verify_generated_resources()
        
        # Step 6: Validate JSON structure
        json_success = self.validate_json_structure()
        
        # Step 7: Check for common issues
        self.check_common_issues()
        
        # Step 8: Generate summary
        overall_success = (sushi_success and analysis_success and 
                          resources_success and json_success)
        self.generate_summary(overall_success)
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        print(f"Completed in {duration:.2f} seconds")
        
        return 0 if overall_success else 1


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Local SUSHI build and validation script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 sushi_build_validate.py
  python3 sushi_build_validate.py --verbose
  python3 sushi_build_validate.py --no-cache
        """
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose debugging output'
    )
    
    parser.add_argument(
        '--no-cache',
        action='store_true',
        help="Don't use cached FHIR packages (always download latest)"
    )
    
    args = parser.parse_args()
    
    validator = SushiBuildValidator(
        verbose=args.verbose,
        use_cache=not args.no_cache
    )
    
    try:
        exit_code = validator.run()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}⚠️  Interrupted by user{Colors.ENDC}")
        sys.exit(130)
    except Exception as e:
        print(f"\n{Colors.FAIL}❌ Unexpected error: {e}{Colors.ENDC}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
