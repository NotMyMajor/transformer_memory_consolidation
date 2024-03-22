
---
## Introduction

This code is for the runs in our work, "Transformer as a hippocampal memory consolidation model based on NMDAR-inspired nonlinearity". In our work, all runs are performed on a single
NVIDIA TITAN V GPU.

## Installation

Supported platforms: MacOS and Ubuntu, Python 3.8

Installation using [Miniconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/index.html):

```bash
conda create -y --name nmda python=3.8
conda activate nmda
pip install -r requirements.txt
```

## Usage

```bash
python main.py --run_dir ./runs --group_name nmda_experiments --alpha 0.1 --num_envs 32 --log_to_wandb
```
* `alpha` is the parameter for the $\text{NMDA}_\alpha$ activation function we used in our experiment.
* `num_envs` is the number of training maps ($N$ in our paper).


## Apple Silicon Installation
You can run the model training on Apple Silicon metal acceleration using the version found in the MacSilicon folder. Follow the steps below to get it up and running.

```bash
conda create -y --name nmda python=3.8
conda activate nmda
conda install pytorch torchvision torchaudio -c pytorch-nightly 
pip install -r requirements.txt
pip install wandb tqdm transformers
```
* `pip install -r requiremments.txt` will likely fail. Run it, let it fail, run the other pip install commands then try the main.py located in the MacSilicon folder. You may need to install a RUST compiler. See this [thread](https://github.com/huggingface/tokenizers/issues/1050) for help.
