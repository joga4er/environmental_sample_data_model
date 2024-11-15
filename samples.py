# Auto generated from samples.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-15T16:35:10
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
from linkml_runtime.linkml_model.types import String

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
class EnvironmentalSampleLcmsCode(extended_str):
    pass


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
    sample_name: Optional[str] = None
    researcher_initials: Optional[Union[str, "ResearcherInitialEnums"]] = None
    sample_type: Optional[Union[str, "SampleTypeEnums"]] = None
    purpose: Optional[str] = None
    related_parent_sample: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.lcms_code):
            self.MissingRequiredField("lcms_code")
        if not isinstance(self.lcms_code, EnvironmentalSampleLcmsCode):
            self.lcms_code = EnvironmentalSampleLcmsCode(self.lcms_code)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.researcher_initials is not None and not isinstance(self.researcher_initials, ResearcherInitialEnums):
            self.researcher_initials = ResearcherInitialEnums(self.researcher_initials)

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnums):
            self.sample_type = SampleTypeEnums(self.sample_type)

        if self.purpose is not None and not isinstance(self.purpose, str):
            self.purpose = str(self.purpose)

        if self.related_parent_sample is not None and not isinstance(self.related_parent_sample, str):
            self.related_parent_sample = str(self.related_parent_sample)

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
                   model_uri=DEFAULT_.sample_name, domain=None, range=Optional[str])

slots.researcher_initials = Slot(uri=DEFAULT_.researcher_initials, name="researcher_initials", curie=DEFAULT_.curie('researcher_initials'),
                   model_uri=DEFAULT_.researcher_initials, domain=None, range=Optional[Union[str, "ResearcherInitialEnums"]])

slots.sample_type = Slot(uri=DEFAULT_.sample_type, name="sample_type", curie=DEFAULT_.curie('sample_type'),
                   model_uri=DEFAULT_.sample_type, domain=None, range=Optional[Union[str, "SampleTypeEnums"]])

slots.purpose = Slot(uri=DEFAULT_.purpose, name="purpose", curie=DEFAULT_.curie('purpose'),
                   model_uri=DEFAULT_.purpose, domain=None, range=Optional[str])

slots.related_parent_sample = Slot(uri=DEFAULT_.related_parent_sample, name="related_parent_sample", curie=DEFAULT_.curie('related_parent_sample'),
                   model_uri=DEFAULT_.related_parent_sample, domain=None, range=Optional[str],
                   pattern=re.compile(r'[/d{2}///d{4}]'))

slots.listOfSamples__samples = Slot(uri=DEFAULT_.samples, name="listOfSamples__samples", curie=DEFAULT_.curie('samples'),
                   model_uri=DEFAULT_.listOfSamples__samples, domain=None, range=Optional[Union[Dict[Union[str, EnvironmentalSampleLcmsCode], Union[dict, EnvironmentalSample]], List[Union[dict, EnvironmentalSample]]]])
