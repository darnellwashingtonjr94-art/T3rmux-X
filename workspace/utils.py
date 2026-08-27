#!/usr/bin/env python3
"""
File and Text Parsing Utilities for T3rmux-x Workspace
"""

import re
from pathlib import Path

def sanitize_input(text: str) -> str:
    """Removes shell unsafe characters from speech string."""
    return re.sub(r'[^a-zA-Z0-9\s\.,_-\?!]', '', text).strip()

def ensure_directory(path_str: str):
    """Ensures nested path structure exists."""
    Path(path_str).mkdir(parents=True, exist_ok=True)

def read_file_safely(file_path: str) -> str:
    """Safely reads content from workspace files."""
    path = Path(file_path)
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")
