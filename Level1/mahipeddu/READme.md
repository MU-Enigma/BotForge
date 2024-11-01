# Text Generation WebUI Setup Guide for AMD ROCm

This guide will help you set up Text Generation WebUI with ROCm support for AMD GPUs.

## Prerequisites

- AMD GPU with ROCm support (RDNA2 or newer architecture recommended)
- Ubuntu 22.04 or newer (recommended for best ROCm support)
- Python 3.10 or newer
- At least 16GB system RAM
- Sufficient GPU VRAM for your chosen model

## 1. Install ROCm

```bash

wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update


sudo apt install rocm-dev
```

Add your user to the render and video groups:
```bash
sudo usermod -a -G render $USER
sudo usermod -a -G video $USER
```

## 2. Set up Python Environment

```bash
sudo apt install python3-pip python3-venv


python3 -m venv textgen-env
source textgen-env/bin/activate
```

## 3. Install Text Generation WebUI

```bash
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui

pip install -r requirements.txt

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.6
```

## 4. Configure for ROCm

Create a `config.json` in the repository root:

```json
{
    "loader": "ExLlama",
    "gpu_memory_allocation": "99%",
    "rope_scaling": {
        "type": "dynamic",
        "factor": 2.0
    }
}
```

## 5. Download Model

```bash
# Create models directory
mkdir models
cd models

# Download your chosen model (example using TheBloke's Mistral)
python3 -m huggingface_hub download TheBloke/Mistral-7B-v0.1-GGUF --filename mistral-7b-v0.1.Q4_K_M.gguf
```


- [Text Generation WebUI GitHub](https://github.com/oobabooga/text-generation-webui)
- [ROCm Documentation](https://rocmdocs.amd.com/en/latest/)
- [HuggingFace Models](https://huggingface.co/models)
