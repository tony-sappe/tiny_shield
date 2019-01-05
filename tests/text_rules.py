TEXT_RULE_BASE = {"name": "test", "type": "text", "key": "test", "optional": False}

TEXT_SEARCH_RULE_PLAIN = {**TEXT_RULE_BASE, **{"value": "hello world", "text_type": "search"}}
TEXT_SEARCH_RULE_ODD_CHARS = {**TEXT_RULE_BASE, **{"value": "odd ch\faract\ters", "text_type": "search"}}
TEXT_SEARCH_RULE_WHITESPACE = {**TEXT_RULE_BASE, **{"value": "    what whitespace?", "text_type": "search"}}
TEXT_SEARCH_RULE_NON_STRING = {**TEXT_RULE_BASE, **{"value": 753930843, "text_type": "search"}}

TEXT_URL_RULE_PLAIN = {**TEXT_RULE_BASE, **{"value": "http://yabber.io", "text_type": "url"}}
TEXT_URL_RULE_SPACE = {**TEXT_RULE_BASE, **{"value": "hello world", "text_type": "url"}}
TEXT_URL_RULE_URI = {**TEXT_RULE_BASE, **{"value": "postgres://read:changeme@127.0.0.1:5432/db", "text_type": "url"}}
TEXT_URL_RULE_NON_STRING = {**TEXT_RULE_BASE, **{"value": [1, 4, 5], "text_type": "url"}}
