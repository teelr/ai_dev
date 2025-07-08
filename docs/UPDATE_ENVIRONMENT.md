# Environment Update Guide

## 📦 Updated environment.yaml

The environment.yaml has been updated to include all necessary packages for your AI development setup:

### What's New:
- **Python 3.11** (upgraded from 3.10)
- **LangChain ecosystem** - Complete suite including experimental and langgraph
- **Milvus support** - pymilvus for vector database
- **AutoGen** - pyautogen for multi-agent systems
- **Google Gemini** - google-generativeai package
- **Anthropic** - anthropic package for Claude API
- **Development tools** - black, mypy, ruff, pylint
- **Testing suite** - pytest with async and coverage support

## 🔄 To Update Your Environment:

### Option 1: Update Existing Environment
```bash
# Activate environment
conda activate ai-dev

# Update with new packages
conda env update -f environment.yaml --prune
```

### Option 2: Recreate Environment (Recommended)
```bash
# Deactivate if active
conda deactivate

# Remove old environment
conda env remove -n ai-dev

# Create fresh environment
conda env create -f environment.yaml

# Activate
conda activate ai-dev
```

## ✅ Verify Installation
```bash
# Check key packages
python -c "import langchain; print(f'LangChain: {langchain.__version__}')"
python -c "import anthropic; print('Anthropic: OK')"
python -c "import google.generativeai; print('Gemini: OK')"
python -c "import autogen; print('AutoGen: OK')"
python -c "import pymilvus; print('Milvus: OK')"
```

## 🔑 API Keys Setup
Create a `.env` file in your project:
```bash
# AI APIs
ANTHROPIC_API_KEY=your-claude-key
GOOGLE_API_KEY=your-gemini-key
OPENAI_API_KEY=your-openai-key

# Vector DB (if using cloud)
MILVUS_HOST=localhost
MILVUS_PORT=19530
```

## 📝 Notes
- The environment now includes ALL packages needed for Libby, Kermit, and Warren agents
- Compatible with both Claude Code CLI and Gemini CLI
- Includes development tools for linting and type checking
- Ready for production deployment with FastAPI/Uvicorn