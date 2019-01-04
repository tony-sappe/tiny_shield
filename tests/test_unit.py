import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tiny_shield.utils.validators import *

from tiny_shield.utils.constants import TINY_SHIELD_SEPARATOR


ARRAY_RULE = {
    "name": "test",
    "type": "array",
    "key": "filters|test",
    "array_type": "integer",
    "optional": True,
    "array_min": 1,
    "array_max": 3,
    "value": [1, 2, 3],
}
BOOLEAN_RULE = {
    "name": "test",
    "type": "boolean",
    "key": "filters{}test".format(TINY_SHIELD_SEPARATOR),
    "optional": True,
    "value": True,
}
DATETIME_RULE = {
    "name": "test",
    "type": "datetime",
    "key": "filters{}test".format(TINY_SHIELD_SEPARATOR),
    "optional": True,
    "value": "1984-09-16T4:05:00",
}
ENUM_RULE = {
    "name": "test",
    "type": "enum",
    "key": "filters{}test".format(TINY_SHIELD_SEPARATOR),
    "enum_values": ["foo", "bar"],
    "optional": True,
    "value": "foo",
}
FLOAT_RULE = {
    "name": "test",
    "type": "float",
    "key": "filters{}test".format(TINY_SHIELD_SEPARATOR),
    "optional": True,
    "value": 3.14,
    "min": 2,
    "max": 4,
}
TEXT_RULE = {
    "name": "test",
    "type": "text",
    "key": "filters{}test".format(TINY_SHIELD_SEPARATOR),
    "optional": True,
    "value": "hello world",
    "text_type": "search",
}
INTEGER_RULE = {
    "name": "test",
    "type": "float",
    "key": "filters{}test".format(TINY_SHIELD_SEPARATOR),
    "optional": True,
    "value": 3,
    "min": 2,
    "max": 4,
}
OBJECT_RULE = {
    "name": "test",
    "type": "object",
    "key": "filters{}test".format(TINY_SHIELD_SEPARATOR),
    "object_keys": {"foo": {"type": "string", "optional": False}, "hello": {"type": "integer", "optional": False}},
    "value": {"foo": "bar", "hello": 1},
}


"""
Beacuse these functions all raise Exceptions on failure, all we need to do to write the unit tests is call the function.
If an exception is raised, the test will fail
"""


def test_validate_array():
    returned_value = validate_array(ARRAY_RULE)
    assert ARRAY_RULE["value"] == returned_value


def test_validate_boolean():
    returned_value = validate_boolean(BOOLEAN_RULE)
    assert BOOLEAN_RULE["value"] == returned_value


def test_validate_datetime():
    returned_value = validate_datetime(DATETIME_RULE)
    assert "1984-09-16T04:05:00Z" == returned_value


def test_validate_enum():
    returned_value = validate_enum(ENUM_RULE)
    assert ENUM_RULE["value"] == returned_value


def test_validate_float():
    returned_value = validate_float(FLOAT_RULE)
    assert FLOAT_RULE["value"] == returned_value


def test_validate_integer():
    returned_value = validate_integer(INTEGER_RULE)
    assert INTEGER_RULE["value"] == returned_value


def test_validate_text():
    returned_value = validate_text(TEXT_RULE)
    assert TEXT_RULE["value"] == returned_value


def test_validate_object():
    returned_value = validate_object(OBJECT_RULE)
    assert OBJECT_RULE["value"] == returned_value
