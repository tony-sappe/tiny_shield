import sys

MAX_INT = sys.maxsize  # == 2^(63-1) == 9223372036854775807
MIN_INT = -sys.maxsize - 1  # == -2^(63-1) - 1 == 9223372036854775808
MAX_FLOAT = sys.float_info.max  # 1.7976931348623157e+308
MIN_FLOAT = sys.float_info.min  # 2.2250738585072014e-308

DEFAULT_MAX_ITEMS = 5000
DEFAULT_MIN_ITEMS = 1

TINY_SHIELD_SEPARATOR = "|"

SPECIAL_CHARACTERS = {
    "horizontal_tab": ord("\t"),
    "vertical_tab": ord("\v"),
    "ascii_backspace": ord("\b"),
    "ascii_formfeed": ord("\f"),
    "carriage_return": ord("\r"),
    "newline": ord("\n"),
}
