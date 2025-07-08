#!/bin/bash
# AI Dev Environment Setup Script
# Reusable installer for Claude Code + Gemini CLI integration

set -e

PROJECT_DIR=$(pwd)
ALIASES_FILE=".bash_aliases"
LAUNCH_SCRIPT="dev-launch.sh"

echo "🤖 Setting up AI Dev Environment in: $PROJECT_DIR"

# Create .bash_aliases
cat << 'EOF' > "$ALIASES_FILE"
# Claude Code CLI
alias cc="claude"
alias ccedit="claude edit"
alias ccsum="claude summarize"
alias ccfix="claude fix"

# Gemini CLI
alias gc="gemini chat"
alias gy="gemini yolo"
alias gm="gemini mcp start"
alias gf="gemini fetch"

# Dual REPL using tmux
alias dualrepl="tmux new-session -d -s dual 'claude repl' \; split-window -h 'gemini repl' \; attach"
EOF

echo "✅ Created $ALIASES_FILE"

# Create dev-launch.sh
cat << EOF > "$LAUNCH_SCRIPT"
#!/bin/bash
cd $PROJECT_DIR || exit
conda activate ai-dev
claude repl
EOF

chmod +x "$LAUNCH_SCRIPT"
echo "✅ Created $LAUNCH_SCRIPT"

# Check if aliases are already sourced in bashrc
if ! grep -q "source $PROJECT_DIR/$ALIASES_FILE" ~/.bashrc; then
    echo "source $PROJECT_DIR/$ALIASES_FILE" >> ~/.bashrc
    echo "✅ Added aliases to ~/.bashrc"
else
    echo "ℹ️  Aliases already in ~/.bashrc"
fi

# Create README for the project
cat << 'EOF' > README_AI_SETUP.md
# AI Dev Environment

This project is configured with Claude Code CLI and Gemini CLI integration.

## Quick Start

```bash
# Activate environment and start Claude REPL
./dev-launch.sh

# Or use dual REPL mode (Claude + Gemini)
dualrepl
```

## Available Aliases

### Claude Code
- `cc` - claude
- `ccedit` - claude edit
- `ccsum` - claude summarize  
- `ccfix` - claude fix

### Gemini CLI
- `gc` - gemini chat
- `gy` - gemini yolo
- `gm` - gemini mcp start
- `gf` - gemini fetch

## Required Tools
- Claude Code CLI: `npm install -g @anthropic-ai/claude-code`
- Gemini CLI: Install from GitHub releases
- tmux (for dual REPL mode)
- conda (with ai-dev environment)
EOF

echo "✅ Created README_AI_SETUP.md"

echo ""
echo "🎉 Setup complete! To use:"
echo "   source ~/.bashrc"
echo "   ./dev-launch.sh"
echo ""
echo "Or copy this script to new projects and run it there!"