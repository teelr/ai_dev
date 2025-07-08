# CLAUDE.md - Project Context for Claude Code CLI

## Project Overview
This is a comprehensive AI Development Environment Template designed for building advanced AI agents. It integrates multiple AI tools, MCP (Model Context Protocol), and GPU support for enhanced development workflows.

## Environment Setup
- **System**: neurX (Ubuntu server) with RTX 5080 GPU support
- **Python Environment**: conda env `ai-dev` (Python 3.11)
- **Working Directory**: `/home/rich/dev/ai_dev`
- **Template Purpose**: Reusable foundation for AI agent projects (Libby, Kermit, Warren)

## Integrated Tools
1. **Claude Code CLI** (`claude`) - High-quality code generation and analysis
2. **Gemini CLI** (`gemini`) - Agentic workflows with ReAct and tool use
3. **MCP Servers** - Model Context Protocol for system integration
4. **GPU Support** - CUDA 12.1 + cuDNN for local AI acceleration
5. **tmux** - For dual REPL sessions

## Available Commands & Aliases
```bash
# Claude shortcuts
cc        # claude
ccedit    # claude edit
ccsum     # claude summarize
ccfix     # claude fix

# Gemini shortcuts  
gc        # gemini chat
gy        # gemini yolo
gm        # gemini mcp start
gf        # gemini fetch

# Dual REPL
dualrepl  # Split tmux: Claude + Gemini
```

## Development Workflow
1. Use Cursor AI on magoo (remote workstation) connected via SSH to neurX
2. Run `./dev-launch.sh` to start Claude REPL with conda environment
3. Use `dualrepl` for simultaneous Claude + Gemini sessions

## Important Files
- `environment.yaml` - Complete conda environment with GPU/MCP support
- `dev-launch.sh` - Quick launcher script
- `dev_setup.sh` - Reusable installer for new projects
- `.bash_aliases` - All CLI shortcuts
- `mcp_config.json` - MCP server configuration
- `docs/` - Complete documentation suite
- `.gitignore` - Comprehensive ignore rules

## Key Dependencies
### AI/ML Frameworks
- LangChain (complete ecosystem) + LangGraph
- LlamaIndex + Anthropic integration
- AutoGen for multi-agent systems
- PyTorch 2.0+ with CUDA support
- Sentence Transformers

### Vector Databases
- ChromaDB, Milvus (pymilvus), FAISS

### MCP Integration
- mcp + multiple server packages
- Filesystem, Git, GitHub, Memory servers
- Web fetching and database integration

### Development Tools
- FastAPI + Uvicorn for web services
- Jupyter/IPython for experimentation
- Black, Ruff, MyPy for code quality
- Pytest with async support

## Testing Commands
When code changes are made, run:
```bash
# Python linting
ruff check .

# Type checking  
mypy .

# Tests (if available)
pytest

# GPU test (if using CUDA)
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"
```

## Project Goals
- **Template Creation**: Reusable foundation for AI projects
- **Agent Development**: Build Libby, Kermit, Warren agents
- **Technology Integration**: LangChain + Milvus + AutoGen + MCP
- **Development Efficiency**: Dual AI workflows (Claude + Gemini)
- **GPU Utilization**: Local acceleration for AI workloads
- **Remote/Local Flexibility**: neurX server + local development