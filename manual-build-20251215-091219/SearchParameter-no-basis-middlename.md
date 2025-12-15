# no-basis-middlename - v2.2.3-test

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **no-basis-middlename**

## SearchParameter: no-basis-middlename 

| | |
| :--- | :--- |
| *Official URL*:http://hl7.no/fhir/SearchParameter/no-basis-middlename | *Version*:2.2.3-test |
| Active as of 2025-12-15 | *Computable Name*:NoBasisMiddlename |

 
SearchParameter for the Norwegian middlename extension http://hl7.no/fhir/StructureDefinition/no-basis-middlename 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "no-basis-middlename",
  "url" : "http://hl7.no/fhir/SearchParameter/no-basis-middlename",
  "version" : "2.2.3-test",
  "name" : "NoBasisMiddlename",
  "status" : "active",
  "date" : "2025-12-15T09:12:27+00:00",
  "description" : "SearchParameter for the Norwegian middlename extension http://hl7.no/fhir/StructureDefinition/no-basis-middlename",
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
  "code" : "middlename",
  "base" : ["Patient", "Practitioner", "Person"],
  "type" : "string",
  "expression" : "Patient.name.extension.where(url='http://hl7.no/fhir/StructureDefinition/no-basis-middlename').value | Practitioner.name.extension.where(url='http://hl7.no/fhir/StructureDefinition/no-basis-middlename').value | Person.name.extension.where(url='http://hl7.no/fhir/StructureDefinition/no-basis-middlename').value",
  "xpathUsage" : "normal",
  "multipleOr" : true,
  "multipleAnd" : true,
  "modifier" : ["missing", "exact", "contains"]
}

```
