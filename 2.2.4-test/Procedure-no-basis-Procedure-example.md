# No Basis Procedure Example - v2.2.4-test

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **No Basis Procedure Example**

## Example Procedure: No Basis Procedure Example

Profile: [no-basis-Procedure](StructureDefinition-no-basis-Procedure.md)

**status**: Completed

**code**: Colonoscopy (procedure)

**subject**: [Peter James Chalmers (official) (no stated gender), DoB Unknown](Patient-PatientExample.md)

### Performers

| | | |
| :--- | :--- | :--- |
| - | **Function** | **Actor** |
| * | Primary performing endoscopist (person) | [Practitioner Magnar Koman](Practitioner-Magnar-Komann-Practitioner.md) |

**bodySite**: TC - Transverse colon



## Resource Content

```json
{
  "resourceType" : "Procedure",
  "id" : "no-basis-Procedure-example",
  "meta" : {
    "profile" : [
      "http://hl7.no/fhir/ig/StructureDefinition/no-basis-Procedure"
    ]
  },
  "status" : "completed",
  "code" : {
    "coding" : [
      {
        "system" : "http://snomed.info/sct",
        "code" : "73761001",
        "display" : "Colonoscopy (procedure)"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/PatientExample"
  },
  "performer" : [
    {
      "function" : {
        "coding" : [
          {
            "system" : "http://snomed.info/sct",
            "code" : "8921000202108",
            "display" : "Primary performing endoscopist (person)"
          }
        ]
      },
      "actor" : {
        "reference" : "Practitioner/Magnar-Komann-Practitioner"
      }
    }
  ],
  "bodySite" : [
    {
      "coding" : [
        {
          "system" : "http://snomed.info/sct",
          "code" : "485005",
          "display" : "TC - Transverse colon"
        }
      ]
    }
  ]
}

```
