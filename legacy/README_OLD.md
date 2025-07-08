# 🚀 AI Development Environment

A streamlined AI development toolkit with environment testing, GPU performance benchmarking, and project creation.

## 📁 Structure

```
ai_dev/
├── README.md                    # This file
├── environment.yaml             # Conda environment definition
├── ai_dev.sh                    # Command-line launcher
├── ai_dev_menu.py               # Interactive menu system
├── run_system_test.sh           # Quick system health check
├── run_system_test_quick.sh     # Essential checks only
├── create_ai_project.py         # AI project creation tool
├── tests/
│   ├── system_stress_test.py    # Complete system stress test
│   └── comprehensive_system_test.py  # Detailed health check
└── projects/                    # Created projects go here
```

## 🚀 Quick Start

### Option 1: Interactive Menu (Recommended)
```bash
cd /home/rich/dev/ai_dev
conda activate ai_dev
python ai_dev_menu.py
```

### Option 2: Command Line
```bash
cd /home/rich/dev/ai_dev
./ai_dev.sh test                    # Quick health check
./ai_dev.sh stress                  # Full stress test
./ai_dev.sh create my_project 1     # Create RAG project
```

### Option 3: Direct Commands
```bash
cd /home/rich/dev/ai_dev
./run_system_test_quick.sh          # Quick health check
conda run -n ai_dev python tests/system_stress_test.py  # Full stress test
python create_ai_project.py --name "my_project" --type 1  # Create project
```

## 🎯 Components

### **Interactive Menu** (`ai_dev_menu.py`)
- **User-friendly interface** with rich formatting
- **6 main functions**: Health check, stress test, project creation, project list, system info, help
- **Easy navigation** with numbered options
- **Real-time feedback** with progress indicators

### **Command Line Launcher** (`ai_dev.sh`)
- **Quick access** to main functions
- **Simple syntax**: `./ai_dev.sh [command]`
- **Project creation** with type selection
- **Built-in help** and error handling

### **System Testing**
- **Quick Test**: `run_system_test_quick.sh` - Essential checks (~10s)
- **Full Test**: `run_system_test.sh` - Comprehensive health check
- **Stress Test**: `tests/system_stress_test.py` - GPU/CPU/RAM stress testing

### **Project Creation**
- **`create_ai_project.py`** - Creates complete AI projects with:
  - 7 project types (RAG, Multi-Agent, Neural Net, etc.)
  - Automatic conda environment setup
  - Project structure and templates
  - Dependencies and configuration

### **Environment**
- **`environment.yaml`** - Conda environment with PyTorch, CUDA, AI libraries

## 🔧 Available Project Types

1. **RAG System** - Document Q&A with retrieval
2. **Multi-Agent** - Collaborative AI agents
3. **Document Processor** - Bulk document analysis
4. **Semantic Search** - Vector-based search engine
5. **Custom Neural Net** - GPU-accelerated ML
6. **API Service** - AI-powered web API
7. **Data Pipeline** - ETL with AI processing

## 📊 System Requirements

- **GPU**: NVIDIA GPU with CUDA support
- **RAM**: 16GB+ recommended
- **Storage**: 10GB+ free space
- **OS**: Linux (tested on Ubuntu)

## 🚀 Usage Examples

### Interactive Menu
```bash
python ai_dev_menu.py
# Then select options 1-6 from the menu
```

### Quick Health Check
```bash
./ai_dev.sh test
# OR
./run_system_test_quick.sh
```

### Create RAG Project
```bash
./ai_dev.sh create document_chat 1
# OR
python create_ai_project.py --name "document_chat" --type 1
cd ../projects/document_chat
conda env create -f environment.yaml
conda activate document_chat
python src/main.py
```

### Full System Stress Test
```bash
./ai_dev.sh stress
# OR
conda run -n ai_dev python tests/system_stress_test.py
```

## ✅ Success Indicators

- ✅ GPU detected and working
- ✅ CUDA available in PyTorch
- ✅ Ollama service running
- ✅ AI libraries import successfully
- ✅ Project creation works
- ✅ Environment setup completes

## 🆘 Troubleshooting

**CUDA not available**: Check `nvidia-smi` and PyTorch installation
**Ollama connection failed**: Run `systemctl status ollama`
**Environment creation fails**: Try `conda clean --all` then retry
**Menu not responding**: Use Ctrl+C to exit, then try command line options

## 🎯 Menu Options

1. **System Health** - Quick health check (~10s)
2. **Stress Test** - Full GPU/CPU stress test (2-5 min)
3. **Create Project** - New AI project with environment
4. **Project List** - Show existing projects
5. **System Info** - Display system specifications
6. **Help** - Show detailed help
0. **Exit** - Exit the menu

---

**Last Updated**: 2024 - Streamlined for essential AI development workflow 