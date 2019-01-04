from .constants import MAX_ITEMS
from .validators import SUPPORTED_TEXT_TYPES
from .validators import validate_array
from .validators import validate_boolean
from .validators import validate_datetime
from .validators import validate_enum
from .validators import validate_float
from .validators import validate_integer
from .validators import validate_object
from .validators import validate_text


VALIDATORS = {
    "array": {"func": validate_array, "required_fields": ["array_type"], "defaults": {}},
    "boolean": {"func": validate_boolean, "required_fields": [], "defaults": {}},
    "date": {"func": validate_datetime, "required_fields": [], "defaults": {}},
    "datetime": {"func": validate_datetime, "required_fields": [], "defaults": {}},
    "enum": {"func": validate_enum, "required_fields": ["enum_values"], "defaults": {}},
    "float": {"func": validate_float, "required_fields": [], "defaults": {}},
    "integer": {"func": validate_integer, "required_fields": [], "defaults": {}},
    "object": {"func": validate_object, "required_fields": ["object_keys"], "defaults": {}},
    "passthrough": {
        "func": lambda k: k["value"],  # Allow any value provided. Not recommended for production code
        "required_fields": [],
        "defaults": {},
    },
    "schema": {"func": lambda k: None, "required_fields": [], "defaults": {}},
    "text": {
        "func": validate_text,
        "types": SUPPORTED_TEXT_TYPES,
        "required_fields": ["text_type"],
        "defaults": {"min": 1, "max": MAX_ITEMS},
    },
}
