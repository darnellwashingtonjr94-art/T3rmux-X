#!/data/data/com.termux/files/usr/bin/bash
# Standalone voice command listener with automatic retry handling

source "$(dirname "$0")/../config/env.sh"

listen_for_input() {
    termux-tts-speak "T3rmux x ready. Speak your command."
    local result=$(termux-speech-to-text 2>/dev/null)
    
    if [ -z "$result" ]; then
        echo "ERR_EMPTY"
    else
        echo "$result"
    fi
}

INPUT=$(listen_for_input)

if [ "$INPUT" == "ERR_EMPTY" ]; then
    termux-tts-speak "No speech detected. Aborting."
    exit 1
fi

echo "$INPUT"
