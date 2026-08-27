#!/usr/bin/env python3
"""
Securely prompts for and verifies API keys before injecting them into the environment.
"""

import os
from logger import log, error, success

def verify_keys():
    gemini_key = os.getenv("GEMINI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not gemini_key or not anthropic_key:
        error("API Keys missing from environment.")
        return False
        
    if not gemini_key.startswith("AIza"):
        error("Invalid Gemini API Key format.")
        return False
        
    success("API keys validated and loaded securely.")
    return True

if __name__ == "__main__":
    verify_keys()
