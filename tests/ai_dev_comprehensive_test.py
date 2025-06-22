#!/usr/bin/env python3
"""
Comprehensive AI Development Environment Test Suite
Tests all major AI components and frameworks installed
"""

import sys
import traceback
from typing import Dict, List, Any
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from loguru import logger

console = Console()

class TestRunner:
    def __init__(self):
        self.results = {}
        
    def test_pytorch_gpu(self) -> Dict[str, Any]:
        """Test PyTorch and GPU availability"""
        try:
            import torch
            result = {
                "pytorch_version": torch.__version__,
                "cuda_available": torch.cuda.is_available(),
                "cuda_version": torch.version.cuda if torch.cuda.is_available() else None,
                "gpu_count": torch.cuda.device_count() if torch.cuda.is_available() else 0,
                "gpu_name": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
                "status": "✅ Working"
            }
        except Exception as e:
            result = {"status": "❌ Failed", "error": str(e)}
        return result
    
    def test_sentence_transformers(self) -> Dict[str, Any]:
        """Test sentence transformers"""
        try:
            from sentence_transformers import SentenceTransformer
            model = SentenceTransformer('all-MiniLM-L6-v2')
            embedding = model.encode("test sentence")
            result = {
                "model_loaded": True,
                "embedding_shape": embedding.shape,
                "status": "✅ Working"
            }
        except Exception as e:
            result = {"status": "❌ Failed", "error": str(e)}
        return result
    
    def test_vector_databases(self) -> Dict[str, Any]:
        """Test ChromaDB, FAISS, and Milvus"""
        results = {}
        
        # ChromaDB
        try:
            import chromadb
            client = chromadb.Client()
            collection = client.create_collection(name="test_chroma")
            collection.add(
                embeddings=[[1.0, 2.0, 3.0]],
                documents=["test doc"],
                ids=["id1"]
            )
            results["chromadb"] = "✅ Working"
        except Exception as e:
            results["chromadb"] = f"❌ Failed: {str(e)}"
        
        # FAISS
        try:
            import faiss
            import numpy as np
            dimension = 128
            index = faiss.IndexFlatL2(dimension)
            vectors = np.random.random((10, dimension)).astype('float32')
            index.add(vectors)
            results["faiss"] = "✅ Working"
        except Exception as e:
            results["faiss"] = f"❌ Failed: {str(e)}"
        
        # Milvus
        try:
            from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType
            results["milvus"] = "✅ Library loaded"
        except Exception as e:
            results["milvus"] = f"❌ Failed: {str(e)}"
        
        return results
    
    def test_langchain(self) -> Dict[str, Any]:
        """Test LangChain components"""
        results = {}
        
        try:
            from langchain.text_splitter import RecursiveCharacterTextSplitter
            splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
            chunks = splitter.split_text("This is a test document. " * 20)
            results["text_splitter"] = f"✅ Working ({len(chunks)} chunks)"
        except Exception as e:
            results["text_splitter"] = f"❌ Failed: {str(e)}"
        
        try:
            from langchain_community.vectorstores import Chroma
            results["chroma_vectorstore"] = "✅ Available"
        except Exception as e:
            results["chroma_vectorstore"] = f"❌ Failed: {str(e)}"
        
        return results
    
    def test_agentic_frameworks(self) -> Dict[str, Any]:
        """Test AutoGen and MemGPT"""
        results = {}
        
        # AutoGen
        try:
            import autogen
            results["autogen"] = f"✅ v{autogen.__version__}"
        except Exception as e:
            results["autogen"] = f"❌ Failed: {str(e)}"
        
        # MemGPT
        try:
            import memgpt
            results["memgpt"] = "✅ Available"
        except Exception as e:
            results["memgpt"] = f"❌ Failed: {str(e)}"
        
        return results
    
    def test_document_processing(self) -> Dict[str, Any]:
        """Test document processing libraries"""
        results = {}
        
        libraries = [
            ("unstructured", "unstructured"),
            ("pypdf", "pypdf"),
            ("python-docx", "docx"),
            ("python-pptx", "pptx"),
            ("openpyxl", "openpyxl"),
            ("beautifulsoup4", "bs4"),
            ("lxml", "lxml")
        ]
        
        for name, import_name in libraries:
            try:
                __import__(import_name)
                results[name] = "✅ Available"
            except Exception as e:
                results[name] = f"❌ Failed: {str(e)}"
        
        return results
    
    def test_database_tools(self) -> Dict[str, Any]:
        """Test PostgreSQL and database tools"""
        results = {}
        
        try:
            import psycopg
            results["psycopg"] = "✅ Available"
        except Exception as e:
            results["psycopg"] = f"❌ Failed: {str(e)}"
        
        try:
            import sqlalchemy
            results["sqlalchemy"] = f"✅ v{sqlalchemy.__version__}"
        except Exception as e:
            results["sqlalchemy"] = f"❌ Failed: {str(e)}"
        
        try:
            import alembic
            results["alembic"] = f"✅ v{alembic.__version__}"
        except Exception as e:
            results["alembic"] = f"❌ Failed: {str(e)}"
        
        return results
    
    def test_utilities(self) -> Dict[str, Any]:
        """Test developer utilities"""
        results = {}
        
        utilities = [
            ("typer", "typer"),
            ("tqdm", "tqdm"),
            ("rica", "rich"),
            ("loguru", "loguru"),
            ("httpx", "httpx"),
            ("aiohttp", "aiohttp")
        ]
        
        for name, import_name in utilities:
            try:
                module = __import__(import_name)
                version = getattr(module, '__version__', 'Unknown')
                results[name] = f"✅ v{version}"
            except Exception as e:
                results[name] = f"❌ Failed: {str(e)}"
        
        return results
    
    def run_all_tests(self):
        """Run all tests with progress tracking"""
        tests = [
            ("PyTorch & GPU", self.test_pytorch_gpu),
            ("Sentence Transformers", self.test_sentence_transformers),
            ("Vector Databases", self.test_vector_databases),
            ("LangChain", self.test_langchain),
            ("Agentic Frameworks", self.test_agentic_frameworks),
            ("Document Processing", self.test_document_processing),
            ("Database Tools", self.test_database_tools),
            ("Developer Utilities", self.test_utilities)
        ]
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            
            for test_name, test_func in tests:
                task = progress.add_task(f"Testing {test_name}...", total=None)
                try:
                    self.results[test_name] = test_func()
                    progress.update(task, description=f"✅ {test_name}")
                except Exception as e:
                    self.results[test_name] = {"status": "❌ Failed", "error": str(e)}
                    progress.update(task, description=f"❌ {test_name}")
                progress.remove_task(task)
    
    def display_results(self):
        """Display test results in a formatted table"""
        console.print("\n" + "="*80)
        console.print(Panel.fit(
            "[bold green]🚀 AI Development Environment Test Results[/bold green]",
            style="bold"
        ))
        
        for category, results in self.results.items():
            console.print(f"\n[bold cyan]{category}[/bold cyan]")
            
            if isinstance(results, dict):
                if "status" in results:
                    # Single test result
                    console.print(f"  {results['status']}")
                    if "error" in results:
                        console.print(f"    Error: {results['error']}")
                    else:
                        for key, value in results.items():
                            if key != "status":
                                console.print(f"    {key}: {value}")
                else:
                    # Multiple test results
                    for test_name, result in results.items():
                        console.print(f"  {test_name}: {result}")
        
        # Summary
        total_tests = sum(len(results) if isinstance(results, dict) and "status" not in results 
                         else 1 for results in self.results.values())
        passed_tests = sum(
            sum(1 for result in results.values() if "✅" in str(result))
            if isinstance(results, dict) and "status" not in results
            else (1 if "✅" in str(results.get("status", "")) else 0)
            for results in self.results.values()
        )
        
        console.print(f"\n[bold]Summary: {passed_tests}/{total_tests} tests passed[/bold]")
        
        # Next steps
        console.print(Panel(
            "[bold yellow]Next Steps:[/bold yellow]\n"
            "1. Install Ollama: curl -fsSL https://ollama.com/install.sh | sh\n"
            "2. Pull models: ollama pull llama2, ollama pull nomic-embed-text\n"
            "3. Start PostgreSQL if needed for database testing\n"
            "4. Install Open-WebUI for web interface\n"
            "5. Test with actual AI workflows",
            title="Recommendations"
        ))

def main():
    """Main test runner"""
    console.print(Panel.fit(
        "[bold blue]AI Development Environment Comprehensive Test[/bold blue]\n"
        f"Python: {sys.version.split()[0]} | Platform: {sys.platform}",
        style="bold"
    ))
    
    runner = TestRunner()
    runner.run_all_tests()
    runner.display_results()

if __name__ == "__main__":
    main()