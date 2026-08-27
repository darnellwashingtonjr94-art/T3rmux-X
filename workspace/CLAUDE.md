# Context & Guidelines for Claude Code in T3rmux-x

## Project Rules
- **Environment:** Android/Termux environment constraints apply (ARM64 linux environment).
- **Architecture:** Keep python/JS scripts lean and modular.
- **Commands:** Prefer native POSIX standard bash commands.

## Code Style & Formatting
- Use explicit error handling on all filesystem operations.
- Prefer Python 3.10+ syntax for python tools.
- Auto-generate minimal documentation for newly generated files.
