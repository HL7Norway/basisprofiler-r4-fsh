# GitHub Issue: Resolve FSH duplicate name warnings by adding VS suffix to ValueSets

**Title:** Resolve FSH duplicate name warnings by adding VS suffix to ValueSets

**Labels:** enhancement

---

## Problem

SUSHI validation warns about duplicate FSH entity names:

```
warn  Detected FSH entity definitions with duplicate names. While FSH allows for 
duplicate names across entity types, they can lead to ambiguous results when 
referring to these entities by name elsewhere (e.g., in references). Consider 
using unique names in FSH declarations and assigning duplicated names using 
caret assignment rules instead. 

Detected duplicate names: 
- NoBasisConnectionType
- NoBasisFamilyRelation
- NoBasisMaritalStatus
- NoBasisParentalResponsibility
```

Each of these names is used for both a CodeSystem and a ValueSet, creating ambiguity when referenced elsewhere in FSH files.

## Solution Implemented

Following FHIR best practices, all ValueSets have been renamed with a `VS` suffix to disambiguate them from their corresponding CodeSystems:

### Changes Made

1. **NoBasisConnectionType** → **NoBasisConnectionTypeVS**
   - File: `no-basis/input/fsh/valuesets/NoBasisConnectionType.fsh`
   - Updated reference in: `no-basis/input/fsh/profiles/NoBasisEndpoint.fsh`

2. **NoBasisFamilyRelation** → **NoBasisFamilyRelationVS**
   - File: `no-basis/input/fsh/valuesets/NoBasisFamilyRelation.fsh`
   - Updated reference in: `no-basis/input/fsh/profiles/NoBasisRelatedPerson.fsh`

3. **NoBasisMaritalStatus** → **NoBasisMaritalStatusVS**
   - File: `no-basis/input/fsh/valuesets/NoBasisMaritalStatus.fsh`
   - Updated reference in: `no-basis/input/fsh/profiles/NoBasisRelatedPerson.fsh`

4. **NoBasisParentalResponsibility** → **NoBasisParentalResponsibilityVS**
   - File: `no-basis/input/fsh/valuesets/NoBasisParentalResponsibility.fsh`
   - Updated reference in: `no-basis/input/fsh/profiles/NoBasisRelatedPerson.fsh`

### CodeSystems (unchanged)

The corresponding CodeSystems retain their original names:
- `NoBasisConnectionType` (CodeSystem)
- `NoBasisFamilyRelation` (CodeSystem)
- `NoBasisMaritalStatus` (CodeSystem)
- `NoBasisParentalResponsibility` (CodeSystem)

## Why This Approach?

This follows the common FHIR convention where:
- **CodeSystems** keep clean names (referenced frequently in value set includes)
- **ValueSets** get a `VS` suffix for clarity when used in binding statements

## Impact

- ✅ Removes SUSHI warning about duplicate names
- ✅ Makes FSH references unambiguous
- ✅ Improves code maintainability
- ⚠️ Breaking change for any external references to these ValueSet names

## Review Needed

Please review these changes and confirm:
1. The naming convention is acceptable for the Norwegian basis profiles
2. No external dependencies will be broken
3. The changes align with HL7 Norway's naming standards

## Related Files Modified

- `no-basis/input/fsh/valuesets/NoBasisConnectionType.fsh`
- `no-basis/input/fsh/valuesets/NoBasisFamilyRelation.fsh`
- `no-basis/input/fsh/valuesets/NoBasisMaritalStatus.fsh`
- `no-basis/input/fsh/valuesets/NoBasisParentalResponsibility.fsh`
- `no-basis/input/fsh/profiles/NoBasisEndpoint.fsh`
- `no-basis/input/fsh/profiles/NoBasisRelatedPerson.fsh`

---

**To create this issue manually:**
1. Go to https://github.com/HL7Norway/basisprofiler-r4-fsh/issues/new
2. Copy the content above
3. Add label: `enhancement`
