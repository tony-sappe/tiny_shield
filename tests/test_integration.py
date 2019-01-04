import copy
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tiny_shield.tiny_shield import TinyShield
from tiny_shield.utils.constants import TINY_SHIELD_SEPARATOR


FILTER_OBJ = {
    "filters": {
        "keywords": ["grumpy", "bungle"],
        "award_type_codes": ["A", "B", "C", "D"],
        "time_period": [{"start_date": "2008-01-01", "end_date": "2011-01-31"}],
        "place_of_performance_scope": "domestic",
        "place_of_performance_locations": [{"country": "USA", "state": "VA", "county": "059"}],
        "agencies": [
            {"type": "funding", "tier": "toptier", "name": "Office of Pizza"},
            {"type": "awarding", "tier": "subtier", "name": "Personal Pizza"},
        ],
        "recipient_search_text": ["D12345678"],
        "recipient_scope": "domestic",
        "recipient_locations": [{"country": "USA", "state": "VA", "county": "059"}],
        "recipient_type_names": ["Small Business", "Alaskan Native Owned Business"],
        "award_ids": ["1605SS17F00018"],
        "award_amounts": [
            {"lower_bound": 1000000.00, "upper_bound": 25000000.00},
            {"upper_bound": 1000000.00},
            {"lower_bound": 500000000.00},
        ],
        "program_numbers": ["10.553"],
        "naics_codes": ["336411"],
        "psc_codes": ["1510"],
        "contract_pricing_type_codes": ["SAMPLECODE123"],
        "set_aside_type_codes": ["SAMPLECODE123"],
        "extent_competed_type_codes": ["SAMPLECODE123"],
    }
}


TS = None

AWARD_FILTER = [
    {"name": "award_ids", "type": "array", "array_type": "text", "text_type": "search"},
    {"name": "award_type_codes", "type": "array", "array_type": "enum", "enum_values": ["A", "B", "C", "D", "E", "F"]},
    {"name": "contract_pricing_type_codes", "type": "array", "array_type": "text", "text_type": "search"},
    {"name": "extent_competed_type_codes", "type": "array", "array_type": "text", "text_type": "search"},
    {"name": "keywords", "type": "array", "array_type": "text", "text_type": "search", "text_min": 3},
    {"name": "legal_entities", "type": "array", "array_type": "integer"},
    {"name": "naics_codes", "type": "array", "array_type": "text", "text_type": "search"},
    {"name": "place_of_performance_scope", "type": "enum", "enum_values": ["domestic", "foreign"]},
    {"name": "program_numbers", "type": "array", "array_type": "text", "text_type": "search"},
    {"name": "psc_codes", "type": "array", "array_type": "text", "text_type": "search"},
    {"name": "recipient_id", "type": "text", "text_type": "search"},
    {"name": "recipient_scope", "type": "enum", "enum_values": ("domestic", "foreign")},
    {"name": "recipient_search_text", "type": "array", "array_type": "text", "text_type": "search"},
    {"name": "recipient_type_names", "type": "array", "array_type": "text", "text_type": "search"},
    {"name": "set_aside_type_codes", "type": "array", "array_type": "text", "text_type": "search"},
    {
        "name": "time_period",
        "type": "array",
        "array_type": "object",
        "object_keys": {
            "start_date": {"type": "date", "min": "2007-10-01", "max": "2017-10-01"},
            "end_date": {"type": "date", "min": "2007-10-01", "max": "2017-10-01"},
            "date_type": {
                "type": "enum",
                "enum_values": ["action_date", "last_modified_date"],
                "optional": True,
                "default": "action_date",
            },
        },
    },
    {
        "name": "award_amounts",
        "type": "array",
        "array_type": "object",
        "object_keys": {
            "lower_bound": {"type": "float", "optional": True},
            "upper_bound": {"type": "float", "optional": True},
        },
    },
    {
        "name": "agencies",
        "type": "array",
        "array_type": "object",
        "object_keys": {
            "type": {"type": "enum", "enum_values": ["funding", "awarding"], "optional": False},
            "tier": {"type": "enum", "enum_values": ["toptier", "subtier"], "optional": False},
            "name": {"type": "text", "text_type": "search", "optional": False},
        },
    },
    {
        "name": "recipient_locations",
        "type": "array",
        "array_type": "object",
        "object_keys": {
            "country": {"type": "text", "text_type": "search", "optional": False},
            "state": {"type": "text", "text_type": "search", "optional": True},
            "zip": {"type": "text", "text_type": "search", "optional": True},
            "district": {"type": "text", "text_type": "search", "optional": True},
            "county": {"type": "text", "text_type": "search", "optional": True},
        },
    },
    {
        "name": "place_of_performance_locations",
        "type": "array",
        "array_type": "object",
        "object_keys": {
            "country": {"type": "text", "text_type": "search", "optional": False},
            "state": {"type": "text", "text_type": "search", "optional": True},
            "zip": {"type": "text", "text_type": "search", "optional": True},
            "district": {"type": "text", "text_type": "search", "optional": True},
            "county": {"type": "text", "text_type": "search", "optional": True},
        },
    },
]

for a in AWARD_FILTER:
    a["optional"] = a.get("optional", True)  # future TODO: want to make time_period required
    a["key"] = "filters{sep}{name}".format(sep=TINY_SHIELD_SEPARATOR, name=a["name"])


def test_check_models():
    """We want this test to fail if either AWARD_FILTERS has an invalid model,
    OR if the logic of the check_models function has been corrupted.
    It will fail if an exception is raised. Otherwise it will define the global TS object
    so we can use it in the remaining tests."""
    global TS
    TS = TinyShield(copy.deepcopy(AWARD_FILTER))


def test_recurse_append():
    mydict = {}
    struct = ["level1", "level2"]
    data = "foobar"
    TS.recurse_append(struct, mydict, data)
    assert mydict == {"level1": {"level2": "foobar"}}


def test_parse_request():
    request = FILTER_OBJ
    TS.parse_request(request)
    assert all("value" in item for item in TS.rules)


def test_enforce_rules():
    TS.enforce_rules()
    assert TS.data == FILTER_OBJ
