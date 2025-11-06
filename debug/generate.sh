#!/bin/bash
# Generate FHIR resources using SUSHI
# Run from repo root: ./debug/generate.sh
# Or from debug folder: ./generate.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT" || exit 1
python3 "$SCRIPT_DIR/generate_fhir.py"
