# 🚀 Ultimate AI Dev Environment

## 🏗️ Architecture Overview

### 🖥️ **magoo** (Remote Workstation)
- **Role**: IDE Frontend
- **Tool**: Cursor AI
- **Connection**: SSH to neurX
- **Purpose**: Code editing, file navigation, integrated terminal

### 🧠 **neurX** (AI Server) 
- **Role**: Execution & AI Tools Backend
- **Tools**: 
  - Claude Code CLI
  - Gemini CLI
  - Python/Conda environments
- **Purpose**: Run all AI tools, execute code, manage projects

## 🔧 Complete Setup

### 1. Cursor AI on magoo
```bash
# Install Cursor AI
# Configure SSH Remote Extension
# Connect to neurX via SSH
```

### 2. Claude Code CLI on neurX
```bash
# Install globally
npm install -g @anthropic-ai/claude-code

# Verify installation
claude --version
```

### 3. Gemini CLI on neurX
```bash
# Download from GitHub releases
wget https://github.com/google/generative-ai-go/releases/latest/download/gemini-linux-amd64
chmod +x gemini-linux-amd64
sudo mv gemini-linux-amd64 /usr/local/bin/gemini

# Configure API key
export GEMINI_API_KEY="your-key-here"
```

### 4. Environment Setup
```bash
# Navigate to ai_dev
cd ~/dev/ai_dev

# Run setup script
./dev_setup.sh

# Reload shell
source ~/.bashrc
```

## 💻 Daily Workflow

### 1. Start Your Session
1. Open Cursor AI on magoo
2. Connect to neurX via SSH Remote
3. Open terminal in Cursor
4. Navigate to your project: `cd ~/dev/ai_dev`

### 2. Choose Your Mode

#### 🤖 Single AI Mode
```bash
# For Claude-focused work
./dev-launch.sh

# For Gemini-focused work  
gemini repl
```

#### 🎭 Dual AI Mode
```bash
# Split screen: Claude (left) + Gemini (right)
dualrepl
```

### 3. Use Your Tools

#### Claude Code CLI (Precision Tasks)
```bash
# Edit files with AI assistance
ccedit main.py

# Summarize codebase
ccsum src/

# Fix linting/type errors
ccfix .

# Interactive REPL
claude repl
```

#### Gemini CLI (Exploratory/Agentic Tasks)
```bash
# Quick prompts
gy "Create a FastAPI endpoint for user auth"

# Interactive chat
gc

# Web research
gf "https://docs.python.org/3/library/asyncio.html"

# Start agentic mode with MCP
gm
```

## 🎯 Use Case Examples

### Example 1: Building a New Feature
```bash
# 1. Research approach with Gemini
gy "Best practices for implementing JWT auth in FastAPI"

# 2. Generate initial code with Claude
ccedit src/auth.py

# 3. Refine and test
ccfix src/auth.py
pytest tests/test_auth.py
```

### Example 2: Debugging Complex Issue
```bash
# 1. Start dual mode
dualrepl

# 2. In Claude pane: Analyze the error
claude> analyze the traceback in logs/error.log

# 3. In Gemini pane: Research solutions
gemini> search for similar AsyncIO timeout errors

# 4. Apply fix with Claude
ccedit src/async_handler.py
```

### Example 3: Code Review & Refactoring
```bash
# 1. Get overview
ccsum src/

# 2. Identify improvements with Gemini
gc
> Review src/database.py for performance issues

# 3. Implement refactoring with Claude
ccedit src/database.py
```

## 🛠️ Advanced Features

### Custom Aliases (in .bash_aliases)
```bash
# Project navigation
alias aidev="cd ~/dev/ai_dev && conda activate ai-dev"

# Quick test runners
alias pytest="python -m pytest -xvs"
alias typecheck="mypy src/"

# Git helpers
alias gs="git status"
alias gd="git diff"
```

### Tmux Commands (in dual mode)
- `Ctrl+b %` - Split vertically
- `Ctrl+b "` - Split horizontally  
- `Ctrl+b ←/→` - Navigate panes
- `Ctrl+b z` - Zoom current pane
- `Ctrl+b d` - Detach session

### MCP (Model Context Protocol)
```bash
# Start Gemini with MCP server
gm

# Available MCP tools:
# - filesystem operations
# - web browsing
# - code execution
# - memory/retrieval
```

## 📁 Project Structure
```
~/dev/ai_dev/
├── CLAUDE.md          # Context for Claude
├── README.md          # Project docs
├── ULTIMATE_DEV_SETUP.md  # This guide
├── .bash_aliases      # All shortcuts
├── dev-launch.sh      # Claude launcher
├── dev_setup.sh       # Setup installer
└── [your code]        # Projects
```

## 🔄 Replicating for New Projects

```bash
# 1. Create new project
mkdir ~/dev/new-agent
cd ~/dev/new-agent

# 2. Copy setup script
cp ~/dev/ai_dev/dev_setup.sh .

# 3. Run setup
./dev_setup.sh

# 4. Start developing!
./dev-launch.sh
```

## 💡 Pro Tips

1. **Use Claude for**:
   - Precise code edits
   - Refactoring
   - Bug fixes
   - Code reviews

2. **Use Gemini for**:
   - Research & exploration
   - Architecture decisions
   - Web lookups
   - Agentic workflows

3. **Use Both Together for**:
   - Complex debugging
   - Full-stack features
   - Learning new frameworks
   - System design

## 🚨 Troubleshooting

### Claude not working?
```bash
# Check installation
which claude
claude --version

# Reinstall if needed
npm install -g @anthropic-ai/claude-code
```

### Gemini not working?
```bash
# Check API key
echo $GEMINI_API_KEY

# Check binary
which gemini
gemini --version
```

### Aliases not loading?
```bash
# Reload bashrc
source ~/.bashrc

# Check alias file
cat ~/.bash_aliases
```

---

**Remember**: This setup gives you the best of both AI assistants - Claude's precision and Gemini's exploration capabilities, all within your familiar Cursor IDE environment!