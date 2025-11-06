Instance: no-basis-Procedure-example
InstanceOf: NoBasisProcedure
Title: "No Basis Procedure Example"
Description: "Example of a colonoscopy procedure using no-basis profile"
Usage: #example
* status = #completed
* code.coding.system = "http://snomed.info/sct"
* code.coding.code = #73761001
* code.coding.display = "Colonoscopy (procedure)"
* subject = Reference(PatientExample)
* performer.function.coding.system = "http://snomed.info/sct"
* performer.function.coding.code = #8921000202108
* performer.function.coding.display = "Primary performing endoscopist (person)"
* performer.actor = Reference(Magnar-Komann-Practitioner)
* bodySite.coding.system = "http://snomed.info/sct"
* bodySite.coding.code = #485005
* bodySite.coding.display = "TC - Transverse colon"
