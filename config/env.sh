#!/data/data/com.termux/files/usr/bin/bash
# Global API Keys and Environment Variables

export GEMINI_API_KEY="your-gemini-api-key-here"
export ANTHROPIC_API_KEY="your-anthropic-api-key-here"
export GEMINI_MODEL="gemini-2.5-pro"
export CLAUDE_EXEC_CMD="claude -p"

# Directory paths
export PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export WORKSPACE_DIR="$PROJECT_ROOT/workspace"
