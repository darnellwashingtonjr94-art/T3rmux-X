#!/usr/bin/env python3
"""
Gemini API Interface Module for T3rmux-x
Handles architectural planning queries with thinking configuration.
"""

import os
import sys
from google import genai
from google.genai import types
from logger import log, error

class GeminiArchitect:
    def __init__(self, model_name: str = "gemini-2.5-pro"):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            error("GEMINI_API_KEY environment variable not set.")
            sys.exit(1)
        self.client = genai.Client(api_key=self.api_key)
        self.model = model_name

    def generate_plan(self, prompt: str) -> str:
        log(f"Sending prompt to Gemini ({self.model})...")
        system_instruction = (
            "You are a principal software architect. Given a user feature request, "
            "output a modular execution plan optimized for Claude Code CLI. "
            "List specific commands, files to create, and code modifications."
        )
        
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                thinking_config=types.ThinkingConfig(thinking_budget=2048)
            )
        )
        return response.text
