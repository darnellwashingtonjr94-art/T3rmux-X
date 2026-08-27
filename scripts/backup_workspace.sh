#!/data/data/com.termux/files/usr/bin/bash
# Creates a timestamped tar archive of the current workspace state

source "$(dirname "$0")/../config/env.sh"

BACKUP_DIR="$PROJECT_ROOT/backups"
mkdir -p "$BACKUP_DIR"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/workspace_backup_$TIMESTAMP.tar.gz"

echo "[+] Archiving workspace..."
tar -czf "$BACKUP_FILE" -C "$PROJECT_ROOT" workspace/

if [ $? -eq 0 ]; then
    echo "[+] Backup saved to: $BACKUP_FILE"
    termux-tts-speak "Workspace successfully backed up."
else
    echo "[-] Backup failed!"
    termux-tts-speak "Error during backup."
fi
