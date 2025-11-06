# FSH Validation Analysis Report

**Run ID:** 19132610909
**Date:** 2025-11-06 10:30:38 UTC
**Workflow:** validate-fsh.yml
**Repository:** HL7Norway/basisprofiler-r4-fsh
**Branch:** main
**Commit:** b618782739340e4c2a83b0d4077f9da34b362def

## Configuration

- **SUSHI Validation:** true
- **Fail on SUSHI Errors:** false
- **Generate Analysis Log:** true
- **IG Short Name:** no-basis

## FSH Validator Results

❌ **No FSH validator log found**

## SUSHI Validation Results

### Summary Statistics

| Metric | Count |
|--------|------:|
| Errors | 1 |
| Warnings | 1 |

### Generated Resources

**Total:** 66 JSON files

### Full SUSHI Log

<details>
<summary>Click to expand full log</summary>

```
info  Running SUSHI v3.16.5 (implements FHIR Shorthand specification v3.0.0)
info  Arguments:
info    --require-latest
info    /home/runner/work/basisprofiler-r4-fsh/basisprofiler-r4-fsh/no-basis
info  No output path specified. Output to .
info  Using configuration file: /home/runner/work/basisprofiler-r4-fsh/basisprofiler-r4-fsh/no-basis/sushi-config.yaml
info  Importing FSH text...
info  Preprocessed 66 documents with 17 aliases.
info  Imported 44 definitions and 21 instances.
info  Loaded virtual package sushi-r5forR4#1.0.0 with 7 resources
info  Resolved hl7.fhir.uv.tools.r4#latest to concrete version 0.8.0
info  Loaded hl7.fhir.uv.tools.r4#0.8.0 with 110 resources
info  Resolved hl7.terminology.r4#latest to concrete version 6.5.0
info  Loaded hl7.terminology.r4#6.5.0 with 4392 resources
info  Resolved hl7.fhir.uv.extensions.r4#latest to concrete version 5.2.0
info  Loaded hl7.fhir.uv.extensions.r4#5.2.0 with 759 resources
info  Loaded hl7.fhir.r4.core#4.0.1 with 4581 resources
info  Loaded virtual package sushi-local#LOCAL with 3 resources
info  Converting FSH to FHIR resources...
info  Converted 33 FHIR StructureDefinitions.
info  Converted 4 FHIR CodeSystems.
info  Converted 7 FHIR ValueSets.
info  Converted 21 FHIR instances.
info  Exporting FHIR resources as JSON...
info  Exported 65 FHIR resources as JSON.
info  Assembling Implementation Guide sources...
info  Generated ImplementationGuide-hl7.fhir.no.basis.json
info  Assembled Implementation Guide sources; ready for IG Publisher.
info  The sample-ig located at https://github.com/FHIR/sample-ig contains scripts useful for downloading and running the IG Publisher.

========================= SUSHI RESULTS ===========================
|  -------------------------------------------------------------  |
| |    Profiles   |  Extensions  |   Logicals   |   Resources   | |
| |-------------------------------------------------------------| |
| |      20       |      13      |      0       |       0       | |
|  -------------------------------------------------------------  |
|  -------------------------------------------------------------  |
| |      ValueSets     |    CodeSystems    |     Instances      | |
| |-------------------------------------------------------------| |
| |         7          |         4         |         21         | |
|  -------------------------------------------------------------  |
|                                                                 |
===================================================================
| O-fish-ally error free!                0 Errors      0 Warnings |
===================================================================

```

</details>

## Analysis & Recommendations

### For AI Review (Claude Sonnet)

When reviewing this log, please analyze:

1. **Validation Status:**
   - Are there any real errors that need fixing?
   - Are warnings acceptable or should they be addressed?
   - Is the "No instances defined" count expected?

2. **Pattern Analysis:**
   - Are there recurring error patterns?
   - Do multiple profiles have the same issues?
   - Are there systemic problems vs isolated issues?

3. **Recommendations:**
   - What files need to be modified?
   - Should workflow configuration be adjusted?
   - Are there missing example instances that should be created?

### Workflow Health Check

- **Action Versions:** All updated to latest (v5/v6)
- **Error Filtering:** Excludes 'No instances defined' from failures ✅
- **Exit Code Handling:** fsh-validator runs with `|| true` ✅

---

_Generated automatically by validate-fsh.yml workflow_
