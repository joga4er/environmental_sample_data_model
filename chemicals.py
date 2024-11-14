# Auto generated from chemicals.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-14T18:55:22
# Schema: chemicals
#
# id: https://w3id.org/linkml/examples/
# description: List of PFAS components considered in PFAS quantification for targeted LC-MS. This schema is organized in Conatiner class PFASList, a parent class PFAS containing descriptions of the chemical itself, and the children class MSchemical providing details on the LCMS.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, String

metamodel_version = "1.7.0"
version = "0.0.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MS = CurieNamespace('ms', 'http://purl.obolibrary.org/obo/MS_')
NCIT = CurieNamespace('ncit', 'http://purl.obolibrary.org/obo/NCIT_')
PUBCHEM = CurieNamespace('pubchem', 'https://pubchem.ncbi.nlm.nih.gov/compound/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
UO = CurieNamespace('uo', 'http://purl.obolibrary.org/obo/UO_')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/linkml/examples/')


# Types

# Class references
class ChemicalSubstanceInternalName(extended_str):
    pass


@dataclass(repr=False)
class MSChemical(YAMLRoot):
    """
    Encodes relevent information for mass spectrometry
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["examples/MSChemical"]
    class_class_curie: ClassVar[str] = "linkml:examples/MSChemical"
    class_name: ClassVar[str] = "MSChemical"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/linkml/examples/MSChemical")

    precursor_channel_name: Optional[str] = None
    precursor_m_z_ratio: Optional[float] = None
    precursor_retention_time: Optional[float] = None
    fragment_channel_name: Optional[str] = None
    fragment_m_z_ratio: Optional[float] = None
    fragment_retention_time: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.precursor_channel_name is not None and not isinstance(self.precursor_channel_name, str):
            self.precursor_channel_name = str(self.precursor_channel_name)

        if self.precursor_m_z_ratio is not None and not isinstance(self.precursor_m_z_ratio, float):
            self.precursor_m_z_ratio = float(self.precursor_m_z_ratio)

        if self.precursor_retention_time is not None and not isinstance(self.precursor_retention_time, float):
            self.precursor_retention_time = float(self.precursor_retention_time)

        if self.fragment_channel_name is not None and not isinstance(self.fragment_channel_name, str):
            self.fragment_channel_name = str(self.fragment_channel_name)

        if self.fragment_m_z_ratio is not None and not isinstance(self.fragment_m_z_ratio, float):
            self.fragment_m_z_ratio = float(self.fragment_m_z_ratio)

        if self.fragment_retention_time is not None and not isinstance(self.fragment_retention_time, float):
            self.fragment_retention_time = float(self.fragment_retention_time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalSubstance(YAMLRoot):
    """
    PFAS component, which is quantified in targeted LCMS.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["ChemicalSubstance"]
    class_class_curie: ClassVar[str] = "schema:ChemicalSubstance"
    class_name: ClassVar[str] = "ChemicalSubstance"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/linkml/examples/ChemicalSubstance")

    internal_name: Union[str, ChemicalSubstanceInternalName] = None
    pubchem: str = None
    cas: str = None
    name: Optional[str] = None
    smiles: Optional[str] = None
    chemical: Optional[Union[dict, MSChemical]] = None
    ida: Optional[Union[dict, MSChemical]] = None
    ips: Optional[Union[dict, MSChemical]] = None
    instrumentation_detection_limit: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.internal_name):
            self.MissingRequiredField("internal_name")
        if not isinstance(self.internal_name, ChemicalSubstanceInternalName):
            self.internal_name = ChemicalSubstanceInternalName(self.internal_name)

        if self._is_empty(self.pubchem):
            self.MissingRequiredField("pubchem")
        if not isinstance(self.pubchem, str):
            self.pubchem = str(self.pubchem)

        if self._is_empty(self.cas):
            self.MissingRequiredField("cas")
        if not isinstance(self.cas, str):
            self.cas = str(self.cas)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.chemical is not None and not isinstance(self.chemical, MSChemical):
            self.chemical = MSChemical(**as_dict(self.chemical))

        if self.ida is not None and not isinstance(self.ida, MSChemical):
            self.ida = MSChemical(**as_dict(self.ida))

        if self.ips is not None and not isinstance(self.ips, MSChemical):
            self.ips = MSChemical(**as_dict(self.ips))

        if self.instrumentation_detection_limit is not None and not isinstance(self.instrumentation_detection_limit, float):
            self.instrumentation_detection_limit = float(self.instrumentation_detection_limit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListOfChemicals(YAMLRoot):
    """
    List of PFAS components encoding general information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["examples/ListOfChemicals"]
    class_class_curie: ClassVar[str] = "linkml:examples/ListOfChemicals"
    class_name: ClassVar[str] = "ListOfChemicals"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/linkml/examples/ListOfChemicals")

    pfas: Optional[Union[Dict[Union[str, ChemicalSubstanceInternalName], Union[dict, ChemicalSubstance]], List[Union[dict, ChemicalSubstance]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="pfas", slot_type=ChemicalSubstance, key_name="internal_name", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class MissingValueEnum(EnumDefinitionImpl):

    nan = PermissibleValue(text="nan")

    _defn = EnumDefinition(
        name="MissingValueEnum",
    )

# Slots
class slots:
    pass

slots.internal_name = Slot(uri=DEFAULT_.internal_name, name="internal_name", curie=DEFAULT_.curie('internal_name'),
                   model_uri=DEFAULT_.internal_name, domain=None, range=URIRef)

slots.precursor_channel_name = Slot(uri=DEFAULT_.precursor_channel_name, name="precursor_channel_name", curie=DEFAULT_.curie('precursor_channel_name'),
                   model_uri=DEFAULT_.precursor_channel_name, domain=None, range=Optional[str])

slots.fragment_channel_name = Slot(uri=DEFAULT_.fragment_channel_name, name="fragment_channel_name", curie=DEFAULT_.curie('fragment_channel_name'),
                   model_uri=DEFAULT_.fragment_channel_name, domain=None, range=Optional[str])

slots.precursor_m_z_ratio = Slot(uri=DEFAULT_.precursor_m_z_ratio, name="precursor_m_z_ratio", curie=DEFAULT_.curie('precursor_m_z_ratio'),
                   model_uri=DEFAULT_.precursor_m_z_ratio, domain=None, range=Optional[float])

slots.fragment_m_z_ratio = Slot(uri=DEFAULT_.fragment_m_z_ratio, name="fragment_m_z_ratio", curie=DEFAULT_.curie('fragment_m_z_ratio'),
                   model_uri=DEFAULT_.fragment_m_z_ratio, domain=None, range=Optional[float])

slots.precursor_retention_time = Slot(uri=MS['1000894'], name="precursor_retention_time", curie=MS.curie('1000894'),
                   model_uri=DEFAULT_.precursor_retention_time, domain=None, range=Optional[float])

slots.fragment_retention_time = Slot(uri=MS['1000894'], name="fragment_retention_time", curie=MS.curie('1000894'),
                   model_uri=DEFAULT_.fragment_retention_time, domain=None, range=Optional[float])

slots.ida = Slot(uri=DEFAULT_.ida, name="ida", curie=DEFAULT_.curie('ida'),
                   model_uri=DEFAULT_.ida, domain=None, range=Optional[Union[dict, MSChemical]])

slots.ips = Slot(uri=DEFAULT_.ips, name="ips", curie=DEFAULT_.curie('ips'),
                   model_uri=DEFAULT_.ips, domain=None, range=Optional[Union[dict, MSChemical]])

slots.name = Slot(uri=DEFAULT_.name, name="name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.pubchem = Slot(uri=NCIT.C54563, name="pubchem", curie=NCIT.curie('C54563'),
                   model_uri=DEFAULT_.pubchem, domain=None, range=str)

slots.cas = Slot(uri=NCIT.C54682, name="cas", curie=NCIT.curie('C54682'),
                   model_uri=DEFAULT_.cas, domain=None, range=str)

slots.smiles = Slot(uri=MS['1000868'], name="smiles", curie=MS.curie('1000868'),
                   model_uri=DEFAULT_.smiles, domain=None, range=Optional[str])

slots.instrumentation_detection_limit = Slot(uri=DEFAULT_.instrumentation_detection_limit, name="instrumentation_detection_limit", curie=DEFAULT_.curie('instrumentation_detection_limit'),
                   model_uri=DEFAULT_.instrumentation_detection_limit, domain=None, range=Optional[float])

slots.chemical = Slot(uri=DEFAULT_.chemical, name="chemical", curie=DEFAULT_.curie('chemical'),
                   model_uri=DEFAULT_.chemical, domain=None, range=Optional[Union[dict, MSChemical]])

slots.listOfChemicals__pfas = Slot(uri=DEFAULT_.pfas, name="listOfChemicals__pfas", curie=DEFAULT_.curie('pfas'),
                   model_uri=DEFAULT_.listOfChemicals__pfas, domain=None, range=Optional[Union[Dict[Union[str, ChemicalSubstanceInternalName], Union[dict, ChemicalSubstance]], List[Union[dict, ChemicalSubstance]]]])
