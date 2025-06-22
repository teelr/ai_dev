#!/usr/bin/env python3
"""
AI Project Creation Workflow
Interactive tool to scaffold new AI projects with your system
"""

import shutil
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table

console = Console()

class AIProjectCreator:
    def __init__(self):
        self.base_dir = Path("/home/rich/dev/projects")
        self.templates_dir = Path("/home/rich/dev/ai_dev/templates")
        
    def show_project_types(self):
        """Display available AI project types"""
        table = Table(title="🤖 Available AI Project Types")
        table.add_column("Type", style="cyan")
        table.add_column("Description", style="green")
        table.add_column("Use Cases", style="yellow")
        
        table.add_row("1. RAG System", "Document Q&A with retrieval", "Chat with PDFs, knowledge base")
        table.add_row("2. Multi-Agent", "Collaborative AI agents", "Research teams, workflow automation")
        table.add_row("3. Document Processor", "Bulk document analysis", "Content extraction, summarization")
        table.add_row("4. Semantic Search", "Vector-based search engine", "Similar document finding")
        table.add_row("5. Custom Neural Net", "GPU-accelerated ML", "Training custom models")
        table.add_row("6. API Service", "AI-powered web API", "Production AI services")
        table.add_row("7. Data Pipeline", "ETL with AI processing", "Data transformation workflows")
        
        console.print(table)
    
    def create_project_structure(self, project_name: str, project_type: str):
        """Create the basic project structure"""
        project_path = self.base_dir / project_name
        
        if project_path.exists():
            if not Confirm.ask(f"Project {project_name} already exists. Overwrite?"):
                return None
            shutil.rmtree(project_path)
        
        # Create directory structure
        dirs_to_create = [
            "src",
            "data/raw",
            "data/processed", 
            "models",
            "notebooks",
            "tests",
            "docs",
            "config",
            "scripts",
            "output"
        ]
        
        for dir_path in dirs_to_create:
            (project_path / dir_path).mkdir(parents=True, exist_ok=True)
        
        return project_path
    
    def create_environment_yaml(self, project_path: Path, project_type: str):
        """Create conda environment file"""
        env_content = f"""name: {project_path.name}
channels:
  - pytorch
  - nvidia
  - conda-forge
  - defaults

dependencies:
  - python=3.10
  - pip
  - git
  
  # Core AI/ML
  - pytorch
  - torchvision
  - pytorch-cuda=12.1
  
  - pip:
    # Local LLM
    - ollama
    
    # AI Frameworks
    - langchain
    - langchain-community
    - langchain-ollama
    
    # Vector Databases
    - chromadb
    - faiss-cpu
    - pymilvus
    
    # Document Processing
    - unstructured[all-docs]
    - pypdf
    - python-docx
    - beautifulsoup4
    
    # Data Processing
    - pandas
    - numpy
    - scipy
    
    # Web & API
    - fastapi
    - uvicorn
    - streamlit
    
    # Utilities
    - rich
    - typer
    - loguru
    - python-dotenv
    
    # Development
    - pytest
    - jupyter
    - ruff
"""
        
        # Add project-specific dependencies
        if "multi-agent" in project_type.lower():
            env_content += """    - pyautogen
    - pymemgpt
"""
        
        if "neural" in project_type.lower() or "custom" in project_type.lower():
            env_content += """    - transformers
    - datasets
    - accelerate
    - wandb
"""
        
        if "api" in project_type.lower():
            env_content += """    - pydantic
    - python-multipart
    - httpx
"""
        
        (project_path / "environment.yaml").write_text(env_content)
    
    def create_main_script(self, project_path: Path, project_type: str):
        """Create the main project script based on type"""
        templates = {
            "rag": self.get_rag_template(),
            "multi-agent": self.get_multiagent_template(),
            "document": self.get_document_template(),
            "semantic": self.get_semantic_template(),
            "neural": self.get_neural_template(),
            "api": self.get_api_template(),
            "pipeline": self.get_pipeline_template()
        }
        
        # Determine template key
        template_key = next((key for key in templates.keys() if key in project_type.lower()), "rag")
        template_content = templates[template_key]
        
        (project_path / "src" / "main.py").write_text(template_content)
    
    def get_rag_template(self):
        return '''#!/usr/bin/env python3
"""
RAG System - Retrieval Augmented Generation
Chat with your documents using local AI
"""

import ollama
import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from rich.console import Console
from pathlib import Path
import typer

console = Console()

class RAGSystem:
    def __init__(self, collection_name: str = "documents"):
        self.client = chromadb.Client()
        self.collection_name = collection_name
        self.collection = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200
        )
        
    def initialize_collection(self):
        """Initialize or get the document collection"""
        try:
            self.collection = self.client.get_collection(self.collection_name)
            console.print(f"✅ Loaded existing collection: {self.collection_name}")
        except:
            self.collection = self.client.create_collection(self.collection_name)
            console.print(f"🆕 Created new collection: {self.collection_name}")
    
    def add_document(self, file_path: str):
        """Add a document to the knowledge base"""
        console.print(f"📄 Processing: {file_path}")
        
        # Load and split document
        if file_path.endswith('.pdf'):
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            text = "\\n".join([doc.page_content for doc in documents])
        else:
            text = Path(file_path).read_text()
        
        chunks = self.text_splitter.split_text(text)
        console.print(f"📝 Split into {len(chunks)} chunks")
        
        # Generate embeddings and store
        embeddings = []
        for chunk in chunks:
            response = ollama.embeddings(model='nomic-embed-text', prompt=chunk)
            embeddings.append(response['embedding'])
        
        # Add to collection
        ids = [f"{Path(file_path).stem}_{i}" for i in range(len(chunks))]
        self.collection.add(
            embeddings=embeddings,
            documents=chunks,
            ids=ids
        )
        
        console.print(f"✅ Added {len(chunks)} chunks to knowledge base")
    
    def query(self, question: str, n_results: int = 3) -> str:
        """Query the knowledge base and generate response"""
        console.print(f"🔍 Searching for: {question}")
        
        # Get query embedding
        query_response = ollama.embeddings(model='nomic-embed-text', prompt=question)
        query_embedding = query_response['embedding']
        
        # Search similar documents
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        
        relevant_docs = results['documents'][0]
        context = "\\n\\n".join(relevant_docs)
        
        # Generate response
        prompt = f"""Context: {context}

Question: {question}

Answer based on the context provided:"""
        
        response = ollama.generate(model='llama3.2:3b', prompt=prompt)
        return response['response'].strip()

def main():
    """Main RAG application"""
    console.print(Panel("🤖 RAG System - Chat with Your Documents", style="bold green"))
    
    rag = RAGSystem()
    rag.initialize_collection()
    
    while True:
        action = typer.prompt("\\n[A]dd document, [Q]uery, or [E]xit")
        
        if action.lower() == 'a':
            file_path = typer.prompt("Enter document path")
            if Path(file_path).exists():
                rag.add_document(file_path)
            else:
                console.print("❌ File not found")
                
        elif action.lower() == 'q':
            question = typer.prompt("Enter your question")
            answer = rag.query(question)
            console.print(Panel(answer, title="🤖 AI Response", style="blue"))
            
        elif action.lower() == 'e':
            break

if __name__ == "__main__":
    main()
'''
    
    def get_multiagent_template(self):
        return '''#!/usr/bin/env python3
"""
Multi-Agent System
Collaborative AI agents working together
"""

import ollama
from rich.console import Console
from typing import List, Dict
import time

console = Console()

class AIAgent:
    def __init__(self, name: str, role: str, model: str = "llama3.2:3b"):
        self.name = name
        self.role = role
        self.model = model
        self.memory = []
    
    def think(self, prompt: str, context: List[str] = None) -> str:
        """Agent thinking and response generation"""
        full_prompt = f"You are {self.name}, a {self.role}.\\n\\n"
        
        if context:
            full_prompt += "Previous conversation:\\n"
            full_prompt += "\\n".join(context[-3:])  # Last 3 messages
            full_prompt += "\\n\\n"
        
        full_prompt += f"Task: {prompt}\\n\\nYour response:"
        
        response = ollama.generate(model=self.model, prompt=full_prompt)
        message = response['response'].strip()
        
        self.memory.append(f"{self.name}: {message}")
        return message

class MultiAgentSystem:
    def __init__(self):
        self.agents = {}
        self.conversation_history = []
    
    def add_agent(self, agent: AIAgent):
        """Add an agent to the system"""
        self.agents[agent.name] = agent
        console.print(f"✅ Added agent: {agent.name} ({agent.role})")
    
    def collaborate(self, task: str, rounds: int = 3):
        """Run collaborative discussion between agents"""
        console.print(f"🚀 Starting collaboration on: {task}")
        
        for round_num in range(rounds):
            console.print(f"\\n--- Round {round_num + 1} ---")
            
            for agent_name, agent in self.agents.items():
                console.print(f"\\n🤖 {agent_name} thinking...")
                
                # Agent responds to task and conversation
                response = agent.think(task, self.conversation_history)
                
                # Add to conversation
                message = f"{agent_name}: {response}"
                self.conversation_history.append(message)
                
                # Display response
                console.print(f"💬 {agent_name}: {response[:100]}...")
                
                time.sleep(1)  # Brief pause for readability
        
        return self.conversation_history

def create_research_team():
    """Create a research team of AI agents"""
    system = MultiAgentSystem()
    
    # Add different types of agents
    system.add_agent(AIAgent(
        "Researcher", 
        "thorough researcher who gathers and analyzes information"
    ))
    
    system.add_agent(AIAgent(
        "Critic", 
        "critical thinker who questions assumptions and finds flaws"
    ))
    
    system.add_agent(AIAgent(
        "Synthesizer", 
        "creative thinker who combines ideas and finds connections"
    ))
    
    return system

def main():
    """Main multi-agent application"""
    console.print(Panel("🤝 Multi-Agent Collaboration System", style="bold green"))
    
    # Create agent team
    team = create_research_team()
    
    # Get research topic
    topic = input("\\nEnter research topic: ")
    
    # Run collaboration
    results = team.collaborate(topic, rounds=2)
    
    # Show final results
    console.print("\\n" + "="*60)
    console.print(Panel("📋 Collaboration Results", style="bold blue"))
    
    for message in results:
        console.print(f"• {message[:80]}...")

if __name__ == "__main__":
    main()
'''
    
    def get_api_template(self):
        return '''#!/usr/bin/env python3
"""
AI API Service
FastAPI service for AI-powered endpoints
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama
import chromadb
from typing import List, Optional
import uvicorn

app = FastAPI(title="AI API Service", version="1.0.0")

# Pydantic models
class QueryRequest(BaseModel):
    text: str
    model: str = "llama3.2:3b"

class QueryResponse(BaseModel):
    response: str
    model_used: str

class EmbeddingRequest(BaseModel):
    text: str
    model: str = "nomic-embed-text"

class EmbeddingResponse(BaseModel):
    embedding: List[float]
    dimensions: int

# Initialize services
client = chromadb.Client()

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "AI API Service is running!", "status": "healthy"}

@app.post("/generate", response_model=QueryResponse)
async def generate_text(request: QueryRequest):
    """Generate text using local LLM"""
    try:
        response = ollama.generate(model=request.model, prompt=request.text)
        return QueryResponse(
            response=response['response'],
            model_used=request.model
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/embeddings", response_model=EmbeddingResponse)
async def get_embeddings(request: EmbeddingRequest):
    """Generate embeddings for text"""
    try:
        response = ollama.embeddings(model=request.model, prompt=request.text)
        embedding = response['embedding']
        return EmbeddingResponse(
            embedding=embedding,
            dimensions=len(embedding)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/models")
async def list_models():
    """List available models"""
    try:
        models = ollama.list()
        return {"models": [model['name'] for model in models['models']]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''
    
    def get_document_template(self):
        return '''#!/usr/bin/env python3
"""
Document Processor
Bulk document analysis and processing
"""

import ollama
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
import typer
from typing import List, Dict
import json
from datetime import datetime

console = Console()

class DocumentProcessor:
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def process_single_document(self, file_path: Path) -> Dict:
        """Process a single document"""
        console.print(f"📄 Processing: {file_path.name}")
        
        # Read document
        if file_path.suffix == '.pdf':
            from pypdf import PdfReader
            reader = PdfReader(file_path)
            text = "\\n".join([page.extract_text() for page in reader.pages])
        else:
            text = file_path.read_text(encoding='utf-8')
        
        # Analyze with AI
        summary_prompt = f"Summarize this document in 2-3 sentences:\\n\\n{text[:2000]}"
        summary_response = ollama.generate(model='llama3.2:3b', prompt=summary_prompt)
        
        keywords_prompt = f"Extract 5-10 key topics from this text:\\n\\n{text[:2000]}"
        keywords_response = ollama.generate(model='llama3.2:3b', prompt=keywords_prompt)
        
        return {
            "filename": file_path.name,
            "path": str(file_path),
            "word_count": len(text.split()),
            "char_count": len(text),
            "summary": summary_response['response'].strip(),
            "keywords": keywords_response['response'].strip(),
            "processed_at": datetime.now().isoformat()
        }
    
    def process_directory(self, input_dir: str, pattern: str = "*.txt") -> List[Dict]:
        """Process all documents in a directory"""
        input_path = Path(input_dir)
        files = list(input_path.glob(pattern))
        
        if not files:
            console.print(f"❌ No files found matching {pattern} in {input_dir}")
            return []
        
        results = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Processing documents...", total=len(files))
            
            for file_path in files:
                try:
                    result = self.process_single_document(file_path)
                    results.append(result)
                    progress.update(task, advance=1, description=f"Processed {file_path.name}")
                except Exception as e:
                    console.print(f"❌ Error processing {file_path.name}: {e}")
        
        # Save results
        output_file = self.output_dir / "processing_results.json"
        output_file.write_text(json.dumps(results, indent=2))
        
        console.print(f"✅ Processed {len(results)} documents")
        console.print(f"📁 Results saved to: {output_file}")
        
        return results

def main():
    """Main document processing application"""
    console.print(Panel("📄 Document Processor", style="bold green"))
    
    processor = DocumentProcessor()
    
    input_dir = typer.prompt("Enter directory path with documents")
    pattern = typer.prompt("Enter file pattern (e.g., *.pdf, *.txt)", default="*.txt")
    
    results = processor.process_directory(input_dir, pattern)
    
    if results:
        console.print("\\n📊 Processing Summary:")
        for result in results[:3]:  # Show first 3
            console.print(f"• {result['filename']}: {result['summary'][:60]}...")

if __name__ == "__main__":
    main()
'''
    
    def get_semantic_template(self):
        return '''#!/usr/bin/env python3
"""
Semantic Search Engine
Vector-based document similarity search
"""

import ollama
import chromadb
import numpy as np
from pathlib import Path
from rich.console import Console
from rich.table import Table
import typer

console = Console()

class SemanticSearchEngine:
    def __init__(self, collection_name: str = "semantic_search"):
        self.client = chromadb.Client()
        self.collection_name = collection_name
        self.collection = None
        
    def initialize(self):
        """Initialize the search engine"""
        try:
            self.collection = self.client.get_collection(self.collection_name)
        except:
            self.collection = self.client.create_collection(self.collection_name)
        console.print(f"🔍 Search engine initialized: {self.collection_name}")
    
    def index_documents(self, docs_dir: str):
        """Index documents for search"""
        docs_path = Path(docs_dir)
        files = list(docs_path.glob("*.txt")) + list(docs_path.glob("*.md"))
        
        if not files:
            console.print("❌ No documents found to index")
            return
        
        console.print(f"📚 Indexing {len(files)} documents...")
        
        for file_path in files:
            text = file_path.read_text()
            
            # Generate embedding
            response = ollama.embeddings(model='nomic-embed-text', prompt=text)
            embedding = response['embedding']
            
            # Add to collection
            self.collection.add(
                embeddings=[embedding],
                documents=[text],
                metadatas=[{"filename": file_path.name, "path": str(file_path)}],
                ids=[file_path.stem]
            )
        
        console.print(f"✅ Indexed {len(files)} documents")
    
    def search(self, query: str, n_results: int = 5):
        """Search for similar documents"""
        # Generate query embedding
        response = ollama.embeddings(model='nomic-embed-text', prompt=query)
        query_embedding = response['embedding']
        
        # Search
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        
        return results
    
    def display_results(self, query: str, results):
        """Display search results in a nice format"""
        console.print(f"\\n🔍 Search results for: '{query}'\\n")
        
        table = Table(title="Search Results")
        table.add_column("Rank", style="cyan")
        table.add_column("File", style="green")
        table.add_column("Preview", style="yellow")
        table.add_column("Score", style="red")
        
        documents = results['documents'][0]
        metadatas = results['metadatas'][0]
        distances = results['distances'][0]
        
        for i, (doc, metadata, distance) in enumerate(zip(documents, metadatas, distances)):
            preview = doc[:100] + "..." if len(doc) > 100 else doc
            score = f"{1 - distance:.3f}"  # Convert distance to similarity score
            
            table.add_row(
                str(i + 1),
                metadata.get('filename', 'Unknown'),
                preview,
                score
            )
        
        console.print(table)

def main():
    """Main semantic search application"""
    console.print(Panel("🔍 Semantic Search Engine", style="bold green"))
    
    engine = SemanticSearchEngine()
    engine.initialize()
    
    while True:
        action = typer.prompt("\\n[I]ndex documents, [S]earch, or [E]xit")
        
        if action.lower() == 'i':
            docs_dir = typer.prompt("Enter documents directory path")
            engine.index_documents(docs_dir)
            
        elif action.lower() == 's':
            query = typer.prompt("Enter search query")
            results = engine.search(query)
            engine.display_results(query, results)
            
        elif action.lower() == 'e':
            break

if __name__ == "__main__":
    main()
'''
    
    def get_neural_template(self):
        return '''#!/usr/bin/env python3
"""
Custom Neural Network
GPU-accelerated machine learning with PyTorch
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
from rich.console import Console
from rich.progress import Progress
import matplotlib.pyplot as plt

console = Console()

class CustomNeuralNet(nn.Module):
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size // 2, output_size)
        )
    
    def forward(self, x):
        return self.layers(x)

class NeuralNetTrainer:
    def __init__(self, model, device):
        self.model = model.to(device)
        self.device = device
        self.train_losses = []
        self.val_losses = []
    
    def train_epoch(self, dataloader, optimizer, criterion):
        """Train for one epoch"""
        self.model.train()
        total_loss = 0
        
        for batch_x, batch_y in dataloader:
            batch_x, batch_y = batch_x.to(self.device), batch_y.to(self.device)
            
            optimizer.zero_grad()
            outputs = self.model(batch_x)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        return total_loss / len(dataloader)
    
    def validate(self, dataloader, criterion):
        """Validate the model"""
        self.model.eval()
        total_loss = 0
        
        with torch.no_grad():
            for batch_x, batch_y in dataloader:
                batch_x, batch_y = batch_x.to(self.device), batch_y.to(self.device)
                outputs = self.model(batch_x)
                loss = criterion(outputs, batch_y)
                total_loss += loss.item()
        
        return total_loss / len(dataloader)
    
    def train(self, train_loader, val_loader, epochs: int = 100, lr: float = 0.001):
        """Full training loop"""
        optimizer = optim.Adam(self.model.parameters(), lr=lr)
        criterion = nn.MSELoss()
        
        console.print(f"🚀 Starting training on {self.device}")
        console.print(f"📊 Model parameters: {sum(p.numel() for p in self.model.parameters()):,}")
        
        with Progress(console=console) as progress:
            task = progress.add_task("Training...", total=epochs)
            
            for epoch in range(epochs):
                train_loss = self.train_epoch(train_loader, optimizer, criterion)
                val_loss = self.validate(val_loader, criterion)
                
                self.train_losses.append(train_loss)
                self.val_losses.append(val_loss)
                
                if epoch % 10 == 0:
                    progress.update(task, advance=10, 
                                    description=f"Epoch {epoch}: Train={train_loss:.4f}, Val={val_loss:.4f}")
        
        console.print("✅ Training completed!")
    
    def plot_losses(self):
        """Plot training history"""
        plt.figure(figsize=(10, 6))
        plt.plot(self.train_losses, label='Training Loss')
        plt.plot(self.val_losses, label='Validation Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.title('Training History')
        plt.legend()
        plt.grid(True)
        plt.savefig('training_history.png')
        console.print("📈 Training plot saved as training_history.png")

def create_sample_data(n_samples: int = 1000):
    """Create sample regression data"""
    X = np.random.randn(n_samples, 10)
    y = np.sum(X**2, axis=1) + 0.1 * np.random.randn(n_samples)  # Nonlinear function
    
    return torch.FloatTensor(X), torch.FloatTensor(y).unsqueeze(1)

def main():
    """Main neural network application"""
    console.print(Panel("🧠 Custom Neural Network Trainer", style="bold green"))
    
    # Check GPU availability
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    console.print(f"🖥️ Using device: {device}")
    
    if torch.cuda.is_available():
        console.print(f"🚀 GPU: {torch.cuda.get_device_name(0)}")
        console.print(f"💾 GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f}GB")
    
    # Create sample data
    console.print("📊 Generating sample data...")
    X, y = create_sample_data(5000)
    
    # Split data
    train_size = int(0.8 * len(X))
    X_train, X_val = X[:train_size], X[train_size:]
    y_train, y_val = y[:train_size], y[train_size:]
    
    # Create data loaders
    train_dataset = TensorDataset(X_train, y_train)
    val_dataset = TensorDataset(X_val, y_val)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=64)
    
    # Create model
    model = CustomNeuralNet(input_size=10, hidden_size=128, output_size=1)
    
    # Train model
    trainer = NeuralNetTrainer(model, device)
    trainer.train(train_loader, val_loader, epochs=100, lr=0.001)
    
    # Plot results
    trainer.plot_losses()
    
    # Save model
    torch.save(model.state_dict(), 'trained_model.pth')
    console.print("💾 Model saved as trained_model.pth")

if __name__ == "__main__":
    main()
'''
    
    def get_pipeline_template(self):
        return '''#!/usr/bin/env python3
"""
AI Data Pipeline
ETL pipeline with AI processing capabilities
"""

import pandas as pd
import ollama
from pathlib import Path
from rich.console import Console
from rich.progress import Progress
import json
from datetime import datetime
import typer

console = Console()

class AIDataPipeline:
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.processing_log = []
    
    def extract(self, file_pattern: str = "*.csv") -> pd.DataFrame:
        """Extract data from files"""
        console.print(f"🔍 Extracting data from {self.input_dir}/{file_pattern}")
        
        files = list(self.input_dir.glob(file_pattern))
        if not files:
            raise FileNotFoundError(f"No files found matching {file_pattern}")
        
        dfs = []
        for file_path in files:
            df = pd.read_csv(file_path)
            df['source_file'] = file_path.name
            dfs.append(df)
            console.print(f"✅ Loaded {file_path.name}: {len(df)} rows")
        
        combined_df = pd.concat(dfs, ignore_index=True)
        console.print(f"📊 Total extracted: {len(combined_df)} rows")
        
        return combined_df
    
    def transform_with_ai(self, df: pd.DataFrame, text_column: str) -> pd.DataFrame:
        """Transform data using AI processing"""
        console.print(f"🤖 AI processing column: {text_column}")
        
        if text_column not in df.columns:
            raise ValueError(f"Column '{text_column}' not found")
        
        # Add AI-generated columns
        df['ai_sentiment'] = None
        df['ai_summary'] = None
        df['ai_keywords'] = None
        
        with Progress(console=console) as progress:
            task = progress.add_task("AI Processing...", total=len(df))
            
            for idx, row in df.iterrows():
                text = str(row[text_column])
                
                if len(text) > 50:  # Only process substantial text
                    # Sentiment analysis
                    sentiment_prompt = f"Analyze the sentiment of this text (positive/negative/neutral):\\n{text[:500]}"
                    sentiment_response = ollama.generate(model='llama3.2:3b', prompt=sentiment_prompt)
                    df.at[idx, 'ai_sentiment'] = sentiment_response['response'].strip()
                    
                    # Summarization
                    summary_prompt = f"Summarize this text in one sentence:\\n{text[:500]}"
                    summary_response = ollama.generate(model='llama3.2:3b', prompt=summary_prompt)
                    df.at[idx, 'ai_summary'] = summary_response['response'].strip()
                    
                    # Keyword extraction
                    keywords_prompt = f"Extract 3-5 key terms from this text:\\n{text[:500]}"
                    keywords_response = ollama.generate(model='llama3.2:3b', prompt=keywords_prompt)
                    df.at[idx, 'ai_keywords'] = keywords_response['response'].strip()
                
                progress.update(task, advance=1)
        
        console.print("✅ AI transformation completed")
        return df
    
    def load(self, df: pd.DataFrame, filename: str = None):
        """Load processed data to output"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"processed_data_{timestamp}.csv"
        
        output_path = self.output_dir / filename
        df.to_csv(output_path, index=False)
        
        # Create summary report
        summary = {
            "processed_at": datetime.now().isoformat(),
            "total_rows": len(df),
            "columns": list(df.columns),
            "ai_processed_rows": len(df[df['ai_sentiment'].notna()]),
            "output_file": str(output_path)
        }
        
        summary_path = self.output_dir / f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        summary_path.write_text(json.dumps(summary, indent=2))
        
        console.print(f"💾 Data saved to: {output_path}")
        console.print(f"📋 Summary saved to: {summary_path}")
        
        return output_path
    
    def run_pipeline(self, file_pattern: str, text_column: str):
        """Run the complete ETL pipeline"""
        console.print(Panel("🚀 Starting AI Data Pipeline", style="bold green"))
        
        try:
            # Extract
            df = self.extract(file_pattern)
            
            # Transform
            df_processed = self.transform_with_ai(df, text_column)
            
            # Load
            output_path = self.load(df_processed)
            
            console.print(Panel("✅ Pipeline completed successfully!", style="bold green"))
            return output_path
            
        except Exception as e:
            console.print(f"❌ Pipeline failed: {e}")
            raise

def main():
    """Main data pipeline application"""
    console.print(Panel("📊 AI Data Pipeline", style="bold green"))
    
    input_dir = typer.prompt("Enter input directory path")
    output_dir = typer.prompt("Enter output directory path", default="output")
    file_pattern = typer.prompt("Enter file pattern", default="*.csv")
    text_column = typer.prompt("Enter text column name to process")
    
    pipeline = AIDataPipeline(input_dir, output_dir)
    pipeline.run_pipeline(file_pattern, text_column)

if __name__ == "__main__":
    main()
'''
    
    def create_config_files(self, project_path: Path):
        """Create configuration files"""
        # Create .env file
        env_content = """# AI Model Configuration
OLLAMA_MODEL=llama3.2:3b
EMBEDDING_MODEL=nomic-embed-text

# Database Configuration
VECTOR_DB=chromadb
COLLECTION_NAME=documents

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Logging
LOG_LEVEL=INFO
"""
        (project_path / ".env").write_text(env_content)
        
        # Create config.yaml
        config_content = """# Project Configuration
project:
  name: {project_name}
  version: "1.0.0"
  description: "AI Project"

models:
  llm: "llama3.2:3b"
  embedding: "nomic-embed-text"

data:
  chunk_size: 1000
  chunk_overlap: 200
  max_file_size: "10MB"

processing:
  batch_size: 32
  max_workers: 4

output:
  format: "json"
  include_metadata: true
""".format(project_name=project_path.name)
        
        (project_path / "config" / "config.yaml").write_text(config_content)
    
    def create_readme(self, project_path: Path, project_type: str):
        """Create README file"""
        readme_content = f"""# {project_path.name}

{project_type} AI project built with the ai_dev system.

## Setup

1. Create conda environment:
   ```bash
   conda env create -f environment.yaml
   conda activate {project_path.name}
   ```

2. Run the application:
   ```bash
   python src/main.py
   ```

## Project Structure

```
{project_path.name}/
├── src/                # Source code
├── data/              # Data files
│   ├── raw/          # Raw input data
│   └── processed/    # Processed data
├── models/           # Saved models
├── notebooks/        # Jupyter notebooks
├── tests/           # Test files
├── docs/            # Documentation
├── config/          # Configuration files
├── scripts/         # Utility scripts
└── output/          # Generated outputs
```

## Features

- 🤖 Local AI with Ollama (RTX 5080 accelerated)
- 🧠 Vector databases (ChromaDB, FAISS, Milvus)
- 📄 Document processing
- 🔍 Semantic search
- 🚀 GPU acceleration

## Requirements

- RTX 5080 GPU
- CUDA 12.8
- Python 3.10
- Ollama with llama3.2:3b and nomic-embed-text models

## Usage

[Add specific usage instructions based on project type]

## Configuration

Edit `config/config.yaml` and `.env` for project settings.
"""
        (project_path / "README.md").write_text(readme_content)
    
    def create_gitignore(self, project_path: Path):
        """Create .gitignore file"""
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.env

# Jupyter
.ipynb_checkpoints/

# Data
data/raw/*
!data/raw/.gitkeep
data/processed/*
!data/processed/.gitkeep

# Models
models/*
!models/.gitkeep

# Output
output/*
!output/.gitkeep

# Logs
*.log
logs/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# AI specific
*.pth
*.pkl
*.joblib
training_history.png
"""
        (project_path / ".gitignore").write_text(gitignore_content)
    
    def create_project(self):
        """Interactive project creation"""
        console.print(Panel("🚀 AI Project Creator", style="bold green"))
        
        # Show available project types
        self.show_project_types()
        
        # Get user input
        project_name = Prompt.ask("Enter project name")
        project_type = Prompt.ask("Choose project type (1-7)")
        
        # Map number to type
        type_map = {
            "1": "RAG System",
            "2": "Multi-Agent",
            "3": "Document Processor", 
            "4": "Semantic Search",
            "5": "Custom Neural Net",
            "6": "API Service",
            "7": "Data Pipeline"
        }
        
        if project_type not in type_map:
            console.print("❌ Invalid project type")
            return
        
        project_type_name = type_map[project_type]
        
        # Create project
        console.print(f"🏗️ Creating {project_type_name} project: {project_name}")
        
        project_path = self.create_project_structure(project_name, project_type_name)
        if not project_path:
            return
        
        # Create files
        self.create_environment_yaml(project_path, project_type_name)
        self.create_main_script(project_path, project_type_name)
        self.create_config_files(project_path)
        self.create_readme(project_path, project_type_name)
        self.create_gitignore(project_path)
        
        # Create .gitkeep files for empty directories
        for empty_dir in ["data/raw", "data/processed", "models", "output"]:
            (project_path / empty_dir / ".gitkeep").touch()
        
        # Initialize git repository
        import subprocess
        try:
            subprocess.run(["git", "init"], cwd=project_path, check=True, capture_output=True)
            subprocess.run(["git", "add", "."], cwd=project_path, check=True, capture_output=True)
            console.print("✅ Git repository initialized")
        except (subprocess.CalledProcessError, FileNotFoundError):
            console.print("⚠️ Git not available, skipping repository initialization")
        
        console.print(Panel(
            f"✅ Project '{project_name}' created successfully!\n\n"
            f"📁 Location: {project_path}\n"
            f"🎯 Type: {project_type_name}\n\n"
            f"Next steps:\n"
            f"1. cd {project_path}\n"
            f"2. conda env create -f environment.yaml\n"
            f"3. conda activate {project_name}\n"
            f"4. python src/main.py",
            title="🎉 Success!",
            style="bold green"
        ))
    
    def create_project_direct(self, project_name: str, project_type_num: int):
        """Create project directly with given parameters"""
        project_types = {
            1: "RAG System",
            2: "Multi-Agent",
            3: "Document Processor", 
            4: "Semantic Search",
            5: "Custom Neural Net",
            6: "API Service",
            7: "Data Pipeline"
        }
        
        if project_type_num not in project_types:
            console.print("❌ Invalid project type. Use 1-7.")
            return
            
        project_type_name = project_types[project_type_num]
        
        console.print(f"🚀 Creating {project_type_name}: {project_name}")
        
        # Create project structure
        project_path = self.create_project_structure(project_name, project_type_name.lower())
        if not project_path:
            return
        
        # Create files
        self.create_environment_yaml(project_path, project_type_name.lower())
        self.create_main_script(project_path, project_type_name.lower())
        self.create_readme(project_path, project_type_name)
        self.create_config_files(project_path)
        
        console.print(Panel(
            f"✅ Project '{project_name}' created successfully!\n\n"
            f"📁 Location: {project_path}\n"
            f"🎯 Type: {project_type_name}\n\n"
            f"Next steps:\n"
            f"1. cd {project_path}\n"
            f"2. conda env create -f environment.yaml\n"
            f"3. conda activate {project_name}\n"
            f"4. python src/main.py",
            title="🎉 Success!",
            style="bold green"
        ))

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="AI Project Creator - Scaffold new AI projects")
    parser.add_argument("--name", "-n", help="Project name")
    parser.add_argument("--type", "-t", type=int, help="Project type (1-7)")
    args = parser.parse_args()
    
    creator = AIProjectCreator()
    
    if args.name and args.type:
        # Non-interactive mode
        creator.create_project_direct(args.name, args.type)
    else:
        # Interactive mode
        creator.create_project()

if __name__ == "__main__":
    main()