from tiny_shield.utils.constants import TINY_SHIELD_SEPARATOR
from tiny_shield.utils.validators import *
from tiny_shield.utils.exceptions import InvalidParameterException
from .text_rules import *

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


def test_validate_array():
    assert ARRAY_RULE["value"] == validate_array(ARRAY_RULE)


def test_validate_boolean():
    assert BOOLEAN_RULE["value"] == validate_boolean(BOOLEAN_RULE)


def test_validate_datetime():
    assert "1984-09-16T04:05:00Z" == validate_datetime(DATETIME_RULE)


def test_validate_enum():
    assert ENUM_RULE["value"] == validate_enum(ENUM_RULE)


def test_validate_float():
    assert FLOAT_RULE["value"] == validate_float(FLOAT_RULE)


def test_validate_integer():
    assert INTEGER_RULE["value"] == validate_integer(INTEGER_RULE)


def test_validate_text_simple():
    assert TEXT_SEARCH_RULE_1["value"] == validate_text(TEXT_SEARCH_RULE_1)


def test_validate_text_special_chars():
    assert "odd characters" == validate_text(TEXT_SEARCH_RULE_2)


def test_validate_text_whitespace():
    assert "what whitespace?" == validate_text(TEXT_SEARCH_RULE_3)


def test_validate_text_integer():
    try:
        validate_text(TEXT_SEARCH_RULE_4)
        raise Exception("InvalidParameterException should have been raised!!!")
    except InvalidParameterException as e:
        pass


def test_validate_text_url():
    assert "http%3A%2F%2Fyabber.io" == validate_text(TEXT_URL_RULE_1)


def test_validate_text_url_2():
    assert "hello+world" == validate_text(TEXT_URL_RULE_2)


def test_validate_text_url3():
    assert "postgres%3A%2F%2Freadonly%3Achangeme%40127.0.0.1%3A5432%2Fpostgres" == validate_text(TEXT_URL_RULE_3)


def test_validate_object():
    returned_value = validate_object(OBJECT_RULE)
    assert OBJECT_RULE["value"] == returned_value
