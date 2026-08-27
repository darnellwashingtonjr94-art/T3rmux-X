#!/usr/bin/env python3
"""
Error Remediation Loop
Parses failed Claude executions and feeds the stderr back to Gemini for fixing.
"""

import os
from gemini_client import GeminiArchitect
from claude_runner import ClaudeRunner
from audio_feedback import speak
from logger import log, error

def handle_build_failure(error_log: str, workspace_path: str):
    log("Initiating auto-remediation sequence...")
    speak("Build failed. Analyzing errors for automatic remediation.")
    
    architect = GeminiArchitect()
    remediation_prompt = f"The previous build failed with this error:\n\n{error_log}\n\nProvide a plan to fix this."
    
    log("Generating fix plan...")
    fix_plan = architect.generate_plan(remediation_prompt)
    
    log("Executing fix plan with Claude Code...")
    speak("Applying fixes.")
    
    runner = ClaudeRunner(workspace_path)
    success = runner.run_plan(fix_plan)
    
    if success:
        speak("Remediation successful.")
        log("Auto-remediation resolved the issue.")
    else:
        speak("Remediation failed. Manual intervention required.")
        error("Auto-remediation loop failed.")
