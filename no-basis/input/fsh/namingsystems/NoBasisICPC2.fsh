Instance: no-basis-icpc-2
InstanceOf: NamingSystem
Usage: #definition
* meta.versionId = "2.1.1"
* name = "NoBasisICPC2"
* status = #active
* kind = #codesystem
* date = "2021-11-02"
* publisher = "HL7 Norway"
* responsible = "Wonca International Classification Committee (WICC)"
* description = "In Norway primary care uses ICPC-2 to document contact-reason, health related problem and diagnosis."

* uniqueId[0].type = #uri
* uniqueId[0].value = "http://hl7.org/fhir/sid/icpc-2"
* uniqueId[0].preferred = true

* uniqueId[+].type = #oid
* uniqueId[=].value = "2.16.840.1.113883.6.139"
* uniqueId[=].preferred = false

* uniqueId[+].type = #oid
* uniqueId[=].value = "2.16.578.1.12.4.1.1.7170"
* uniqueId[=].preferred = false
* uniqueId[=].comment = "Volven oid for ICPC-2 codesystem for use in Norwegian legacy implementations."
