# 🔌 MCP (Model Context Protocol) Setup Guide

## Overview
MCP enables AI assistants to interact with external systems through a standardized protocol. It provides tools for file systems, databases, APIs, and more.

## 🚀 Quick Setup

### 1. Install MCP Servers
After updating your conda environment:
```bash
conda activate ai-dev
conda env update -f environment.yaml --prune
```

### 2. Configure Claude Desktop (if using)
Add to Claude Desktop settings (`~/.config/claude/config.json`):
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "mcp-server-filesystem",
      "args": ["--root", "/home/rich/dev"]
    },
    "memory": {
      "command": "mcp-server-memory",
      "args": ["--db", "~/.mcp/memory.db"]
    }
  }
}
```

### 3. Configure for CLI Tools

#### For Claude Code CLI
Create `~/.claude/mcp_config.json`:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "mcp-server-filesystem",
      "args": ["--root", "/home/rich/dev"],
      "description": "File system access"
    },
    "git": {
      "command": "mcp-server-git",
      "description": "Git operations"
    },
    "memory": {
      "command": "mcp-server-memory",
      "args": ["--db", "~/.mcp/memory.db"],
      "description": "Persistent memory"
    }
  }
}
```

#### For Gemini CLI
Gemini CLI has built-in MCP support. Start with:
```bash
gm  # or gemini mcp start
```

## 📦 Available MCP Servers

### Core Servers (Installed)
1. **filesystem** - Read/write files, navigate directories
2. **git** - Git operations (commit, branch, diff)
3. **github** - GitHub API (issues, PRs, repos)
4. **memory** - Persistent storage across sessions
5. **sqlite** - SQLite database operations
6. **postgres** - PostgreSQL operations
7. **fetch** - Web content retrieval

### Configuration Examples

#### Filesystem Server
```json
{
  "filesystem": {
    "command": "mcp-server-filesystem",
    "args": ["--root", "/home/rich/dev", "--allow-write"]
  }
}
```

#### GitHub Server
```json
{
  "github": {
    "command": "mcp-server-github",
    "env": {
      "GITHUB_TOKEN": "ghp_your_token_here"
    }
  }
}
```

#### Memory Server
```json
{
  "memory": {
    "command": "mcp-server-memory",
    "args": ["--db", "~/.mcp/memory.db", "--max-items", "1000"]
  }
}
```

## 🔧 Integration with Your Workflow

### Using MCP with Claude Code CLI
```bash
# Start Claude with MCP
claude --mcp-config ~/.claude/mcp_config.json

# In REPL mode
claude repl
> use filesystem to read all Python files in src/
> remember this project structure for later
> use git to show recent commits
```

### Using MCP with Gemini CLI
```bash
# Start Gemini with MCP
gm

# Available commands in MCP mode:
# - File operations
# - Web fetching
# - Memory storage
# - Git operations
```

### Dual Mode with MCP
```bash
# Start both with MCP support
tmux new-session -d -s dual 'claude repl --mcp' \; split-window -h 'gemini mcp' \; attach
```

## 🎯 Use Cases

### 1. Project Analysis
```bash
# Claude with filesystem MCP
> analyze all Python files in this project and create a dependency graph
> save the analysis to memory for future reference
```

### 2. Code Generation with Context
```bash
# Gemini with memory MCP
> recall the project structure from memory
> generate a new module that fits the existing architecture
```

### 3. Git Workflow
```bash
# Claude with git MCP
> show me what changed in the last 5 commits
> create a commit message based on current staged changes
```

### 4. Documentation Generation
```bash
# Either tool with filesystem MCP
> read all source files and generate comprehensive API documentation
> update the README.md with current project structure
```

## 🔐 Security Notes

1. **Filesystem Access**: Limited to specified root directory
2. **API Tokens**: Store in environment variables
3. **Database Access**: Use connection strings carefully
4. **Memory Storage**: Local SQLite by default

## 🛠️ Custom MCP Servers

Create your own MCP server:
```python
# my_mcp_server.py
from mcp import Server, Tool

class MyCustomServer(Server):
    def __init__(self):
        super().__init__("my-custom-server")
        
    @Tool("custom_operation")
    async def custom_operation(self, param: str) -> str:
        return f"Processed: {param}"

if __name__ == "__main__":
    server = MyCustomServer()
    server.run()
```

Add to config:
```json
{
  "custom": {
    "command": "python",
    "args": ["/path/to/my_mcp_server.py"]
  }
}
```

## 📝 Best Practices

1. **Start Simple**: Begin with filesystem and memory servers
2. **Security First**: Limit access scopes appropriately
3. **Combine Tools**: Use MCP with both Claude and Gemini for different strengths
4. **Persistent Memory**: Use memory server to maintain context across sessions
5. **Version Control**: Use git server for code-aware operations

## 🚨 Troubleshooting

### MCP Server Not Starting
```bash
# Check if installed
which mcp-server-filesystem

# Test server directly
mcp-server-filesystem --root /tmp --help

# Check logs
tail -f ~/.mcp/logs/server.log
```

### Permission Issues
```bash
# Ensure MCP directory exists
mkdir -p ~/.mcp/memory
chmod 755 ~/.mcp
```

### Connection Failed
```bash
# Verify server is running
ps aux | grep mcp-server

# Check port availability
netstat -an | grep 3000
```

---

With MCP integrated, your AI assistants can now interact with your file system, databases, and external services directly!