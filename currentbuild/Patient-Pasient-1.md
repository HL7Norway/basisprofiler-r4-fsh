# Pasient-1 - v2.2.3-test

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Pasient-1**

## Example Patient: Pasient-1

Profile: [no-basis-Patient](StructureDefinition-no-basis-Patient.md)

Rita Lin (no stated gender), DoB Unknown ( urn:oid:2.16.578.1.12.4.1.4.1#13031353453)

-------



## Resource Content

```json
{
  "resourceType" : "Patient",
  "id" : "Pasient-1",
  "meta" : {
    "profile" : ["http://hl7.no/fhir/ig/StructureDefinition/no-basis-Patient"]
  },
  "identifier" : [
    {
      "system" : "urn:oid:2.16.578.1.12.4.1.4.1",
      "value" : "13031353453"
    }
  ],
  "name" : [
    {
      "family" : "Lin",
      "given" : ["Rita"]
    }
  ]
}

```
