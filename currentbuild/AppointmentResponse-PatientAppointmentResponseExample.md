# PatientAppointmentResponseExample - v2.2.3-test

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **PatientAppointmentResponseExample**

## Example AppointmentResponse: PatientAppointmentResponseExample

Profile: [no-basis-AppointmentResponse](StructureDefinition-no-basis-AppointmentResponse.md)

**no-basis-shortnotice**: true

**appointment**: [MRI results discussion](Appointment-AppointmentExample.md)

**actor**: [Peter James Chalmers](Patient-PatientExample.md)

**participantStatus**: Accepted



## Resource Content

```json
{
  "resourceType" : "AppointmentResponse",
  "id" : "PatientAppointmentResponseExample",
  "meta" : {
    "profile" : [
      "http://hl7.no/fhir/ig/StructureDefinition/no-basis-AppointmentResponse"
    ]
  },
  "extension" : [
    {
      "url" : "http://hl7.no/fhir/ig/StructureDefinition/no-basis-shortnotice",
      "valueBoolean" : true
    }
  ],
  "appointment" : {
    "reference" : "Appointment/AppointmentExample",
    "display" : "MRI results discussion"
  },
  "actor" : {
    "reference" : "Patient/PatientExample",
    "type" : "Patient",
    "display" : "Peter James Chalmers"
  },
  "participantStatus" : "accepted"
}

```
