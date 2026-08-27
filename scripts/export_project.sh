#!/data/data/com.termux/files/usr/bin/bash
# Packages a completed Claude Code build for easy sharing

PROJECT_NAME=${1:-"t3rmux_build"}
EXPORT_DIR="$PROJECT_ROOT/exports"
mkdir -p "$EXPORT_DIR"

echo "[+] Zipping workspace contents to ${PROJECT_NAME}.zip..."
cd "$WORKSPACE_DIR" || exit 1

# Exclude T3rmux-x orchestrator files, keep only generated project files
zip -r "$EXPORT_DIR/${PROJECT_NAME}.zip" . -x "*.py" "*.sh" "CLAUDE.md" "settings.json"

echo "[+] Export available at: $EXPORT_DIR/${PROJECT_NAME}.zip"
