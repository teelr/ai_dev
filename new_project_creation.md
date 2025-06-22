🚀 AI Project Creation - Quick Reference

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 QUICK WORKFLOW (11 Steps)

1. Navigate to AI dev directory
   cd /home/rich/dev/ai_dev

2. Activate AI development environment  
   conda activate ai_dev

3. Create new project
   python create_ai_project.py --name "project_name" --type X
   
   OR interactive mode:
   python create_ai_project.py

4. Navigate to new project
   cd /home/rich/dev/projects/project_name

5. Create conda environment (2-5 minutes)
   conda env create -f environment.yaml

6. Activate project environment
   conda activate project_name

7. Verify GPU access
   python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"

8. Test Ollama connection
   python -c "import ollama; print('Models:', [m['name'] for m in ollama.list()['models']])"

9. Run the application
   python src/main.py

10. Test functionality (add document, query, etc.)

11. Start development
    code .  # VS Code
    # OR
    jupyter lab notebooks/  # Jupyter

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 PROJECT TYPES

1. RAG System         → Document Q&A, chat with PDFs
2. Multi-Agent        → Collaborative AI, research teams  
3. Document Processor → Bulk analysis, summarization
4. Semantic Search    → Vector search, recommendations
5. Custom Neural Net  → GPU training, deep learning
6. API Service        → Web APIs, microservices
7. Data Pipeline      → ETL, data enrichment

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 COMPLETE EXAMPLE

cd /home/rich/dev/ai_dev
conda activate ai_dev
python create_ai_project.py --name "document_chat" --type 1
cd /home/rich/dev/projects/document_chat
conda env create -f environment.yaml
conda activate document_chat
python -c "import torch; print(f'GPU: {torch.cuda.is_available()}')"
python src/main.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ SHORTCUTS

# Create alias for faster project creation
echo 'alias new-ai="cd /home/rich/dev/ai_dev && conda activate ai_dev && python create_ai_project.py"' >> ~/.bashrc
source ~/.bashrc

# Then just run:
new-ai

# List all projects
ls /home/rich/dev/projects/

# List all environments  
conda env list

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 COMMON ISSUES

"python: command not found"
→ conda activate project_name

"CUDA not available" 
→ nvidia-smi (check GPU)
→ conda activate project_name

"Ollama connection failed"
→ systemctl status ollama
→ ollama list

"Environment creation fails"
→ conda clean --all
→ Try again with --force

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ SUCCESS CHECK

□ Project directory exists
□ (project_name) shows in terminal
□ torch.cuda.is_available() = True  
□ ollama.list() shows models
□ python src/main.py runs
□ Application works (can add docs, query, etc.)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📖 For detailed guide: /home/rich/dev/AI_workflow.md