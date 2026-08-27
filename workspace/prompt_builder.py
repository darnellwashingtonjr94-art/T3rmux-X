#!/usr/bin/env python3
"""
Dynamically injects system context (like OS info) into the user's voice prompt.
"""

from system_info import getDeviceInfo
import yaml

def build_architect_prompt(user_voice_input: str) -> str:
    device_context = getDeviceInfo()
    
    full_prompt = (
        f"USER REQUEST: {user_voice_input}\n\n"
        f"TARGET ENVIRONMENT CONTEXT:\n"
        f"- OS: {device_context.get('platform')}\n"
        f"- Architecture: {device_context.get('arch')}\n"
        f"- Free Memory: {device_context.get('freeMemoryMB')}MB\n\n"
        f"Constraints: Generate lean, mobile-friendly code."
    )
    return full_prompt
