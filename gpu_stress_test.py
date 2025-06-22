#!/usr/bin/env python3
"""
RTX 5080 GPU Stress Test
Push your GPU to the limits with various AI workloads
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import time
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.table import Table
import gc

console = Console()

class GPUStressTester:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.gpu_name = torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU"
        self.max_memory = torch.cuda.get_device_properties(0).total_memory if torch.cuda.is_available() else 0
        
    def print_gpu_info(self):
        """Display GPU information"""
        if not torch.cuda.is_available():
            console.print("❌ CUDA not available - running on CPU")
            return
            
        props = torch.cuda.get_device_properties(0)
        
        table = Table(title="🚀 GPU Information")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("GPU Name", self.gpu_name)
        table.add_row("Total Memory", f"{props.total_memory / 1024**3:.1f} GB")
        table.add_row("Multiprocessors", str(props.multi_processor_count))
        table.add_row("CUDA Cores", str(props.multi_processor_count * 128))  # Estimate
        table.add_row("Memory Clock", f"{props.memory_clock_rate / 1000:.0f} MHz")
        table.add_row("Compute Capability", f"{props.major}.{props.minor}")
        
        console.print(table)
        
    def monitor_gpu_usage(self):
        """Monitor GPU memory and utilization"""
        if not torch.cuda.is_available():
            return "CPU Mode"
            
        allocated = torch.cuda.memory_allocated(0) / 1024**3
        reserved = torch.cuda.memory_reserved(0) / 1024**3
        total = self.max_memory / 1024**3
        
        return f"Memory: {allocated:.1f}GB allocated, {reserved:.1f}GB reserved, {total:.1f}GB total"
    
    def test_matrix_operations(self, size=8192, iterations=100):
        """Stress test with large matrix operations"""
        console.print(f"🔢 [bold cyan]Matrix Multiplication Test[/bold cyan] - Size: {size}x{size}")
        
        # Create large matrices
        A = torch.randn(size, size, device=self.device, dtype=torch.float32)
        B = torch.randn(size, size, device=self.device, dtype=torch.float32)
        
        console.print(f"📊 {self.monitor_gpu_usage()}")
        
        start_time = time.time()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            task = progress.add_task("Computing matrix multiplications...", total=iterations)
            
            for i in range(iterations):
                C = torch.matmul(A, B)
                # Add some complexity
                C = torch.relu(C)
                C = torch.softmax(C, dim=-1)
                
                if i % 10 == 0:
                    progress.update(task, advance=10)
                    
        end_time = time.time()
        
        # Calculate performance metrics
        operations = iterations * size * size * size * 2  # Multiply + accumulate
        gflops = operations / (end_time - start_time) / 1e9
        
        console.print(f"✅ Completed {iterations} matrix multiplications in {end_time - start_time:.2f}s")
        console.print(f"⚡ Performance: {gflops:.1f} GFLOPS")
        console.print(f"📊 {self.monitor_gpu_usage()}")
        
        del A, B, C
        torch.cuda.empty_cache()
        
        return gflops
    
    def test_convolution_networks(self, batch_size=64, iterations=50):
        """Stress test with deep CNN operations"""
        console.print(f"🧠 [bold cyan]CNN Stress Test[/bold cyan] - Batch: {batch_size}")
        
        # Create a deep CNN model
        class StressNet(nn.Module):
            def __init__(self):
                super().__init__()
                self.conv_layers = nn.ModuleList([
                    nn.Conv2d(3, 64, 3, padding=1),
                    nn.Conv2d(64, 128, 3, padding=1),
                    nn.Conv2d(128, 256, 3, padding=1),
                    nn.Conv2d(256, 512, 3, padding=1),
                    nn.Conv2d(512, 512, 3, padding=1),
                    nn.Conv2d(512, 256, 3, padding=1),
                ])
                self.pool = nn.MaxPool2d(2, 2)
                self.fc = nn.Linear(256 * 4 * 4, 1000)
                
            def forward(self, x):
                for conv in self.conv_layers:
                    x = F.relu(conv(x))
                    if x.size(2) > 4:  # Don't pool if too small
                        x = self.pool(x)
                x = x.view(x.size(0), -1)
                x = self.fc(x)
                return x
        
        model = StressNet().to(self.device)
        
        # Create input data (simulating high-res images)
        input_data = torch.randn(batch_size, 3, 224, 224, device=self.device)
        
        console.print(f"📊 {self.monitor_gpu_usage()}")
        
        start_time = time.time()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            task = progress.add_task("Running CNN forward passes...", total=iterations)
            
            for i in range(iterations):
                # Forward pass
                output = model(input_data)
                
                # Simulate backward pass workload
                loss = output.sum()
                loss.backward()
                
                # Clear gradients
                model.zero_grad()
                
                if i % 5 == 0:
                    progress.update(task, advance=5)
        
        end_time = time.time()
        
        images_per_sec = (iterations * batch_size) / (end_time - start_time)
        
        console.print(f"✅ Processed {iterations * batch_size} images in {end_time - start_time:.2f}s")
        console.print(f"⚡ Throughput: {images_per_sec:.1f} images/second")
        console.print(f"📊 {self.monitor_gpu_usage()}")
        
        del model, input_data, output
        torch.cuda.empty_cache()
        
        return images_per_sec
    
    def test_memory_bandwidth(self, size_gb=4):
        """Test memory bandwidth with large tensor operations"""
        console.print(f"💾 [bold cyan]Memory Bandwidth Test[/bold cyan] - {size_gb}GB tensors")
        
        # Calculate tensor size for desired GB
        elements = int(size_gb * 1024**3 / 4)  # 4 bytes per float32
        tensor_size = int(elements**0.5)  # Square tensor
        
        console.print(f"Creating {tensor_size}x{tensor_size} tensors...")
        
        A = torch.randn(tensor_size, tensor_size, device=self.device, dtype=torch.float32)
        B = torch.randn(tensor_size, tensor_size, device=self.device, dtype=torch.float32)
        
        console.print(f"📊 {self.monitor_gpu_usage()}")
        
        # Memory copy operations
        start_time = time.time()
        
        for i in range(20):
            C = A + B  # Memory bandwidth intensive
            D = C * 2.0
            E = torch.sin(D)  # Compute intensive
            F = E.transpose(0, 1)  # Memory layout change
            
        torch.cuda.synchronize()  # Wait for all operations
        end_time = time.time()
        
        # Calculate bandwidth
        bytes_moved = tensor_size * tensor_size * 4 * 20 * 4  # 4 operations, 4 bytes per float
        bandwidth_gb_s = bytes_moved / (end_time - start_time) / 1024**3
        
        console.print(f"✅ Memory operations completed in {end_time - start_time:.2f}s")
        console.print(f"⚡ Bandwidth: {bandwidth_gb_s:.1f} GB/s")
        console.print(f"📊 {self.monitor_gpu_usage()}")
        
        del A, B, C, D, E, F
        torch.cuda.empty_cache()
        
        return bandwidth_gb_s
    
    def test_transformer_attention(self, seq_len=2048, hidden_size=1024, iterations=30):
        """Stress test transformer attention mechanisms"""
        console.print(f"🔍 [bold cyan]Transformer Attention Test[/bold cyan] - Seq: {seq_len}, Hidden: {hidden_size}")
        
        # Create attention mechanism
        class MultiHeadAttention(nn.Module):
            def __init__(self, hidden_size, num_heads=16):
                super().__init__()
                self.num_heads = num_heads
                self.head_dim = hidden_size // num_heads
                self.scale = self.head_dim ** -0.5
                
                self.qkv = nn.Linear(hidden_size, hidden_size * 3)
                self.proj = nn.Linear(hidden_size, hidden_size)
                
            def forward(self, x):
                B, N, C = x.shape
                qkv = self.qkv(x).reshape(B, N, 3, self.num_heads, self.head_dim).permute(2, 0, 3, 1, 4)
                q, k, v = qkv[0], qkv[1], qkv[2]
                
                attn = (q @ k.transpose(-2, -1)) * self.scale
                attn = attn.softmax(dim=-1)
                
                x = (attn @ v).transpose(1, 2).reshape(B, N, C)
                x = self.proj(x)
                return x
        
        attention = MultiHeadAttention(hidden_size).to(self.device)
        input_tensor = torch.randn(8, seq_len, hidden_size, device=self.device)
        
        console.print(f"📊 {self.monitor_gpu_usage()}")
        
        start_time = time.time()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            task = progress.add_task("Computing attention...", total=iterations)
            
            for i in range(iterations):
                output = attention(input_tensor)
                
                # Simulate gradient computation
                loss = output.sum()
                loss.backward()
                attention.zero_grad()
                
                if i % 3 == 0:
                    progress.update(task, advance=3)
        
        end_time = time.time()
        
        tokens_per_sec = (iterations * 8 * seq_len) / (end_time - start_time)
        
        console.print(f"✅ Processed attention in {end_time - start_time:.2f}s")
        console.print(f"⚡ Throughput: {tokens_per_sec:.0f} tokens/second")
        console.print(f"📊 {self.monitor_gpu_usage()}")
        
        del attention, input_tensor, output
        torch.cuda.empty_cache()
        
        return tokens_per_sec
    
    def run_comprehensive_stress_test(self):
        """Run all stress tests"""
        console.print(Panel.fit(
            "🔥 RTX 5080 GPU STRESS TEST 🔥\n"
            "Pushing your GPU to the absolute limits!",
            style="bold red"
        ))
        
        self.print_gpu_info()
        console.print()
        
        results = {}
        
        try:
            # Test 1: Matrix Operations
            results['matrix_gflops'] = self.test_matrix_operations()
            console.print()
            
            # Test 2: CNN Operations  
            results['cnn_throughput'] = self.test_convolution_networks()
            console.print()
            
            # Test 3: Memory Bandwidth
            results['memory_bandwidth'] = self.test_memory_bandwidth()
            console.print()
            
            # Test 4: Transformer Attention
            results['attention_throughput'] = self.test_transformer_attention()
            console.print()
            
            # Final Results
            self.display_final_results(results)
            
        except RuntimeError as e:
            if "out of memory" in str(e):
                console.print("💥 [bold red]GPU Memory Exhausted![/bold red]")
                console.print("🎯 [bold yellow]Mission Accomplished - You've maxed out your RTX 5080![/bold yellow]")
            else:
                console.print(f"❌ Error: {e}")
        
        # Cleanup
        torch.cuda.empty_cache()
        gc.collect()
    
    def display_final_results(self, results):
        """Display comprehensive benchmark results"""
        table = Table(title="🏆 GPU Stress Test Results")
        table.add_column("Benchmark", style="cyan")
        table.add_column("Performance", style="green")
        table.add_column("Rating", style="yellow")
        
        # Matrix operations
        gflops = results.get('matrix_gflops', 0)
        if gflops > 20000:
            rating = "🔥 BEAST MODE"
        elif gflops > 10000:
            rating = "⚡ EXCELLENT"
        elif gflops > 5000:
            rating = "✅ GOOD"
        else:
            rating = "📈 WARMING UP"
        table.add_row("Matrix GFLOPS", f"{gflops:.1f}", rating)
        
        # CNN throughput
        cnn = results.get('cnn_throughput', 0)
        if cnn > 1000:
            rating = "🔥 BEAST MODE"
        elif cnn > 500:
            rating = "⚡ EXCELLENT"
        elif cnn > 200:
            rating = "✅ GOOD"
        else:
            rating = "📈 WARMING UP"
        table.add_row("CNN Images/sec", f"{cnn:.1f}", rating)
        
        # Memory bandwidth
        bandwidth = results.get('memory_bandwidth', 0)
        if bandwidth > 800:
            rating = "🔥 BEAST MODE"
        elif bandwidth > 600:
            rating = "⚡ EXCELLENT"
        elif bandwidth > 400:
            rating = "✅ GOOD"
        else:
            rating = "📈 WARMING UP"
        table.add_row("Memory GB/s", f"{bandwidth:.1f}", rating)
        
        # Attention throughput
        attention = results.get('attention_throughput', 0)
        if attention > 50000:
            rating = "🔥 BEAST MODE"
        elif attention > 30000:
            rating = "⚡ EXCELLENT"
        elif attention > 15000:
            rating = "✅ GOOD"
        else:
            rating = "📈 WARMING UP"
        table.add_row("Attention Tokens/s", f"{attention:.0f}", rating)
        
        console.print(table)
        
        console.print(Panel(
            f"🎯 [bold green]GPU Stress Test Complete![/bold green]\n\n"
            f"Your RTX 5080 has been thoroughly exercised!\n"
            f"Temperature should be nice and toasty right about now 🔥\n\n"
            f"📊 Final GPU Status: {self.monitor_gpu_usage()}",
            title="Mission Accomplished!"
        ))

def main():
    tester = GPUStressTester()
    tester.run_comprehensive_stress_test()

if __name__ == "__main__":
    main()