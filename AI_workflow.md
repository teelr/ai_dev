# 🚀 AI Development System - Complete Workflow Guide

## System Overview

Your AI development system provides a complete, GPU-accelerated local AI environment optimized for rapid prototyping and production deployment. The system centers around the `create_ai_project.py` tool that scaffolds production-ready AI projects.

### Core Infrastructure
- **Hardware**: NVIDIA RTX 5080 (16GB VRAM) with CUDA 12.8
- **AI Engine**: Ollama with llama3.2:3b and nomic-embed-text models
- **Frontend**: Open WebUI on port 8080
- **Network**: Tailscale VPN (100.82.174.94) for secure remote access
- **Development**: 9 specialized conda environments

---

## 📋 Complete Walkthrough: Creating "next_ai_project"

### Step 1: Navigate to AI Development Directory

```bash
cd /home/rich/dev/ai_dev
```

### Step 2: Activate the AI Development Environment

```bash
conda activate ai_dev
```

**Expected Output:**
```
(ai_dev) rich@neurX:/home/rich/dev/ai_dev$
```

### Step 3: Create Your New Project

**Option A: Interactive Mode (Recommended for First Time)**
```bash
python create_ai_project.py
```

You'll see a menu like this:
```
🤖 Available AI Project Types
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Type                ┃ Description                                ┃ Use Cases                                                                                                                                                              ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1. RAG System       │ Document Q&A with retrieval                │ Chat with PDFs, knowledge base                                                                                                                                         │
│ 2. Multi-Agent      │ Collaborative AI agents                    │ Research teams, workflow automation                                                                                                                                    │
│ 3. Document Proc... │ Bulk document analysis                     │ Content extraction, summarization                                                                                                                                      │
│ 4. Semantic Search  │ Vector-based search engine                 │ Similar document finding                                                                                                                                               │
│ 5. Custom Neural... │ GPU-accelerated ML                         │ Training custom models                                                                                                                                                 │
│ 6. API Service      │ AI-powered web API                         │ Production AI services                                                                                                                                                 │
│ 7. Data Pipeline    │ ETL with AI processing                     │ Data transformation workflows                                                                                                                                          │
└─────────────────────┴────────────────────────────────────────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

Enter project name: next_ai_project
Choose project type (1-7): 1
```

**Option B: Command Line Mode (Faster)**
```bash
python create_ai_project.py --name "next_ai_project" --type 1
```

### Step 4: Verify Project Creation

**Expected Success Message:**
```
🚀 Creating RAG System: next_ai_project
✅ Git repository initialized
╭──────────────────────────────── 🎉 Success! ─────────────────────────────────╮
│ ✅ Project 'next_ai_project' created successfully!                           │
│                                                                              │
│ 📁 Location: /home/rich/dev/projects/next_ai_project                         │
│ 🎯 Type: RAG System                                                          │
│                                                                              │
│ Next steps:                                                                  │
│ 1. cd /home/rich/dev/projects/next_ai_project                                │
│ 2. conda env create -f environment.yaml                                      │
│ 3. conda activate next_ai_project                                            │
│ 4. python src/main.py                                                        │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### Step 5: Navigate to Your New Project

```bash
cd /home/rich/dev/projects/next_ai_project
```

**Verify the project structure:**
```bash
ls -la
```

**Expected Output:**
```
drwxr-xr-x  10 rich rich  4096 Jun 22 14:30 .
drwxr-xr-x   3 rich rich  4096 Jun 22 14:30 ..
drwxr-xr-x   8 rich rich  4096 Jun 22 14:30 .git
-rw-r--r--   1 rich rich   147 Jun 22 14:30 .env
-rw-r--r--   1 rich rich  1844 Jun 22 14:30 .gitignore
-rw-r--r--   1 rich rich  1156 Jun 22 14:30 README.md
drwxr-xr-x   2 rich rich  4096 Jun 22 14:30 config
drwxr-xr-x   4 rich rich  4096 Jun 22 14:30 data
drwxr-xr-x   2 rich rich  4096 Jun 22 14:30 docs
-rw-r--r--   1 rich rich  1367 Jun 22 14:30 environment.yaml
drwxr-xr-x   2 rich rich  4096 Jun 22 14:30 models
drwxr-xr-x   2 rich rich  4096 Jun 22 14:30 notebooks
drwxr-xr-x   2 rich rich  4096 Jun 22 14:30 output
drwxr-xr-x   2 rich rich  4096 Jun 22 14:30 scripts
drwxr-xr-x   2 rich rich  4096 Jun 22 14:30 src
drwxr-xr-x   2 rich rich  4096 Jun 22 14:30 tests
```

### Step 6: Create the Conda Environment

```bash
conda env create -f environment.yaml
```

**Expected Output (this takes 2-5 minutes):**
```
Collecting package metadata (repodata.json): done
Solving environment: done

Downloading and Extracting Packages:

pytorch-2.3.0        | 776.4 MB  | ████████████████████ | 100% 
pytorch-cuda-12.1    | 1.7 MB    | ████████████████████ | 100% 
...

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate next_ai_project
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

### Step 7: Activate Your Project Environment

```bash
conda activate next_ai_project
```

**Expected Output:**
```
(next_ai_project) rich@neurX:/home/rich/dev/projects/next_ai_project$
```

### Step 8: Verify GPU Access

```bash
python -c "import torch; print(f'CUDA Available: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"None\"}')"
```

**Expected Output:**
```
CUDA Available: True
GPU: NVIDIA GeForce RTX 5080
```

### Step 9: Test Ollama Connection

```bash
python -c "import ollama; print('Models:', [m['name'] for m in ollama.list()['models']])"
```

**Expected Output:**
```
Models: ['llama3.2:3b', 'nomic-embed-text:latest']
```

### Step 10: Run Your RAG System

```bash
python src/main.py
```

**Expected Output:**
```
🤖 RAG System - Chat with Your Documents
🆕 Created new collection: documents

[A]dd document, [Q]uery, or [E]xit: 
```

### Step 11: Test the RAG System

**Add a test document:**
```
[A]dd document, [Q]uery, or [E]xit: a
Enter document path: /home/rich/dev/AI_workflow.md
```

**Expected Output:**
```
📄 Processing: /home/rich/dev/AI_workflow.md
📝 Split into 47 chunks
✅ Added 47 chunks to knowledge base
```

**Query the document:**
```
[A]dd document, [Q]uery, or [E]xit: q
Enter your question: What project types are available?
```

**Expected Output:**
```
🔍 Searching for: What project types are available?
╭─────────────────────── 🤖 AI Response ───────────────────────╮
│ Based on the context provided, there are 7 project types    │
│ available:                                                   │
│                                                              │
│ 1. RAG System - Document Q&A with retrieval                 │
│ 2. Multi-Agent - Collaborative AI agents                    │
│ 3. Document Processor - Bulk document analysis              │
│ 4. Semantic Search - Vector-based search                    │
│ 5. Custom Neural Net - GPU-accelerated ML                   │
│ 6. API Service - AI-powered web API                         │
│ 7. Data Pipeline - ETL with AI processing                   │
╰──────────────────────────────────────────────────────────────╯
```

---

## 🎯 Project Types Deep Dive

### 1. RAG System (Document Q&A)
**When to use:** Need to chat with PDFs, create knowledge bases, or build document Q&A systems

**Example creation:**
```bash
python create_ai_project.py --name "doc_chat_system" --type 1
```

**What you get:**
- ChromaDB vector database integration
- Document chunking and embedding
- Interactive chat interface
- PDF and text file support

**First steps after creation:**
1. Add documents with `[A]dd document`
2. Query with natural language
3. System automatically finds relevant chunks and generates answers

### 2. Multi-Agent System
**When to use:** Need collaborative AI for research, brainstorming, or complex problem-solving

**Example creation:**
```bash
python create_ai_project.py --name "research_team" --type 2
```

**What you get:**
- 3 specialized agents: Researcher, Critic, Synthesizer
- Collaborative discussion framework
- Memory and context management

**First steps after creation:**
1. Enter a research topic
2. Watch agents collaborate and debate
3. Get comprehensive analysis from multiple perspectives

### 3. Document Processor
**When to use:** Need to analyze hundreds of documents, extract summaries, or generate reports

**Example creation:**
```bash
python create_ai_project.py --name "bulk_analyzer" --type 3
```

**What you get:**
- Batch document processing
- AI-powered summarization and keyword extraction
- Progress tracking with Rich UI
- JSON output with metadata

### 4. Semantic Search
**When to use:** Need to find similar documents, build recommendation systems, or semantic search

**Example creation:**
```bash
python create_ai_project.py --name "doc_search" --type 4
```

**What you get:**
- Vector similarity search
- Document indexing with embeddings
- Ranked search results
- Interactive search interface

### 5. Custom Neural Network
**When to use:** Need to train custom models, experiment with architectures, or GPU-accelerated ML

**Example creation:**
```bash
python create_ai_project.py --name "custom_model" --type 5
```

**What you get:**
- PyTorch GPU acceleration setup
- Training loop with progress tracking
- Model checkpointing and visualization
- Sample data generation

### 6. API Service
**When to use:** Need to deploy AI as web service, create microservices, or production APIs

**Example creation:**
```bash
python create_ai_project.py --name "ai_api" --type 6
```

**What you get:**
- FastAPI web service framework
- Ollama integration endpoints
- Automatic API documentation
- Production-ready structure

**Test your API:**
```bash
python src/main.py  # Starts server on port 8000
curl http://localhost:8000/generate -X POST -H "Content-Type: application/json" -d '{"text": "Hello AI!"}'
```

### 7. Data Pipeline
**When to use:** Need ETL with AI processing, data enrichment, or automated analysis

**Example creation:**
```bash
python create_ai_project.py --name "data_enricher" --type 7
```

**What you get:**
- ETL pipeline framework
- AI-powered data analysis (sentiment, summarization, keywords)
- CSV processing with progress tracking
- Automated reporting

---

## 🔧 Working with Your Projects

### Managing Multiple Projects

**List all your projects:**
```bash
ls /home/rich/dev/projects/
```

**Switch between project environments:**
```bash
conda deactivate
conda activate next_ai_project    # or any other project name
```

### Customizing Your Project

**Add new dependencies:**
```bash
conda activate next_ai_project
pip install new-package
```

**Update environment file:**
```bash
conda env export > environment.yaml
```

**Edit configuration:**
```bash
nano config/config.yaml  # Project settings
nano .env                # Environment variables
```

### Project Development Workflow

**1. Start development:**
```bash
cd /home/rich/dev/projects/next_ai_project
conda activate next_ai_project
code .  # Opens in VS Code
```

**2. Run your application:**
```bash
python src/main.py
```

**3. Run tests (when you add them):**
```bash
python -m pytest tests/
```

**4. Commit changes:**
```bash
git add .
git commit -m "Add new feature"
```

---

## 🌐 Remote Access via Tailscale

### Access from Remote Machine

**WebUI Access:**
- URL: `http://100.82.174.94:8080`
- Use llama3.2:3b model for chat
- Upload documents for RAG

**API Projects:**
If you created an API service project:
```bash
# From remote machine
curl http://100.82.174.94:8000/generate -X POST -H "Content-Type: application/json" -d '{"text": "Hello from remote!"}'
```

---

## 🚀 GPU Monitoring

### Real-time GPU Usage
```bash
watch nvidia-smi
```

**What to look for:**
- GPU utilization spikes during model inference
- Memory usage increases when models load
- Temperature and power consumption

### GPU Usage in Projects
```bash
# Check if your project detects GPU
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"

# Monitor GPU during model runs
nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv --loop=1
```

---

## 🔍 Troubleshooting Guide

### Issue: "python: command not found"
**Solution:**
```bash
conda activate next_ai_project
# OR use full path
/home/rich/miniconda/envs/next_ai_project/bin/python src/main.py
```

### Issue: "ImportError: No module named 'ollama'"
**Solution:**
```bash
conda activate next_ai_project
pip install ollama
```

### Issue: "CUDA not available"
**Check:**
```bash
nvidia-smi  # Should show RTX 5080
nvcc --version  # Should show CUDA 12.8
conda activate next_ai_project
python -c "import torch; print(torch.version.cuda)"
```

### Issue: "Ollama connection failed"
**Check Ollama status:**
```bash
systemctl status ollama
ollama list  # Should show llama3.2:3b and nomic-embed-text
```

**Restart if needed:**
```bash
sudo systemctl restart ollama
```

### Issue: "ChromaDB collection errors"
**Solution:**
```bash
# Remove corrupted database
rm -rf ~/.cache/chromadb/
# Restart your application - it will recreate the database
```

### Issue: "Environment creation fails"
**Solutions:**
```bash
# Clean conda cache
conda clean --all

# Try creating environment again
cd /home/rich/dev/projects/next_ai_project
conda env create -f environment.yaml --force
```

---

## 📊 Success Checklist

After completing the walkthrough, verify everything works:

✅ **Project Created**: `next_ai_project` directory exists  
✅ **Environment Active**: `(next_ai_project)` shows in terminal  
✅ **GPU Detected**: `torch.cuda.is_available()` returns `True`  
✅ **Ollama Connected**: Models list shows llama3.2:3b  
✅ **Application Runs**: `python src/main.py` starts without errors  
✅ **Document Processing**: Can add documents and query them  
✅ **Remote Access**: WebUI accessible via Tailscale  

---

## 📚 Next Steps

### Experiment with Different Project Types
```bash
# Try a multi-agent system
python create_ai_project.py --name "research_agents" --type 2

# Try an API service
python create_ai_project.py --name "my_ai_api" --type 6

# Try document processing
python create_ai_project.py --name "doc_processor" --type 3
```

### Customize Templates
Edit `/home/rich/dev/ai_dev/create_ai_project.py` to:
- Add new project types
- Modify templates
- Add custom dependencies

### Scale Your Projects
- Deploy APIs to production
- Connect multiple agents
- Build complex pipelines
- Integrate with external services

Your AI development system is now ready for rapid prototyping and production deployment! 🚀

---

## 💡 Pro Tips

**Speed up project creation:**
```bash
# Create alias for faster access
echo 'alias new-ai="cd /home/rich/dev/ai_dev && conda activate ai_dev && python create_ai_project.py"' >> ~/.bashrc
source ~/.bashrc

# Now just run:
new-ai
```

**Monitor all projects:**
```bash
# See all conda environments (your projects)
conda env list

# Quick project status
ls /home/rich/dev/projects/
```

**Backup your work:**
```bash
# Each project is a git repository
cd /home/rich/dev/projects/next_ai_project
git remote add origin https://github.com/yourusername/next_ai_project.git
git push -u origin main
```