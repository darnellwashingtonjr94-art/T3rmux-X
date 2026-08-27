#!/usr/bin/env python3
"""
Text-to-Speech Helper
Provides auditory status cues using Termux native API.
"""

import subprocess
import shutil

def speak(message: str):
    """Spoken notification wrapper using termux-tts-speak."""
    if shutil.which("termux-tts-speak"):
        subprocess.run(["termux-tts-speak", message], stderr=subprocess.DEVNULL)
    else:
        print(f"[TTS Fallback]: {message}")

if __name__ == "__main__":
    speak("Audio feedback system functional.")
