#!/data/data/com.termux/files/usr/bin/bash
# Convenient bash aliases for Termux users to trigger orchestrator commands

# Add this to your ~/.bashrc or ~/.zshrc in Termux:
# source /path/to/T3rmux-x/config/aliases.sh

alias tx-listen="python $PROJECT_ROOT/workspace/termux_bot.py"
alias tx-clean="bash $PROJECT_ROOT/scripts/clean_workspace.sh"
alias tx-status="bash $PROJECT_ROOT/scripts/health_check.sh"
alias tx-backup="bash $PROJECT_ROOT/scripts/backup_workspace.sh"
alias tx-update="bash $PROJECT_ROOT/scripts/update_t3rmux.sh"

echo "[+] T3rmux-x shortcuts loaded. Type 'tx-listen' to start."
