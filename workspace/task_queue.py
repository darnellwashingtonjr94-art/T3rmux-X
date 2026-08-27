#!/usr/bin/env python3
"""
Task Queue Manager
Allows stacking multiple voice commands into a backlog if a build is currently running.
"""

import json
from pathlib import Path
from logger import log

QUEUE_FILE = Path(__file__).parent / "build_queue.json"

def init_queue():
    if not QUEUE_FILE.exists():
        QUEUE_FILE.write_text("[]", encoding="utf-8")

def add_task(prompt: str):
    init_queue()
    tasks = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    tasks.append({"prompt": prompt, "status": "pending"})
    QUEUE_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
    log(f"Added task to queue. Queue depth: {len(tasks)}")

def get_next_task() -> str:
    init_queue()
    tasks = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    pending = [t for t in tasks if t["status"] == "pending"]
    
    if pending:
        next_task = pending[0]
        # Mark as processing
        for t in tasks:
            if t == next_task:
                t["status"] = "processing"
        QUEUE_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
        return next_task["prompt"]
    return None

def clear_completed():
    init_queue()
    tasks = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    incomplete = [t for t in tasks if t["status"] != "completed"]
    QUEUE_FILE.write_text(json.dumps(incomplete, indent=2), encoding="utf-8")
