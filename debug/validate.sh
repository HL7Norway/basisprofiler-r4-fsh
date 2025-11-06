#!/bin/bash
# Quick validation runner for bash/zsh users
# Run from repo root: ./debug/validate.sh
# Or from debug folder: ./validate.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT" || exit 1
python3 "$SCRIPT_DIR/validate_fsh.py"
