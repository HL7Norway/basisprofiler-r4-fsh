# no-basis-Procedure - v2.2.4-test

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **no-basis-Procedure**

## Resource Profile: no-basis-Procedure 

| | |
| :--- | :--- |
| *Official URL*:http://hl7.no/fhir/ig/StructureDefinition/no-basis-Procedure | *Version*:2.2.4-test |
| Draft as of 2021-10-27 | *Computable Name*:NoBasisProcedure |

 
Basis profile for a procedure, to be used in Norway. The profile is adapted to include norwegian specific features and constraints. 

**Usages:**

* Examples for this Profile: [Procedure/no-basis-Procedure-example](Procedure-no-basis-Procedure-example.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/hl7.fhir.no.basis|current/StructureDefinition/no-basis-Procedure)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-no-basis-Procedure.csv), [Excel](StructureDefinition-no-basis-Procedure.xlsx), [Schematron](StructureDefinition-no-basis-Procedure.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "no-basis-Procedure",
  "url" : "http://hl7.no/fhir/ig/StructureDefinition/no-basis-Procedure",
  "version" : "2.2.4-test",
  "name" : "NoBasisProcedure",
  "title" : "no-basis-Procedure",
  "status" : "draft",
  "date" : "2021-10-27",
  "description" : "Basis profile for a procedure, to be used in Norway. The profile is adapted to include norwegian specific features and constraints.",
  "jurisdiction" : [
    {
      "coding" : [
        {
          "system" : "urn:iso:std:iso:3166",
          "code" : "NO",
          "display" : "Norway"
        }
      ]
    }
  ],
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
    },
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    },
    {
      "identity" : "w5",
      "uri" : "http://hl7.org/fhir/fivews",
      "name" : "FiveWs Pattern Mapping"
    },
    {
      "identity" : "v2",
      "uri" : "http://hl7.org/v2",
      "name" : "HL7 v2 Mapping"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Procedure",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Procedure",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Procedure",
        "path" : "Procedure"
      },
      {
        "id" : "Procedure.code.coding",
        "path" : "Procedure.code.coding",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "value",
              "path" : "$this"
            }
          ],
          "rules" : "open"
        }
      },
      {
        "id" : "Procedure.code.coding:NKPK",
        "path" : "Procedure.code.coding",
        "sliceName" : "NKPK",
        "short" : "Codes defined by Norsk Klinisk Prosedyrekodeverk (NCMP, NCSP og NCRP)",
        "definition" : "A reference to a code defined by Norsk Klinisk Prosedyrekodeverk (NCMP, NCSP og NCRP)",
        "min" : 0,
        "max" : "1"
      },
      {
        "id" : "Procedure.code.coding:NKPK.system",
        "path" : "Procedure.code.coding.system",
        "fixedUri" : "urn:oid:2.16.578.1.12.4.1.1.7275"
      },
      {
        "id" : "Procedure.code.coding:SNOMED-CT",
        "path" : "Procedure.code.coding",
        "sliceName" : "SNOMED-CT",
        "short" : "Code defined by SNOMED CT",
        "definition" : "A reference to a code defined SNOMED CT.",
        "min" : 0,
        "max" : "1"
      },
      {
        "id" : "Procedure.code.coding:SNOMED-CT.system",
        "path" : "Procedure.code.coding.system",
        "fixedUri" : "http://snomed.info/sct"
      },
      {
        "id" : "Procedure.code.coding:ICPC-2",
        "path" : "Procedure.code.coding",
        "sliceName" : "ICPC-2",
        "short" : "Code defined by a ICPC-2",
        "definition" : "A reference to a code defined by ICPC-2",
        "min" : 0,
        "max" : "1"
      },
      {
        "id" : "Procedure.code.coding:ICPC-2.system",
        "path" : "Procedure.code.coding.system",
        "fixedUri" : "http://hl7.org/fhir/sid/icpc-2"
      },
      {
        "id" : "Procedure.bodySite",
        "path" : "Procedure.bodySite",
        "binding" : {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",
              "valueString" : "BodySite"
            }
          ],
          "strength" : "preferred",
          "description" : "Codes describing anatomical locations. May include laterality.",
          "valueSet" : "http://hl7.org/fhir/ValueSet/body-site"
        }
      }
    ]
  }
}

```
