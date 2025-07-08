# 🎮 RTX 5080 GPU Setup Guide

## 🚀 NVIDIA Driver & CUDA Setup

### 1. Check Current Status
```bash
# Check NVIDIA driver
nvidia-smi

# Check CUDA version
nvcc --version

# Check GPU availability in Python
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
python -c "import torch; print(f'GPU: {torch.cuda.get_device_name(0)}')"
```

### 2. Install/Update NVIDIA Drivers

#### Option A: Ubuntu Package Manager (Recommended)
```bash
# Update package list
sudo apt update

# Install NVIDIA driver (for RTX 5080, use 545+ series)
sudo apt install nvidia-driver-545

# Reboot
sudo reboot

# Verify after reboot
nvidia-smi
```

#### Option B: NVIDIA Official Installer
```bash
# Download latest driver
wget https://us.download.nvidia.com/XFree86/Linux-x86_64/545.29.06/NVIDIA-Linux-x86_64-545.29.06.run

# Make executable
chmod +x NVIDIA-Linux-x86_64-545.29.06.run

# Install (follow prompts)
sudo ./NVIDIA-Linux-x86_64-545.29.06.run
```

### 3. CUDA Toolkit Installation

The conda environment already includes CUDA toolkit, but for system-wide:

```bash
# Add NVIDIA package repository
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update

# Install CUDA 12.1
sudo apt install cuda-12-1

# Add to PATH
echo 'export PATH=/usr/local/cuda-12.1/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

## 🐍 Python Environment GPU Support

### Activate Environment & Test
```bash
# Activate conda environment
conda activate ai-dev

# Test PyTorch GPU
python -c "
import torch
print(f'PyTorch version: {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
print(f'CUDA version: {torch.version.cuda}')
print(f'GPU count: {torch.cuda.device_count()}')
print(f'Current GPU: {torch.cuda.get_device_name(0)}')
print(f'Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB')
"
```

### Monitor GPU Usage
```bash
# Real-time monitoring
watch -n 1 nvidia-smi

# Or use gpustat (prettier output)
gpustat -i 1

# In Python
python -c "
import GPUtil
GPUs = GPUtil.getGPUs()
for gpu in GPUs:
    print(f'GPU {gpu.id}: {gpu.name}')
    print(f'Memory: {gpu.memoryUsed}/{gpu.memoryTotal} MB')
    print(f'Utilization: {gpu.load*100}%')
"
```

## 🔧 Optimization for AI Workloads

### 1. PyTorch Settings
```python
# Enable TF32 for better performance on RTX 5080
import torch
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

# Set memory growth
torch.cuda.empty_cache()
torch.cuda.set_per_process_memory_fraction(0.8)  # Use 80% of GPU memory
```

### 2. Environment Variables
Add to `~/.bashrc`:
```bash
# CUDA optimizations
export CUDA_VISIBLE_DEVICES=0
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512

# cuDNN optimizations
export CUDNN_BENCHMARK=1

# Tensor Core usage
export TORCH_ALLOW_TF32_CUBLAS_OVERRIDE=1
```

### 3. Model Loading Optimizations
```python
# Load models directly to GPU
model = AutoModel.from_pretrained("model-name").to("cuda")

# Use mixed precision for faster inference
from torch.cuda.amp import autocast
with autocast():
    output = model(input_ids)

# Compile models (PyTorch 2.0+)
compiled_model = torch.compile(model)
```

## 🧪 Benchmarking Script

Create `test_gpu.py`:
```python
import torch
import time
import numpy as np

def benchmark_gpu():
    """Test GPU performance with matrix operations"""
    
    # Check GPU
    if not torch.cuda.is_available():
        print("No GPU available!")
        return
    
    print(f"Using GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    
    # Matrix multiplication benchmark
    sizes = [1024, 2048, 4096, 8192]
    
    for size in sizes:
        # Create random matrices
        a = torch.randn(size, size, device='cuda')
        b = torch.randn(size, size, device='cuda')
        
        # Warmup
        for _ in range(3):
            c = torch.matmul(a, b)
        
        torch.cuda.synchronize()
        
        # Benchmark
        start = time.time()
        for _ in range(10):
            c = torch.matmul(a, b)
        torch.cuda.synchronize()
        end = time.time()
        
        avg_time = (end - start) / 10
        tflops = (2 * size**3) / (avg_time * 1e12)
        
        print(f"Matrix size: {size}x{size}")
        print(f"Average time: {avg_time*1000:.2f} ms")
        print(f"Performance: {tflops:.2f} TFLOPS")
        print()

if __name__ == "__main__":
    benchmark_gpu()
```

Run with:
```bash
python test_gpu.py
```

## 🎯 AI Model Optimization

### For LLMs
```python
# Use Flash Attention 2 (if supported)
model = AutoModelForCausalLM.from_pretrained(
    "model-name",
    torch_dtype=torch.float16,
    use_flash_attention_2=True
).to("cuda")

# Quantization for larger models
from transformers import BitsAndBytesConfig
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)
```

### For Embeddings
```python
# Batch processing for efficiency
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('model-name', device='cuda')
model.max_seq_length = 512

# Process in batches
embeddings = model.encode(
    sentences,
    batch_size=32,
    normalize_embeddings=True,
    show_progress_bar=True
)
```

## 🚨 Troubleshooting

### CUDA Out of Memory
```python
# Clear cache
torch.cuda.empty_cache()

# Reduce batch size
batch_size = 16  # Instead of 32

# Use gradient checkpointing
model.gradient_checkpointing_enable()
```

### Driver Issues
```bash
# Check for conflicts
sudo apt list --installed | grep nvidia

# Remove old drivers
sudo apt remove --purge nvidia-*

# Reinstall
sudo apt install nvidia-driver-545
```

### Performance Issues
```bash
# Check power mode
nvidia-smi -q -d PERFORMANCE

# Set to maximum performance
sudo nvidia-smi -pm 1
sudo nvidia-smi -pl 350  # Set power limit (watts)
```

## 📊 Monitoring Tools

1. **nvidia-smi**: Built-in monitoring
2. **gpustat**: Pretty terminal output
3. **nvtop**: Interactive GPU process viewer
4. **tensorboard**: Training metrics

```bash
# Install monitoring tools
pip install gpustat nvitop
sudo apt install nvtop

# Run nvtop
nvtop
```

---

Your RTX 5080 is now fully configured for AI development with optimized drivers, CUDA support, and monitoring tools!