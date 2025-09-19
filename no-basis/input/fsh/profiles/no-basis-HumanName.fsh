Profile: NoBasisHumanName
Parent: HumanName
Id: no-basis-HumanName
Title: "no-basis-HumanName"
Description: "Basisprofil for Norwegian HumanName. Defined by The Norwegian Directorate of eHealth and HL7 Norway. The profile adds the concept of middlename and further explains the use for the data-elements in a Norwegian context. The basis profile is open, but derived profiles should close down the information elements according to specification relevant to the use-case."
* ^url = "http://hl7.no/fhir/StructureDefinition/no-basis-HumanName"
* ^version = "2.0.15"
* ^status = #active
* ^date = "2019-05-20"
* ^fhirVersion = #4.0.1
* ^kind = #complex-type
* ^abstract = false
* extension contains no-basis-middlename 0..1
* extension[no-basis-middlename] only http://hl7.no/fhir/StructureDefinition/no-basis-middlename
* extension[no-basis-middlename] ^short = "Defines a middle name"
* extension[no-basis-middlename] ^definition = "Defines a middle name as a specific extension as this is widely used in Norwegian names. The middlename is defined in norwegian legislation (lov om personnavn)."
* family ^definition = "Ref. 'lov om personnavn' for further details about Norwegian HumanNames. The part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father."
* family ^alias[0] = "etternavn"
* given ^short = "Given names (not always 'first')"
* given ^definition = "Given name. In Norway Given name does not include middlenames according to the regulation for norwegian names. Multiple given names are however legal. Ref. 'Lov om personnavn' for further details about Norwegian HumanNames."
* given ^alias[0] = "fornavn"
* prefix ^short = "Prefix is not used in Norwegian names"
* prefix ^definition = "This is not a part of official Norwegian names as defined in 'lov om personnavn' regulation. Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the start of the name."
* prefix ^mustSupport = false
* suffix ^short = "Suffix is not used in Norwegian human names"
* suffix ^definition = "This is not a part of official Norwegian names as defined in 'lov om personnavn' regulation. Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the end of the name."
* suffix ^mustSupport = false
* ^short = "Norwegian human name"
* ^definition = "Defines the format of norwegian human name according to norwegian legislation (lov om personnavn)."
