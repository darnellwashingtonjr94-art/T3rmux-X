#!/usr/bin/env python3
"""
T3rmux-x Orchestrator Main Script
Captures voice input -> Gemini 2.5 Pro reasoning -> Claude Code execution
"""

import os
import subprocess
import sys
from google import genai
from google.genai import types

def speak(text: str):
    subprocess.run(["termux-tts-speak", text])

def capture_voice() -> str:
    speak("Listening for your build prompt...")
    result = subprocess.run(["termux-speech-to-text"], capture_output=True, text=True)
    prompt = result.stdout.strip()
    if not prompt:
        speak("I couldn't hear any prompt. Exiting.")
        sys.exit(1)
    return prompt

def generate_architectural_plan(prompt: str) -> str:
    speak("Analyzing request with Gemini 2 point 5 Pro...")
    client = genai.Client()
    
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-pro"),
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are a lead software architect. Convert the user prompt into a precise execution plan for Claude Code.",
            thinking_config=types.ThinkingConfig(thinking_budget=2048)
        )
    )
    return response.text

def execute_claude_build(plan: str):
    speak("Executing project build with Claude Code.")
    workspace_dir = os.path.join(os.path.dirname(__file__))
    cmd = ["claude", "-p", f"Execute this plan:\n{plan}"]
    
    subprocess.run(cmd, cwd=workspace_dir)
    speak("Build complete.")

def main():
    user_prompt = capture_voice()
    print(f"[+] Spoken Prompt: {user_prompt}")
    
    plan = generate_architectural_plan(user_prompt)
    print(f"\n[+] Architectural Blueprint:\n{plan}\n")
    
    execute_claude_build(plan)

if __name__ == "__main__":
    main()
