#!/usr/bin/env python3
"""
FHIR Resource Generator Script
Runs SUSHI to generate FHIR resources locally under debug/generated.
These files are for local testing only and are gitignored.
"""

import subprocess
import sys
import os
import shutil
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


def clean_generated_folder():
    """Clean the debug/generated folder."""
    print_step("Cleaning debug/generated folder")
    
    if GENERATED_PATH.exists():
        try:
            shutil.rmtree(GENERATED_PATH)
            print_success("Cleaned previous generated files")
        except Exception as e:
            print_error(f"Failed to clean generated folder: {e}")
            return False
    
    # Create fresh directory
    GENERATED_PATH.mkdir(parents=True, exist_ok=True)
    return True


def run_sushi():
    """Run SUSHI to generate FHIR resources."""
    print_step("Running SUSHI to generate FHIR resources")
    
    if not IG_PATH.exists():
        print_error(f"IG directory not found: {IG_PATH}")
        return False
    
    # Change to IG directory
    os.chdir(IG_PATH)
    
    # Run SUSHI
    try:
        result = subprocess.run(
            ["sushi", ".", "--require-latest"],
            capture_output=True,
            text=True,
            check=False
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
            print_success("SUSHI generation completed successfully")
            if has_warnings:
                print_warning("Some warnings were found (see above)")
            return True
        else:
            if has_errors:
                print_error("SUSHI generation failed with errors")
            else:
                print_warning("SUSHI generation completed with warnings")
            return result.returncode == 0
            
    except Exception as e:
        print_error(f"Error running SUSHI: {e}")
        return False


def copy_generated_files():
    """Copy generated files from fsh-generated to debug/generated."""
    print_step("Copying generated files to debug/generated")
    
    fsh_generated = IG_PATH / "fsh-generated"
    if not fsh_generated.exists():
        print_error("No fsh-generated folder found")
        return False
    
    try:
        # Copy entire fsh-generated folder to debug/generated
        if (fsh_generated / "resources").exists():
            dest_resources = GENERATED_PATH / "resources"
            dest_resources.mkdir(parents=True, exist_ok=True)
            
            json_files = list((fsh_generated / "resources").glob("*.json"))
            for src_file in json_files:
                dest_file = dest_resources / src_file.name
                shutil.copy2(src_file, dest_file)
            
            print_success(
                f"Copied {len(json_files)} FHIR resource files"
            )
        
        # Copy includes if they exist
        if (fsh_generated / "includes").exists():
            dest_includes = GENERATED_PATH / "includes"
            shutil.copytree(
                fsh_generated / "includes",
                dest_includes,
                dirs_exist_ok=True
            )
            print_success("Copied includes folder")
        
        # Copy data if it exists
        if (fsh_generated / "data").exists():
            dest_data = GENERATED_PATH / "data"
            shutil.copytree(
                fsh_generated / "data",
                dest_data,
                dirs_exist_ok=True
            )
            print_success("Copied data folder")
        
        return True
        
    except Exception as e:
        print_error(f"Failed to copy generated files: {e}")
        return False


def display_summary():
    """Display summary of generated files."""
    print_step("Generated files summary")
    
    resources_dir = GENERATED_PATH / "resources"
    if resources_dir.exists():
        json_files = sorted(resources_dir.glob("*.json"))
        
        # Count by resource type
        resource_types = {}
        for f in json_files:
            # Extract resource type from filename
            name = f.stem
            if "-" in name:
                parts = name.split("-")
                rtype = parts[-1].replace(".StructureDefinition", "")
                rtype = rtype.replace(".json", "")
            else:
                rtype = "Other"
            
            resource_types[rtype] = resource_types.get(rtype, 0) + 1
        
        print(f"\n📊 Total files generated: {len(json_files)}")
        print("\n📁 Files by type:")
        for rtype, count in sorted(
            resource_types.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            print(f"   {rtype}: {count}")
        
        print(f"\n💾 Location: {GENERATED_PATH.relative_to(WORKSPACE_ROOT)}")
        print("   (gitignored - local testing only)")


def main():
    """Main function."""
    print_banner(
        f"FHIR Resource Generator - "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    
    # Check prerequisites
    if not check_sushi_installed():
        return 1
    
    # Clean previous generated files
    if not clean_generated_folder():
        return 1
    
    # Run SUSHI
    if not run_sushi():
        print_error("SUSHI generation failed")
        return 1
    
    # Copy generated files
    if not copy_generated_files():
        return 1
    
    # Display summary
    display_summary()
    
    # Final message
    print_banner("Generation Complete")
    print_success("FHIR resources generated successfully!")
    print(
        f"\n📂 Generated files: "
        f"{GENERATED_PATH.relative_to(WORKSPACE_ROOT)}"
    )
    print("   Use these files for local testing and validation")
    print("   (These files are gitignored and won't be committed)")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
