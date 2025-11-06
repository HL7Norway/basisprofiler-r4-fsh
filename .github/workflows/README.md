# GitHub Actions Workflows - FSH Validation

This repository contains two validation workflows for FHIR Shorthand (FSH) files.

## Workflows Overview

### 1. `validate-fsh.yml` - FSH Validator Only
**Purpose**: Lightweight syntax validation of FSH files  
**Triggers**: Manual (workflow_dispatch)  
**Duration**: ~1-2 minutes

**What it does**:
- ✅ Validates FSH syntax using `fsh-validator`
- ✅ Optional SUSHI build (manual trigger)
- ✅ Fast feedback on FSH syntax errors

**When to use**:
- Quick syntax checks during development
- Pre-commit validation
- When you only need to verify FSH syntax

**Manual triggers**:
- `run_sushi_validation`: Enable/disable SUSHI build
- `fail_on_sushi_errors`: Control if SUSHI errors fail the workflow

---

### 2. `sushi-build-validate.yml` - Complete SUSHI Build ⭐ **RECOMMENDED**
**Purpose**: Full FHIR resource generation and validation  
**Triggers**: 
- Pull requests (automatic)
- Push to main (automatic)  
- Manual (workflow_dispatch)

**Duration**: ~3-5 minutes

**What it does**:
- ✅ Compiles FSH to FHIR JSON using SUSHI
- ✅ Generates all profiles, extensions, ValueSets, CodeSystems, instances
- ✅ Validates JSON structure
- ✅ Checks for common issues (missing resources, duplicates, circular dependencies)
- ✅ Provides detailed statistics and summaries
- ✅ Uploads generated resources as artifacts
- ✅ **Fails on errors** (enforces quality)

**When to use**:
- Before merging pull requests
- After making changes to FSH files
- When you need to verify complete resource generation
- To download generated FHIR resources

---

## Workflow Comparison

| Feature | validate-fsh.yml | sushi-build-validate.yml |
|---------|------------------|--------------------------|
| FSH Syntax Check | ✅ | ✅ (via SUSHI) |
| FHIR Resource Generation | Optional | ✅ Always |
| JSON Validation | ❌ | ✅ |
| Resource Statistics | ❌ | ✅ |
| Issue Detection | ❌ | ✅ |
| Artifact Upload | FSH + logs | FSH + JSON + logs |
| Auto-trigger on PR | ❌ (commented) | ✅ |
| Auto-trigger on Push | ❌ (commented) | ✅ |
| Fail on Errors | Optional | ✅ Always |
| FHIR Package Caching | ✅ | ✅ |

---

## Usage Examples

### Quick FSH Syntax Check
```bash
# Use validate-fsh.yml with SUSHI disabled (default)
# Go to Actions → Validate FSH Files → Run workflow
```

### Full Build and Validation (Recommended)
```bash
# sushi-build-validate.yml runs automatically on:
# - Pull requests
# - Push to main

# Or trigger manually:
# Go to Actions → SUSHI Build & Validate → Run workflow
```

### Download Generated Resources
After `sushi-build-validate.yml` runs:
1. Go to the workflow run
2. Scroll to "Artifacts"
3. Download `sushi-build-{run_id}`
4. Extract to see all generated JSON files

---

## Output Examples

### validate-fsh.yml Output
```
📊 FSH Validation Results:
==========================
✅ FSH validation passed successfully

🍣 SUSHI Validation Results: (if enabled)
============================
0 Errors, 0 Warnings
```

### sushi-build-validate.yml Output
```
📊 Build Statistics:
┌─────────────────────┬───────┐
│ Metric              │ Count │
├─────────────────────┼───────┤
│ Errors              │ 0     │
│ Warnings            │ 0     │
│ Total Resources     │ 65    │
│ Profiles/Extensions │ 33    │
│ ValueSets           │ 7     │
│ CodeSystems         │ 4     │
│ Instances           │ 21    │
└─────────────────────┴───────┘

✅ Build completed successfully with no errors
```

---

## Troubleshooting

### "Extension could not be found" errors
- **Cause**: Old package dependencies or incorrect paths
- **Fixed**: Both workflows no longer install `hl7.fhir.no.basis-2.2.0-snapshots`
- **Solution**: SUSHI automatically resolves local extensions

### "No instances defined for profile" messages
- **Nature**: Informational, not actual errors
- **Impact**: Does not cause build failure
- **Action**: Optional - create example instances if needed

### Build failures
1. Check the job summary for error counts
2. Download artifacts to inspect generated resources
3. Review SUSHI output log for specific error messages
4. Common issues:
   - Duplicate names → Add unique suffixes
   - Missing references → Verify instance names match
   - Syntax errors → Check FSH syntax

---

## Best Practices

1. **Use `sushi-build-validate.yml` for CI/CD** - It runs automatically on PRs
2. **Use `validate-fsh.yml` for quick checks** - Faster feedback during development
3. **Review artifacts** - Download generated resources to verify output
4. **Fix errors before merging** - `sushi-build-validate.yml` will fail on errors
5. **Monitor warnings** - Address warnings to maintain code quality

---

## Maintenance

Both workflows are configured for the `no-basis` IG:
- Working directory: `no-basis/`
- FSH source: `no-basis/input/fsh/`
- Generated output: `no-basis/fsh-generated/`
- Configuration: `no-basis/sushi-config.yaml`

To modify:
- Change `IG_SHORTNAME` environment variable in workflow files
- Update path patterns in trigger conditions
