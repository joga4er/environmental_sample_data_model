# Auto generated from samples.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-21T10:55:09
# Schema: samples
#
# id: https://w3id.org/linkml/examples/
# description: List of environmental samples run in the Lohmann lab.
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
from linkml_runtime.linkml_model.types import Decimal, String
from linkml_runtime.utils.metamodelcore import Decimal

metamodel_version = "1.7.0"
version = "0.0.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCIT = CurieNamespace('ncit', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/OBI_')
PUBCHEM = CurieNamespace('pubchem', 'https://pubchem.ncbi.nlm.nih.gov/compound/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
UO = CurieNamespace('uo', 'http://purl.obolibrary.org/obo/UO_')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/linkml/examples/')


# Types

# Class references
class SamplingLocationFieldName(extended_str):
    pass


class EnvironmentalSampleLcmsCode(extended_str):
    pass


@dataclass(repr=False)
class SamplingLocation(YAMLRoot):
    """
    Comprises relevant information on the place the environmental sample was collected from.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["examples/SamplingLocation"]
    class_class_curie: ClassVar[str] = "linkml:examples/SamplingLocation"
    class_name: ClassVar[str] = "SamplingLocation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/linkml/examples/SamplingLocation")

    field_name: Union[str, SamplingLocationFieldName] = None
    latitude: str = None
    longitude: str = None
    field_description: Optional[str] = None
    country_name: Optional[str] = None
    height: Optional[str] = None
    depth: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.field_name):
            self.MissingRequiredField("field_name")
        if not isinstance(self.field_name, SamplingLocationFieldName):
            self.field_name = SamplingLocationFieldName(self.field_name)

        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, str):
            self.latitude = str(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, str):
            self.longitude = str(self.longitude)

        if self.field_description is not None and not isinstance(self.field_description, str):
            self.field_description = str(self.field_description)

        if self.country_name is not None and not isinstance(self.country_name, str):
            self.country_name = str(self.country_name)

        if self.height is not None and not isinstance(self.height, str):
            self.height = str(self.height)

        if self.depth is not None and not isinstance(self.depth, Decimal):
            self.depth = Decimal(self.depth)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentalSample(YAMLRoot):
    """
    Comprises relevent data from environmental samples.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["examples/EnvironmentalSample"]
    class_class_curie: ClassVar[str] = "linkml:examples/EnvironmentalSample"
    class_name: ClassVar[str] = "EnvironmentalSample"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/linkml/examples/EnvironmentalSample")

    lcms_code: Union[str, EnvironmentalSampleLcmsCode] = None
    sample_name: str = None
    researcher_initials: Union[str, "ResearcherInitialEnums"] = None
    sample_type: Union[str, "SampleTypeEnums"] = None
    purpose: Optional[str] = None
    related_parent_sample: Optional[str] = None
    restricted: Optional[Union[str, "RestrictionEnums"]] = None
    location: Optional[Union[str, SamplingLocationFieldName]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.lcms_code):
            self.MissingRequiredField("lcms_code")
        if not isinstance(self.lcms_code, EnvironmentalSampleLcmsCode):
            self.lcms_code = EnvironmentalSampleLcmsCode(self.lcms_code)

        if self._is_empty(self.sample_name):
            self.MissingRequiredField("sample_name")
        if not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self._is_empty(self.researcher_initials):
            self.MissingRequiredField("researcher_initials")
        if not isinstance(self.researcher_initials, ResearcherInitialEnums):
            self.researcher_initials = ResearcherInitialEnums(self.researcher_initials)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, SampleTypeEnums):
            self.sample_type = SampleTypeEnums(self.sample_type)

        if self.purpose is not None and not isinstance(self.purpose, str):
            self.purpose = str(self.purpose)

        if self.related_parent_sample is not None and not isinstance(self.related_parent_sample, str):
            self.related_parent_sample = str(self.related_parent_sample)

        if self.restricted is not None and not isinstance(self.restricted, RestrictionEnums):
            self.restricted = RestrictionEnums(self.restricted)

        if self.location is not None and not isinstance(self.location, SamplingLocationFieldName):
            self.location = SamplingLocationFieldName(self.location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListOfSamples(YAMLRoot):
    """
    List of PFAS components encoding general information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["examples/ListOfSamples"]
    class_class_curie: ClassVar[str] = "linkml:examples/ListOfSamples"
    class_name: ClassVar[str] = "ListOfSamples"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/linkml/examples/ListOfSamples")

    samples: Optional[Union[Dict[Union[str, EnvironmentalSampleLcmsCode], Union[dict, EnvironmentalSample]], List[Union[dict, EnvironmentalSample]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="samples", slot_type=EnvironmentalSample, key_name="lcms_code", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class MissingValueEnum(EnumDefinitionImpl):

    nan = PermissibleValue(text="nan")

    _defn = EnumDefinition(
        name="MissingValueEnum",
    )

class ResearcherInitialEnums(EnumDefinitionImpl):

    AH = PermissibleValue(
        text="AH",
        description="Asta Habtemichael")
    IH = PermissibleValue(
        text="IH",
        description="Izak Hill")
    JA = PermissibleValue(
        text="JA",
        description="Juliana Agudelo")
    JSN = PermissibleValue(
        text="JSN",
        description="Jarod Snook")
    JB = PermissibleValue(
        text="JB",
        description="Jitka Becanova")
    JSA = PermissibleValue(
        text="JSA",
        description="Justin Sankey")
    KS = PermissibleValue(
        text="KS",
        description="Kelsey Staniec")
    LG = PermissibleValue(
        text="LG",
        description="Liam Geyer")
    MW = PermissibleValue(
        text="MW",
        description="Melissa Woodward")
    OS = PermissibleValue(
        text="OS",
        description="Olga Skende")
    SV = PermissibleValue(
        text="SV",
        description="Simon Vojta")
    TE = PermissibleValue(
        text="TE",
        description="Taylor Elpers")
    TG = PermissibleValue(
        text="TG",
        description="Thomas Garrow")
    RL = PermissibleValue(
        text="RL",
        description="Rainer Lohmann")
    RN = PermissibleValue(
        text="RN",
        description="Rachel Nelson")

    _defn = EnumDefinition(
        name="ResearcherInitialEnums",
    )

class RestrictionEnums(EnumDefinitionImpl):

    restricted = PermissibleValue(
        text="restricted",
        description="sample data may not be published or shared")
    open = PermissibleValue(
        text="open",
        description="sample data may be published or shared")

    _defn = EnumDefinition(
        name="RestrictionEnums",
    )

class SampleTypeEnums(EnumDefinitionImpl):

    blank = PermissibleValue(
        text="blank",
        description="blank sample (field blank, lab blank, process blank, method blank, etc.)")
    matrix_spike = PermissibleValue(
        text="matrix_spike",
        description="spiked sample, where known PFAS amounts have been added")
    pfas_quantification = PermissibleValue(
        text="pfas_quantification",
        description="sample where pfas levels will be quantified")

    _defn = EnumDefinition(
        name="SampleTypeEnums",
    )

# Slots
class slots:
    pass

slots.lcms_code = Slot(uri=DEFAULT_.lcms_code, name="lcms_code", curie=DEFAULT_.curie('lcms_code'),
                   model_uri=DEFAULT_.lcms_code, domain=None, range=URIRef,
                   pattern=re.compile(r'[/d{2}///d{4}]'))

slots.sample_name = Slot(uri=DEFAULT_.sample_name, name="sample_name", curie=DEFAULT_.curie('sample_name'),
                   model_uri=DEFAULT_.sample_name, domain=None, range=str)

slots.researcher_initials = Slot(uri=DEFAULT_.researcher_initials, name="researcher_initials", curie=DEFAULT_.curie('researcher_initials'),
                   model_uri=DEFAULT_.researcher_initials, domain=None, range=Union[str, "ResearcherInitialEnums"])

slots.sample_type = Slot(uri=DEFAULT_.sample_type, name="sample_type", curie=DEFAULT_.curie('sample_type'),
                   model_uri=DEFAULT_.sample_type, domain=None, range=Union[str, "SampleTypeEnums"])

slots.purpose = Slot(uri=DEFAULT_.purpose, name="purpose", curie=DEFAULT_.curie('purpose'),
                   model_uri=DEFAULT_.purpose, domain=None, range=Optional[str])

slots.related_parent_sample = Slot(uri=DEFAULT_.related_parent_sample, name="related_parent_sample", curie=DEFAULT_.curie('related_parent_sample'),
                   model_uri=DEFAULT_.related_parent_sample, domain=None, range=Optional[str],
                   pattern=re.compile(r'[/d{2}///d{4}]'))

slots.restricted = Slot(uri=DEFAULT_.restricted, name="restricted", curie=DEFAULT_.curie('restricted'),
                   model_uri=DEFAULT_.restricted, domain=None, range=Optional[Union[str, "RestrictionEnums"]])

slots.location = Slot(uri=DEFAULT_.location, name="location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.location, domain=None, range=Optional[Union[str, SamplingLocationFieldName]])

slots.field_name = Slot(uri=DEFAULT_.field_name, name="field_name", curie=DEFAULT_.curie('field_name'),
                   model_uri=DEFAULT_.field_name, domain=None, range=URIRef)

slots.field_description = Slot(uri=DEFAULT_.field_description, name="field_description", curie=DEFAULT_.curie('field_description'),
                   model_uri=DEFAULT_.field_description, domain=None, range=Optional[str])

slots.latitude = Slot(uri=NCIT.C68642, name="latitude", curie=NCIT.curie('C68642'),
                   model_uri=DEFAULT_.latitude, domain=None, range=str,
                   pattern=re.compile(r'[/d{1,2}./d{6}]'))

slots.longitude = Slot(uri=NCIT.C68643, name="longitude", curie=NCIT.curie('C68643'),
                   model_uri=DEFAULT_.longitude, domain=None, range=str,
                   pattern=re.compile(r'[/d{1,2,3}./d{6}]'))

slots.country_name = Slot(uri=OBI['0001627'], name="country_name", curie=OBI.curie('0001627'),
                   model_uri=DEFAULT_.country_name, domain=None, range=Optional[str])

slots.height = Slot(uri=NCIT.C25347, name="height", curie=NCIT.curie('C25347'),
                   model_uri=DEFAULT_.height, domain=None, range=Optional[str],
                   pattern=re.compile(r'[/d{1,2,3}./d{2}]'))

slots.depth = Slot(uri=NCIT.C25333, name="depth", curie=NCIT.curie('C25333'),
                   model_uri=DEFAULT_.depth, domain=None, range=Optional[Decimal])

slots.listOfSamples__samples = Slot(uri=DEFAULT_.samples, name="listOfSamples__samples", curie=DEFAULT_.curie('samples'),
                   model_uri=DEFAULT_.listOfSamples__samples, domain=None, range=Optional[Union[Dict[Union[str, EnvironmentalSampleLcmsCode], Union[dict, EnvironmentalSample]], List[Union[dict, EnvironmentalSample]]]])
