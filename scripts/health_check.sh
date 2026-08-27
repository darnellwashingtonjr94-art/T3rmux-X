#!/data/data/com.termux/files/usr/bin/bash
# Pre-flight environment check to verify essential CLI tools

echo "[+] Running T3rmux-x system health check..."

check_tool() {
    if command -v "$1" >/dev/null 2>&1; then
        echo "  [✓] $1 is installed"
    else
        echo "  [✗] $1 is MISSING"
    fi
}

check_tool "termux-speech-to-text"
check_tool "termux-tts-speak"
check_tool "python"
check_tool "node"
check_tool "claude"
check_tool "git"

echo "[+] System check complete."
