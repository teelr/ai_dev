#!/usr/bin/env python3
"""
System Stress Test - Push CPU and System to Limits
Since GPU compute is blocked by CUDA compatibility
"""

import torch
import numpy as np
import multiprocessing as mp
import time
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

console = Console()

def cpu_intensive_task(size=4096, iterations=50):
    """CPU-intensive matrix operations"""
    # Use CPU tensors for computation
    A = torch.randn(size, size, dtype=torch.float32)
    B = torch.randn(size, size, dtype=torch.float32)
    
    results = []
    for i in range(iterations):
        C = torch.matmul(A, B)
        C = torch.relu(C)
        C = torch.softmax(C, dim=-1)
        results.append(C.sum().item())
    
    return sum(results)

def numpy_stress_test(size=8192, iterations=20):
    """NumPy-based stress test"""
    A = np.random.randn(size, size).astype(np.float32)
    B = np.random.randn(size, size).astype(np.float32)
    
    results = []
    for i in range(iterations):
        C = np.dot(A, B)
        C = np.maximum(C, 0)  # ReLU
        C = C / np.sum(C, axis=1, keepdims=True)  # Normalize
        results.append(np.sum(C))
    
    return sum(results)

def run_cpu_stress_test():
    """Multi-core CPU stress test"""
    console.print(Panel("🔥 CPU STRESS TEST - All Cores", style="bold red"))
    
    num_cores = mp.cpu_count()
    console.print(f"🖥️ Using all {num_cores} CPU cores")
    
    start_time = time.time()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
        console=console
    ) as progress:
        task = progress.add_task("Melting your CPU...", total=None)
        
        # Run on all cores simultaneously
        with ProcessPoolExecutor(max_workers=num_cores) as executor:
            futures = []
            for i in range(num_cores):
                future = executor.submit(cpu_intensive_task, 2048, 30)
                futures.append(future)
                progress.update(task, description=f"Started core {i+1}/{num_cores}")
            
            # Wait for all to complete
            results = []
            for i, future in enumerate(futures):
                result = future.result()
                results.append(result)
                progress.update(task, description=f"Core {i+1}/{num_cores} completed")
    
    end_time = time.time()
    
    console.print(f"✅ All cores completed in {end_time - start_time:.2f}s")
    console.print(f"🔥 Your CPU should be nice and hot! 🌡️")
    console.print(f"⚡ Total computation result: {sum(results):.2e}")

def run_memory_stress_test():
    """Memory allocation stress test"""
    console.print(Panel("💾 MEMORY STRESS TEST - RAM Usage", style="bold blue"))
    
    arrays = []
    total_gb = 0
    
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            task = progress.add_task("Allocating memory...", total=None)
            
            while total_gb < 8:  # Try to use 8GB of RAM
                # Allocate 100MB chunks
                size = 100 * 1024 * 1024 // 4  # 100MB of float32
                arr = np.random.randn(size).astype(np.float32)
                arrays.append(arr)
                
                total_gb += 0.1
                progress.update(task, description=f"Allocated {total_gb:.1f}GB of RAM")
                
                # Do some computation to keep memory active
                result = np.sum(arr ** 2)
                
            console.print(f"✅ Successfully allocated {total_gb:.1f}GB of RAM")
            console.print(f"💾 Memory is fully loaded!")
            
    except MemoryError:
        console.print(f"💥 Out of memory at {total_gb:.1f}GB!")
        console.print(f"🎯 Maximum RAM usage reached!")
    
    # Cleanup
    del arrays

def run_threading_stress_test():
    """Multi-threading stress test"""
    console.print(Panel("🧵 THREADING STRESS TEST - Context Switching", style="bold green"))
    
    def worker_thread(thread_id, duration=30):
        """Worker thread that does intensive computation"""
        start = time.time()
        count = 0
        while time.time() - start < duration:
            # Intensive computation
            result = sum(i**2 for i in range(1000))
            count += 1
        return thread_id, count
    
    num_threads = mp.cpu_count() * 4  # Oversubscribe for context switching stress
    console.print(f"🧵 Starting {num_threads} threads (4x CPU cores)")
    
    start_time = time.time()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
        console=console
    ) as progress:
        task = progress.add_task("Thread mayhem...", total=None)
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for i in range(num_threads):
                future = executor.submit(worker_thread, i, 20)
                futures.append(future)
                progress.update(task, description=f"Started thread {i+1}/{num_threads}")
            
            # Wait for completion
            results = []
            for i, future in enumerate(futures):
                thread_id, count = future.result()
                results.append(count)
                progress.update(task, description=f"Thread {i+1}/{num_threads} completed")
    
    end_time = time.time()
    total_operations = sum(results)
    
    console.print(f"✅ {num_threads} threads completed in {end_time - start_time:.2f}s")
    console.print(f"⚡ Total operations: {total_operations:,}")
    console.print(f"🔥 Context switching stress complete!")

def gpu_stress_alternatives():
    """Show alternative ways to stress the GPU"""
    console.print(Panel(
        "🚀 GPU STRESS ALTERNATIVES\n\n"
        "Since PyTorch can't use your RTX 5080 directly,\n"
        "here are other ways to stress your GPU:\n\n"
        "1. 🎮 Run a demanding game (Cyberpunk 2077, etc.)\n"
        "2. 🔥 Use gpu-burn: apt install gpu-burn && gpu-burn 60\n"
        "3. ⛏️ Mining stress test: t-rex or similar\n"
        "4. 🧪 CUDA samples: deviceQuery, bandwidthTest\n"
        "5. 🔥 FurMark GPU stress test\n"
        "6. 📊 Use nvidia-smi to monitor: watch -n 1 nvidia-smi\n\n"
        "Your RTX 5080 is beast - it just needs the right tools!",
        title="GPU Alternatives",
        style="bold yellow"
    ))

def main():
    """Run comprehensive system stress tests"""
    console.print(Panel.fit(
        "🔥 SYSTEM TORTURE TEST 🔥\n"
        "Since we can't stress the GPU, let's melt everything else!",
        style="bold red"
    ))
    
    # CPU stress test
    run_cpu_stress_test()
    console.print()
    
    # Memory stress test
    run_memory_stress_test()
    console.print()
    
    # Threading stress test
    run_threading_stress_test()
    console.print()
    
    # GPU alternatives
    gpu_stress_alternatives()
    
    console.print(Panel(
        "🎉 System Stress Test Complete!\n\n"
        "Your CPU should be running hot, RAM fully loaded,\n"
        "and the system scheduler working overtime!\n\n"
        "🌡️ Check your system temps - everything should be toasty!\n"
        "💻 Time to let your machine cool down...",
        title="Mission Accomplished!",
        style="bold green"
    ))

if __name__ == "__main__":
    main()