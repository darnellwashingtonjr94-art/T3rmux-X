#!/usr/bin/env python3
"""
Claude Code CLI Wrapper
Pipes Gemini's architectural blueprint to Claude in headless mode.
"""

import os
import subprocess
from logger import log, error, success

class ClaudeRunner:
    def __init__(self, workspace_path: str):
        self.workspace = workspace_path

    def run_plan(self, plan_text: str) -> bool:
        log("Invoking Claude Code CLI execution...")
        prompt_input = f"Execute this implementation plan step-by-step:\n\n{plan_text}"
        
        cmd = ["claude", "-p", prompt_input]
        
        try:
            process = subprocess.Popen(
                cmd,
                cwd=self.workspace,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = process.communicate()
            
            if process.returncode == 0:
                success("Claude Code completed build tasks successfully.")
                return True
            else:
                error(f"Claude Code failed with code {process.returncode}:\n{stderr}")
                return False
                
        except Exception as e:
            error(f"Failed to trigger Claude subprocess: {str(e)}")
            return False
