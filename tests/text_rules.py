TEXT_RULE_BASE = {"name": "test", "type": "text", "key": "test", "optional": False}

TEXT_SEARCH_RULE_1 = {**TEXT_RULE_BASE, **{"value": "hello world", "text_type": "search"}}
TEXT_SEARCH_RULE_2 = {**TEXT_RULE_BASE, **{"value": "odd ch\faract\ters", "text_type": "search"}}
TEXT_SEARCH_RULE_3 = {**TEXT_RULE_BASE, **{"value": "    what whitespace?", "text_type": "search"}}
TEXT_SEARCH_RULE_4 = {**TEXT_RULE_BASE, **{"value": 753930843, "text_type": "search"}}

TEXT_URL_RULE_1 = {**TEXT_RULE_BASE, **{"value": "http://yabber.io", "text_type": "url"}}
TEXT_URL_RULE_2 = {**TEXT_RULE_BASE, **{"value": "hello world", "text_type": "url"}}
TEXT_URL_RULE_3 = {**TEXT_RULE_BASE, **{"value": "postgres://readonly:changeme@127.0.0.1:5432/postgres", "text_type": "url"}}
TEXT_URL_RULE_4 = {**TEXT_RULE_BASE, **{"value": [1, 4, 5], "text_type": "url"}}
