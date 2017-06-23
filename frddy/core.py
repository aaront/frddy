# -*- coding: utf-8 -*-

"""
frddy.core
~~~~~~~~~~
Handles the core functionality and classes
"""

import enum
import json

import requests


class Type(enum.Enum):
    """The type of JSON result"""
    UNKNOWN = -1
    STRING_LIKE = 1
    DICT_LIKE = 2


class Results:
    def __init__(self, raw_json):
        self.raw_json = raw_json

    @property
    def type(self) -> Type:
        if isinstance(self.raw_json, str):
            return Type.STRING_LIKE
        if isinstance(self.raw_json, dict):
            return Type.DICT_LIKE
        return Type.UNKNOWN


def analyze_url(url: str) -> Results:
    page = requests.get(url)
    j = page.json()
    return Results(j)

def analyze_file(file: str) -> Results:
    with open(file, 'r', encoding='utf-8') as f:
        j = json.loads(f)
    return Results(j)
