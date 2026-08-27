#!/data/data/com.termux/files/usr/bin/bash
# Self-updater for the T3rmux-x orchestrator

echo "[+] Checking for T3rmux-x updates..."
cd "$(dirname "$0")/.." || exit 1

# Stash any local config changes temporarily
git stash push -m "Pre-update stash" config/env.sh >/dev/null 2>&1

git pull origin main

# Pop stashed configs if they exist
git stash pop >/dev/null 2>&1

echo "[+] Re-installing dependencies in case of updates..."
source venv/bin/activate 2>/dev/null || echo "[-] No venv found. Skipping pip install."
pip install -r workspace/requirements.txt
npm install

termux-tts-speak "T3rmux x update complete."
echo "[+] Update finished successfully."
