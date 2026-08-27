#!/usr/bin/env python3
import os
import sys
import json
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../workspace')))
from metrics import log_usage, METRICS_FILE

def test_log_usage_creates_file():
    if METRICS_FILE.exists():
        METRICS_FILE.unlink()
        
    log_usage("gemini-2.5-pro", 150, 300)
    
    assert METRICS_FILE.exists()
    data = json.loads(METRICS_FILE.read_text())
    assert len(data["runs"]) == 1
    assert data["runs"][0]["input"] == 150
