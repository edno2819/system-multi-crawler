import json
from pathlib import Path
import re


def format_folder_name(name: str):
    not_allowed_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in not_allowed_chars:
        name = name.replace(char, '')
    name = name.strip()
    name = re.sub(' +', ' ', name)
    name = name.replace(' ', '_')
    name = name.lower()
    return name

