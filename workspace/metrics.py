#!/usr/bin/env python3
"""
Tracks Gemini and Claude token usage to help manage API costs.
"""

import json
from pathlib import Path

METRICS_FILE = Path(__file__).parent.parent / "logs" / "usage_metrics.json"

def log_usage(model: str, input_tokens: int, output_tokens: int):
    METRICS_FILE.parent.mkdir(exist_ok=True)
    
    if not METRICS_FILE.exists():
        METRICS_FILE.write_text(json.dumps({"total_cost": 0.0, "runs": []}))
        
    data = json.loads(METRICS_FILE.read_text())
    
    data["runs"].append({
        "model": model,
        "input": input_tokens,
        "output": output_tokens
    })
    
    METRICS_FILE.write_text(json.dumps(data, indent=2))

if __name__ == "__main__":
    print("Metrics tracker initialized.")
