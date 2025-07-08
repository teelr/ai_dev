# 🚀 AI Development Environment Template

A comprehensive AI development environment integrating Claude Code CLI, Gemini CLI, MCP (Model Context Protocol), and GPU support for building advanced AI agents.

## 🎯 Features

- **Dual AI Integration**: Claude Code CLI + Gemini CLI working in harmony
- **MCP Support**: Model Context Protocol for agentic workflows
- **GPU Ready**: Full CUDA support for RTX GPUs (tested with RTX 5080)
- **Complete AI Stack**: LangChain, Milvus, AutoGen, and more
- **Remote + Local**: Work with remote servers (neurX) or local GPU
- **Developer Friendly**: Pre-configured aliases, launchers, and tools

## 📁 Project Structure

```
ai_dev/
├── README.md                # This file
├── CLAUDE.md               # Context for Claude Code CLI
├── environment.yaml        # Conda environment with all dependencies
├── .bash_aliases          # CLI shortcuts and aliases
├── dev-launch.sh          # Quick launcher for Claude REPL
├── dev_setup.sh           # Reusable setup installer
├── mcp_config.json        # MCP server configuration
│
├── docs/
│   ├── ULTIMATE_DEV_SETUP.md   # Complete setup guide
│   ├── WORKFLOW_VISUAL.md      # Visual workflow diagrams
│   ├── MCP_SETUP.md           # MCP configuration guide
│   ├── GPU_SETUP.md           # GPU/CUDA setup guide
│   └── UPDATE_ENVIRONMENT.md   # Environment update instructions
│
└── legacy/
    └── README_OLD.md      # Original project documentation
```

## 🚀 Quick Start

### Prerequisites
- Conda/Miniconda installed
- Node.js 18+ (for Claude Code CLI)
- (Optional) NVIDIA GPU with CUDA support

### Installation

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/ai_dev.git
cd ai_dev
```

2. **Create conda environment**
```bash
conda env create -f environment.yaml
conda activate ai-dev
```

3. **Install CLI tools**
```bash
# Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Gemini CLI (download latest release)
wget https://github.com/google/generative-ai-go/releases/latest/download/gemini-linux-amd64
chmod +x gemini-linux-amd64
sudo mv gemini-linux-amd64 /usr/local/bin/gemini
```

4. **Run setup script**
```bash
./dev_setup.sh
source ~/.bashrc
```

## 💻 Usage

### Single AI Mode
```bash
# Start Claude REPL
./dev-launch.sh

# Or start Gemini
gemini repl
```

### Dual AI Mode
```bash
# Split screen with both AIs
dualrepl
```

### Available Commands
```bash
# Claude shortcuts
cc         # Launch Claude
ccedit     # Edit files with AI
ccsum      # Summarize code
ccfix      # Fix issues

# Gemini shortcuts
gc         # Chat mode
gy         # YOLO mode
gm         # MCP agentic mode
gf         # Fetch web content
```

## 🔧 Configuration

### API Keys
Create a `.env` file:
```bash
ANTHROPIC_API_KEY=your-claude-key
GOOGLE_API_KEY=your-gemini-key
OPENAI_API_KEY=your-openai-key  # Optional
GITHUB_TOKEN=your-github-token   # For MCP GitHub server
```

### MCP Configuration
Edit `mcp_config.json` to customize MCP servers. Default includes:
- Filesystem access
- Git operations
- Memory persistence
- Web fetching

## 📦 Included Packages

### AI/ML Frameworks
- LangChain (complete ecosystem)
- LlamaIndex
- AutoGen (multi-agent)
- Sentence Transformers
- PyTorch with GPU support

### Vector Databases
- ChromaDB
- Milvus (pymilvus)
- FAISS

### Development Tools
- FastAPI + Uvicorn
- Jupyter/IPython
- Black, Ruff, MyPy
- Pytest with async support

### GPU/CUDA Support
- CUDA Toolkit 12.1
- cuDNN 8.9
- GPU monitoring tools

## 🎯 Use Cases

This environment is perfect for:
- Building AI agents (chatbots, assistants)
- RAG (Retrieval-Augmented Generation) systems
- Multi-agent orchestration with AutoGen
- LLM application development
- Vector database experiments
- GPU-accelerated ML workflows

## 📚 Documentation

- [Complete Setup Guide](docs/ULTIMATE_DEV_SETUP.md)
- [Visual Workflows](docs/WORKFLOW_VISUAL.md)
- [MCP Configuration](docs/MCP_SETUP.md)
- [GPU Setup](docs/GPU_SETUP.md)

## 🔄 Reusing This Template

To use this template for a new project:

```bash
# Copy template to new project
cp -r ~/dev/ai_dev ~/dev/my-new-agent

# Navigate to new project
cd ~/dev/my-new-agent

# Run setup
./dev_setup.sh

# Start developing!
./dev-launch.sh
```

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

MIT License - feel free to use this template for your projects.

## 🙏 Acknowledgments

- Built for use with Cursor AI IDE
- Powered by Claude (Anthropic) and Gemini (Google)
- Optimized for neurX server integration

---

*Happy AI Development! 🤖*