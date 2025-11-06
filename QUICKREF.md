# Quick Reference - Debug Tools

## Generate FHIR Resources

```bash
./debug/generate.sh
```

Generates FHIR resources to `debug/generated/` (gitignored).

## Validate FSH + Generated Files

```bash
./debug/validate.sh
```

Validates FSH syntax and checks generated resources.

## Workflow

1. **Generate**: `./debug/generate.sh` → Creates files in `debug/generated/`
2. **Validate**: `./debug/validate.sh` → Checks FSH and generated files

## Important

- ✅ Scripts in `debug/` are committed to git
- ❌ Files in `debug/generated/` are NOT committed (gitignored)
- 📁 All generated files stay local for testing only

See [debug/README.md](debug/README.md) for full documentation.
