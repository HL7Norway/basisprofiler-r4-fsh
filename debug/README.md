# Debug Tools

This folder contains validation and debugging tools for local development.

## Contents

- **`sushi_build_validate.py`** - Complete SUSHI build & validation (replicates GitHub Actions) ⭐ **RECOMMENDED**
- **`generate_fhir.py`** - Generate FHIR resources to `debug/generated/`
- **`generate.sh`** - Bash wrapper for generation
- **`validate_fsh.py`** - Validate FSH syntax and check generated files
- **`validate.sh`** - Bash wrapper for validation
- **`LOCAL_VALIDATION.md`** - Detailed usage documentation

## Quick Start

### Complete Build & Validation (Recommended)

Run the comprehensive SUSHI build and validation (same as GitHub Actions):

```bash
# Full validation with all checks
python3 debug/sushi_build_validate.py

# With verbose output for debugging
python3 debug/sushi_build_validate.py --verbose

# Force latest package downloads (no cache)
python3 debug/sushi_build_validate.py --no-cache
```

This script:
- ✅ Checks environment (Node.js, NPM, SUSHI)
- ✅ Runs complete SUSHI build
- ✅ Analyzes errors and warnings
- ✅ Verifies all generated resources
- ✅ Validates JSON structure of all files
- ✅ Checks for common issues
- ✅ Generates comprehensive summary report

## Workflow

### 1. Generate FHIR Resources (Local Only)

First, generate FHIR resources from your FSH files:

```bash
# Python
python3 debug/generate_fhir.py

# Or bash
./debug/generate.sh
```

This creates files in `debug/generated/` (gitignored, never committed).

### 2. Validate

Then validate your FSH files and check the generated resources:

```bash
# Python
python3 debug/validate_fsh.py

# Or bash
./debug/validate.sh
```

## Purpose

These tools allow you to:

- Generate FHIR resources locally without committing them
- Test FSH files before pushing to GitHub
- Debug resource generation issues
- Validate generated JSON structures
- Keep your repository clean (generated files are gitignored)

## Generated Files Location

All generated files go to `debug/generated/`:
- `debug/generated/resources/` - FHIR resource JSON files
- `debug/generated/includes/` - Include files
- `debug/generated/data/` - Data files

**Important:** The `debug/generated/` folder is in `.gitignore` and will 
never be committed to GitHub. These are for local testing only.

See [LOCAL_VALIDATION.md](LOCAL_VALIDATION.md) for detailed documentation.
