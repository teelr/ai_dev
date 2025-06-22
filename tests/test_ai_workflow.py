#!/usr/bin/env python3
"""
End-to-End AI Workflow Test
Demonstrates a complete RAG pipeline with local models
"""

import ollama
import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from rich.console import Console
from rich.panel import Panel

console = Console()

def test_complete_rag_workflow():
    """Test a complete RAG workflow with local models"""
    console.print(Panel("🚀 Testing Complete RAG Workflow", style="bold green"))
    
    # 1. Document Processing
    console.print("📄 [bold cyan]Step 1:[/bold cyan] Processing documents...")
    documents = [
        "Artificial Intelligence (AI) is transforming how we work and live.",
        "Machine Learning is a subset of AI that learns from data.",
        "Large Language Models like LLaMA can understand and generate text.",
        "Vector databases store embeddings for semantic search.",
        "RAG combines retrieval with generation for better AI responses."
    ]
    
    # Split documents
    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    all_chunks = []
    for doc in documents:
        chunks = splitter.split_text(doc)
        all_chunks.extend(chunks)
    
    console.print(f"  ✅ Split {len(documents)} documents into {len(all_chunks)} chunks")
    
    # 2. Generate Embeddings
    console.print("🔢 [bold cyan]Step 2:[/bold cyan] Generating embeddings...")
    embeddings = []
    for chunk in all_chunks:
        response = ollama.embeddings(model='nomic-embed-text', prompt=chunk)
        embeddings.append(response['embedding'])
    
    console.print(f"  ✅ Generated {len(embeddings)} embeddings (dim={len(embeddings[0])})")
    
    # 3. Store in Vector Database
    console.print("🗄️ [bold cyan]Step 3:[/bold cyan] Storing in vector database...")
    client = chromadb.Client()
    
    try:
        collection = client.get_collection("ai_knowledge")
        client.delete_collection("ai_knowledge")
    except:
        pass
    
    collection = client.create_collection("ai_knowledge")
    
    # Add documents to ChromaDB
    ids = [f"doc_{i}" for i in range(len(all_chunks))]
    collection.add(
        embeddings=embeddings,
        documents=all_chunks,
        ids=ids
    )
    
    console.print(f"  ✅ Stored {collection.count()} documents in ChromaDB")
    
    # 4. Query Processing
    console.print("🔍 [bold cyan]Step 4:[/bold cyan] Processing user query...")
    user_query = "What is machine learning?"
    
    # Generate query embedding
    query_response = ollama.embeddings(model='nomic-embed-text', prompt=user_query)
    query_embedding = query_response['embedding']
    
    # Search similar documents
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )
    
    relevant_docs = results['documents'][0]
    console.print(f"  ✅ Found {len(relevant_docs)} relevant documents")
    for i, doc in enumerate(relevant_docs):
        console.print(f"    {i+1}. {doc[:50]}...")
    
    # 5. Generate Response
    console.print("🤖 [bold cyan]Step 5:[/bold cyan] Generating AI response...")
    
    context = "\n".join(relevant_docs)
    prompt = f"""Context: {context}

Question: {user_query}

Answer based on the context provided:"""
    
    response = ollama.generate(model='llama3.2:3b', prompt=prompt)
    ai_answer = response['response'].strip()
    
    console.print(f"  ✅ Generated response ({len(ai_answer)} chars)")
    
    # 6. Display Results
    console.print("\n" + "="*60)
    console.print(Panel(f"[bold yellow]Query:[/bold yellow] {user_query}", title="User Question"))
    console.print(Panel(f"[bold green]{ai_answer}[/bold green]", title="AI Response"))
    
    return True

def test_multi_agent_simulation():
    """Test basic multi-agent interaction"""
    console.print(Panel("🤝 Testing Multi-Agent Simulation", style="bold blue"))
    
    # Simulate two AI agents discussing
    agents = {
        "Researcher": "You are a researcher who provides factual information.",
        "Critic": "You are a critic who questions and challenges ideas."
    }
    
    topic = "The future of AI development"
    conversation = []
    
    for round_num in range(2):
        for agent_name, role in agents.items():
            if round_num == 0 and agent_name == "Researcher":
                prompt = f"{role} Discuss: {topic}"
            else:
                context = "\n".join([f"{name}: {msg}" for name, msg in conversation[-2:]])
                prompt = f"{role}\n\nPrevious discussion:\n{context}\n\nYour response:"
            
            response = ollama.generate(model='llama3.2:3b', prompt=prompt)
            message = response['response'].strip()[:150] + "..."
            conversation.append((agent_name, message))
            
            console.print(f"🤖 [bold cyan]{agent_name}:[/bold cyan] {message}")
    
    console.print("  ✅ Multi-agent conversation completed")
    return True

def main():
    """Run all workflow tests"""
    console.print(Panel.fit(
        "[bold magenta]🧪 AI Development Environment - End-to-End Test[/bold magenta]",
        style="bold"
    ))
    
    try:
        # Test 1: Complete RAG Workflow
        test_complete_rag_workflow()
        
        console.print("\n")
        
        # Test 2: Multi-Agent Simulation
        test_multi_agent_simulation()
        
        # Success Summary
        console.print("\n" + "="*60)
        console.print(Panel(
            "[bold green]🎉 ALL TESTS PASSED![/bold green]\n\n"
            "✅ Document processing and chunking\n"
            "✅ Local embedding generation (nomic-embed-text)\n"
            "✅ Vector database storage (ChromaDB)\n"
            "✅ Semantic search and retrieval\n"
            "✅ Local LLM generation (LLaMA 3.2 3B)\n"
            "✅ Complete RAG pipeline\n"
            "✅ Multi-agent interactions\n\n"
            "[bold yellow]Your AI development environment is FULLY OPERATIONAL! 🚀[/bold yellow]",
            title="Success!"
        ))
        
    except Exception as e:
        console.print(f"\n❌ [bold red]Test failed:[/bold red] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()