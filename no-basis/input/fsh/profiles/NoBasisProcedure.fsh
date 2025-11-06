Profile: NoBasisProcedure
Parent: Procedure
Id: no-basis-Procedure
Title: "no-basis-Procedure"
Description: "Basis profile for a procedure, to be used in Norway. The profile is adapted to include norwegian specific features and constraints."
* ^version = "2.1.0"
* ^status = #active
* ^date = "2021-10-27"

* code.coding ^slicing.discriminator.type = #value
* code.coding ^slicing.discriminator.path = "$this"
* code.coding ^slicing.rules = #open

* code.coding contains
    NKPK 0..1 and
    SNOMED-CT 0..1 and
    ICPC-2 0..1

* code.coding[NKPK] ^short = "Codes defined by Norsk Klinisk Prosedyrekodeverk (NCMP, NCSP og NCRP)"
* code.coding[NKPK] ^definition = "A reference to a code defined by Norsk Klinisk Prosedyrekodeverk (NCMP, NCSP og NCRP)"
* code.coding[NKPK].system = "urn:oid:2.16.578.1.12.4.1.1.7275"

* code.coding[SNOMED-CT] ^short = "Code defined by SNOMED CT"
* code.coding[SNOMED-CT] ^definition = "A reference to a code defined SNOMED CT."
* code.coding[SNOMED-CT].system = "http://snomed.info/sct"

* code.coding[ICPC-2] ^short = "Code defined by a ICPC-2"
* code.coding[ICPC-2] ^definition = "A reference to a code defined by ICPC-2"
* code.coding[ICPC-2].system = "http://hl7.org/fhir/sid/icpc-2"

* bodySite ^binding.strength = #preferred
