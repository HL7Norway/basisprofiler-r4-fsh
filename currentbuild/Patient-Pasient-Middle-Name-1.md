# Pasient-Middle-Name-1 - v2.2.3-test

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Pasient-Middle-Name-1**

## Example Patient: Pasient-Middle-Name-1

Profile: [no-basis-Patient](StructureDefinition-no-basis-Patient.md)

Grieg Edvard (no stated gender), DoB Unknown ( urn:oid:2.16.578.1.12.4.1.4.1#15064312345)

-------



## Resource Content

```json
{
  "resourceType" : "Patient",
  "id" : "Pasient-Middle-Name-1",
  "meta" : {
    "profile" : ["http://hl7.no/fhir/ig/StructureDefinition/no-basis-Patient"]
  },
  "identifier" : [
    {
      "system" : "urn:oid:2.16.578.1.12.4.1.4.1",
      "value" : "15064312345"
    }
  ],
  "name" : [
    {
      "extension" : [
        {
          "url" : "http://hl7.no/fhir/ig/StructureDefinition/no-basis-middlename",
          "valueString" : "Hagerup"
        }
      ],
      "family" : "Edvard",
      "given" : ["Grieg"]
    }
  ]
}

```
