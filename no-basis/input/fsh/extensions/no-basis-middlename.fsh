Extension: NoBasisMiddlename
Id: no-basis-middlename
Title: "no-basis-middlename"
Description: "The basis extension defines the Norwegian middlename which is called 'mellomnavn' and defined by Norwegian legislation (Lov om personnavn)."
* ^url = "http://hl7.no/fhir/StructureDefinition/no-basis-middlename"
* ^version = "2.0.6"
* ^status = #active
* ^date = "2019-09-23"
* ^publisher = "Direktoratet for e-helse"
* ^purpose = "Specific usage of middle name as a specific part of official name standard where name order is important"
* ^context[+].type = #element
* ^context[=].expression = "HumanName"
* ^kind = #complex-type
* ^abstract = false
// url constraint not needed for extension definition
* valueString 1..1
  * ^short = "The middle name of a person"
  * ^definition = "The middle name of a person. The middlename should be a norwegian middlename as defined by norwegian legislation (Lov om personnavn)."
  * ^alias[0] = "mellomnavn"
