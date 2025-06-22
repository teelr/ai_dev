#!/usr/bin/env python3
"""
Simple GPU Stress Test for RTX 5080
Push your GPU hard with matrix operations
"""

import torch
import time
import gc
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

console = Console()

def gpu_info():
    """Display basic GPU info"""
    if not torch.cuda.is_available():
        console.print("❌ CUDA not available")
        return False
    
    gpu_name = torch.cuda.get_device_name(0)
    total_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
    
    console.print(f"🚀 GPU: {gpu_name}")
    console.print(f"💾 Memory: {total_memory:.1f} GB")
    return True

def monitor_memory():
    """Show current GPU memory usage"""
    if not torch.cuda.is_available():
        return "CPU Mode"
    
    allocated = torch.cuda.memory_allocated(0) / 1024**3
    reserved = torch.cuda.memory_reserved(0) / 1024**3
    total = torch.cuda.get_device_properties(0).total_memory / 1024**3
    
    return f"GPU Memory: {allocated:.1f}GB used / {total:.1f}GB total"

def stress_test_matrices():
    """Stress test with progressively larger matrices"""
    console.print(Panel("🔥 GPU STRESS TEST - Matrix Operations", style="bold red"))
    
    if not gpu_info():
        return
    
    device = torch.device('cuda')
    sizes = [2048, 4096, 6144, 8192, 10240, 12288]
    
    for size in sizes:
        console.print(f"\n🔢 Testing {size}x{size} matrices...")
        console.print(f"📊 {monitor_memory()}")
        
        try:
            # Create large matrices
            A = torch.randn(size, size, device=device, dtype=torch.float32)
            B = torch.randn(size, size, device=device, dtype=torch.float32)
            
            console.print(f"📊 After allocation: {monitor_memory()}")
            
            # Time the computation
            torch.cuda.synchronize()
            start_time = time.time()
            
            # Intensive computation
            for i in range(10):
                C = torch.matmul(A, B)
                C = torch.relu(C)
                C = torch.softmax(C, dim=-1)
                
                if i % 3 == 0:
                    console.print(f"  Iteration {i+1}/10...")
            
            torch.cuda.synchronize()
            end_time = time.time()
            
            # Calculate performance
            total_ops = 10 * size * size * size * 2  # matmul operations
            gflops = total_ops / (end_time - start_time) / 1e9
            
            console.print(f"✅ Completed in {end_time - start_time:.2f}s")
            console.print(f"⚡ Performance: {gflops:.1f} GFLOPS")
            console.print(f"🌡️ GPU getting toasty! 🔥")
            
            # Cleanup
            del A, B, C
            torch.cuda.empty_cache()
            
        except RuntimeError as e:
            if "out of memory" in str(e):
                console.print(f"💥 GPU Memory Exhausted at {size}x{size}!")
                console.print(f"🎯 Maximum matrix size found: {sizes[sizes.index(size)-1] if sizes.index(size) > 0 else 'N/A'}")
                break
            else:
                console.print(f"❌ Error: {e}")
                break

def stress_test_sustained():
    """Sustained load test"""
    console.print(Panel("⚡ SUSTAINED LOAD TEST - 60 seconds", style="bold yellow"))
    
    if not torch.cuda.is_available():
        return
    
    device = torch.device('cuda')
    
    # Find a good size that doesn't crash
    size = 4096
    console.print(f"🔥 Running sustained {size}x{size} operations for 60 seconds...")
    
    try:
        A = torch.randn(size, size, device=device)
        B = torch.randn(size, size, device=device)
        
        start_time = time.time()
        iteration = 0
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            task = progress.add_task("Melting your GPU...", total=None)
            
            while time.time() - start_time < 60:  # Run for 60 seconds
                C = torch.matmul(A, B)
                C = torch.relu(C + 0.1)
                B = C  # Keep memory hot
                iteration += 1
                
                if iteration % 10 == 0:
                    progress.update(task, description=f"Iteration {iteration} - {monitor_memory()}")
        
        end_time = time.time()
        ops_per_sec = iteration / (end_time - start_time)
        
        console.print(f"🔥 Completed {iteration} operations in {end_time - start_time:.1f}s")
        console.print(f"⚡ Rate: {ops_per_sec:.1f} operations/second")
        console.print(f"🌡️ Your GPU should be VERY warm now! 🔥🔥🔥")
        
        del A, B, C
        torch.cuda.empty_cache()
        
    except Exception as e:
        console.print(f"❌ Error during sustained test: {e}")

def stress_test_memory_fill():
    """Try to fill GPU memory completely"""
    console.print(Panel("💾 MEMORY FILL TEST - Use all GPU RAM", style="bold blue"))
    
    if not torch.cuda.is_available():
        return
    
    device = torch.device('cuda')
    tensors = []
    
    try:
        # Start with smaller chunks and grow
        chunk_size = 1024
        
        while True:
            console.print(f"📊 {monitor_memory()}")
            console.print(f"Allocating {chunk_size}x{chunk_size} tensor...")
            
            tensor = torch.randn(chunk_size, chunk_size, device=device)
            tensors.append(tensor)
            
            # Do some computation to keep GPU busy
            result = torch.matmul(tensor, tensor.T)
            result = torch.softmax(result, dim=-1)
            
            # Increase size for next iteration
            chunk_size += 512
            
    except RuntimeError as e:
        if "out of memory" in str(e):
            console.print(f"💥 GPU Memory Completely Filled!")
            console.print(f"📊 Final state: {monitor_memory()}")
            console.print(f"🎯 Allocated {len(tensors)} tensors before running out of memory")
            console.print(f"🔥 YOUR RTX 5080 IS MAXED OUT! 🔥")
        else:
            console.print(f"❌ Error: {e}")
    
    # Cleanup
    del tensors
    torch.cuda.empty_cache()
    gc.collect()

def main():
    """Run all GPU stress tests"""
    console.print(Panel.fit(
        "🚀 RTX 5080 GPU TORTURE TEST 🚀\n"
        "Time to make that GPU sweat!",
        style="bold green"
    ))
    
    # Test 1: Progressive matrix sizes
    stress_test_matrices()
    
    # Clean up between tests
    torch.cuda.empty_cache()
    time.sleep(2)
    
    # Test 2: Sustained load
    stress_test_sustained() 
    
    # Clean up between tests
    torch.cuda.empty_cache()
    time.sleep(2)
    
    # Test 3: Memory fill
    stress_test_memory_fill()
    
    console.print(Panel(
        "🎉 GPU Stress Test Complete!\n\n"
        "Your RTX 5080 has been thoroughly exercised.\n"
        "Check your GPU temps - they should be quite toasty! 🔥\n\n"
        "Time to let that beast cool down...",
        title="Mission Accomplished!",
        style="bold green"
    ))

if __name__ == "__main__":
    main()