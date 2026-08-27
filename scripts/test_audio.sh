#!/data/data/com.termux/files/usr/bin/bash
# Diagnostic audio capture and TTS verification script

source "$(dirname "$0")/../config/env.sh"

echo "[+] Testing Text-to-Speech (TTS)..."
termux-tts-speak "T3rmux-x audio system diagnostic check initialising."

echo "[+] Testing Speech-to-Text (STT)... Speak into your phone microphone now."
STT_OUTPUT=$(termux-speech-to-text)

if [ -z "$STT_OUTPUT" ]; then
    echo "[-] Error: No speech input detected or Termux-API permission denied."
    termux-tts-speak "Audio capture failed."
    exit 1
else
    echo "[+] Speech captured successfully:"
    echo "    \"$STT_OUTPUT\""
    termux-tts-speak "Speech successfully captured."
fi
