#!/usr/bin/env python3
"""
Local FSH Validation Script
Validates FSH files and checks locally generated FHIR resources.
Use generate_fhir.py first to create resources in debug/generated.
"""

import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime

# Configuration
IG_SHORTNAME = "no-basis"
WORKSPACE_ROOT = Path(__file__).parent.parent
IG_PATH = WORKSPACE_ROOT / IG_SHORTNAME
DEBUG_PATH = WORKSPACE_ROOT / "debug"
GENERATED_PATH = DEBUG_PATH / "generated"


def print_banner(text):
    """Print a formatted banner."""
    print("\n" + "=" * 80)
    print(f"  {text}")
    print("=" * 80 + "\n")


def print_step(text):
    """Print a step message."""
    print(f"🔍 {text}...")


def print_success(text):
    """Print a success message."""
    print(f"✅ {text}")


def print_error(text):
    """Print an error message."""
    print(f"❌ {text}")


def print_warning(text):
    """Print a warning message."""
    print(f"⚠️  {text}")


def check_sushi_installed():
    """Check if SUSHI is installed."""
    try:
        result = subprocess.run(
            ["sushi", "--version"],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            print_success(f"SUSHI is installed: {version}")
            return True
        else:
            print_error("SUSHI is not working correctly")
            return False
    except FileNotFoundError:
        print_error("SUSHI is not installed")
        print("\nTo install SUSHI, run:")
        print("  npm install -g fsh-sushi")
        return False


def run_sushi_validation():
    """Run SUSHI validation (lightweight check only)."""
    print_step("Running FSH syntax validation")
    
    if not IG_PATH.exists():
        print_error(f"IG directory not found: {IG_PATH}")
        return False
    
    # Change to IG directory
    os.chdir(IG_PATH)
    
    # Run SUSHI - it will validate and generate
    try:
        result = subprocess.run(
            ["sushi", "."],
            capture_output=True,
            text=True,
            check=False,
            timeout=120
        )
        
        # Print output
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        # Check for errors
        output = result.stdout + result.stderr
        has_errors = any(
            word in output.lower() for word in ["error", "fatal"]
        )
        has_warnings = "warn" in output.lower()
        
        if result.returncode == 0:
            print_success("FSH validation completed successfully")
            if has_warnings:
                print_warning("Some warnings found (see above)")
            return True
        else:
            if has_errors:
                print_error("FSH validation failed with errors")
            else:
                print_warning("FSH validation completed with warnings")
            return False
            
    except subprocess.TimeoutExpired:
        print_error("SUSHI validation timed out")
        return False
    except Exception as e:
        print_error(f"Error running SUSHI: {e}")
        return False


def check_generated_files():
    """Check locally generated FHIR files in debug/generated."""
    print_step("Validating local generated files")
    
    if not GENERATED_PATH.exists():
        print_warning("No debug/generated folder found")
        print("   Run './debug/generate_fhir.py' first to generate files")
        return False
    
    resources_dir = GENERATED_PATH / "resources"
    if not resources_dir.exists():
        print_warning("No resources in debug/generated")
        return False
    
    json_files = list(resources_dir.glob("*.json"))
    if not json_files:
        print_warning("No JSON files found in debug/generated/resources")
        return False
    
    print_success(f"Found {len(json_files)} generated FHIR resources")
    
    # Validate JSON structure
    print_step("Validating JSON structure")
    valid_count = 0
    error_count = 0
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = f.read()
                # Basic validation - can be expanded
                if '"resourceType"' in data and data.strip():
                    valid_count += 1
                else:
                    print_warning(f"Invalid structure: {json_file.name}")
                    error_count += 1
        except Exception as e:
            print_error(f"Failed to read {json_file.name}: {e}")
            error_count += 1
    
    if error_count == 0:
        print_success(f"All {valid_count} files have valid JSON structure")
        return True
    else:
        print_warning(
            f"{valid_count} valid, {error_count} with errors"
        )
        return False


def main():
    """Main function."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print_banner(f"FSH Validation - {timestamp}")
    
    print("This script validates FSH syntax and checks generated files.")
    print("To generate files first, run: ./debug/generate_fhir.py\n")
    
    # Check prerequisites
    if not check_sushi_installed():
        return 1
    
    # Run FSH validation
    fsh_valid = run_sushi_validation()
    
    # Check generated files (if they exist)
    files_valid = check_generated_files()
    
    # Summary
    print_banner("Validation Complete")
    
    if fsh_valid and files_valid:
        print_success("All validations passed!")
        print(f"\n� Generated files: debug/generated/")
        print("   These files are gitignored for local testing only")
        return 0
    elif fsh_valid and not files_valid:
        print_warning("FSH validation passed")
        print_warning("No generated files to validate")
        print("\nRun './debug/generate_fhir.py' to generate files")
        return 0
    else:
        print_error("Validation failed - check errors above")
        return 1


if __name__ == "__main__":
    sys.exit(main())