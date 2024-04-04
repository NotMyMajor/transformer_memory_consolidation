## Introduction

This is a fork of "transformer_memory_consolidation" from the paper "Transformer as a hippocampal memory consolidation model based on NMDAR-inspired nonlinearity". This is for a student project at the University of Texas at Dallas. Runs were performed on Windows systems with RTX 3080 or 3070 GPUs or on Apple Silicon with an M1 Pro.

---
## (Original Introduction)

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


## GPU activation with CUDA

The provided installation instructions do not appear to install CUDA automatically, which is recommended for using PyTorch with a NVIDIA GPU on a Windows machine. If `torch.device()` does not detect the GPU, it will default to using the CPU, drastically increasing training time. Installing PyTorch and this project's dependencies individually solved this issue. 

PyTorch installation instructions are available [here](https://pytorch.org/get-started/locally/).

After installing PyTorch with CUDA support, ensure that the GPU is detected from the command line. Useful commands are mentioned [here](https://stackoverflow.com/questions/48152674/how-do-i-check-if-pytorch-is-using-the-gpu).

- Open a Python interpreter
`python3`  
&nbsp;
- Import PyTorch
`import torch`   
&nbsp;
- Check that CUDA is available
  `torch.cuda.is_available()`  
&nbsp;
- Check for GPUs
`torch.cuda.device_count()`  
&nbsp;
- Get GPU device location
`torch.cuda.device(0)`  
&nbsp;
- Get GPU name
`torch.cuda.get_device_name(0)`  

## Exporting WandB Run History
There is now an export_excel.py script to make exporting the WandB run history easier.
Keep in mind that this is a quick and dirty script made to make the process slightly easier. It has some basic input checking to try to make sure you can't mess it up too bad, but use with some caution.

You may need to install tkinter if you don't have it already.
```bash
python -m pip install tkinter
```

To use the script:
* Open the run on WandB
* Go to Overview
* Click the "..." in the top right
* Select "Export Data". Copy the path from the line "run = api.run("/COPY/THIS/PATH")". Just the path without the ""
* Open the terminal and navigate to the folder with the script 
```bash
python export_excel.py
```
Follow the instructions in the terminal to paste the WandB run name/path from the WandB website and choose a save path and filename for the output spreadsheet.

If you still want to export the WandB run manually, the instructions are below.

## Exporting WandB Run History Manually
To export the WandB run history after a run is complete:
* Open the run on WandB
* Go to Overview
* Click the "..." in the top right
* Select "Export Data". Copy the line "run = api.run("YOUR_RUN_NAME_HERE")"
* Open up a terminal and follow the steps below, substituting the line you copied where it says "run = api.run("YOUR_RUN_NAME_HERE")".
* Change "/Output/Path/Here/OutputName.xlsx" to the path and filename you want to save the spreadsheet.

(The first time I tried this, pandas gave an error due to a missing dependency that didn't get installed. Just pip install that missing dependency and try again.)

```bash
pip install pandas
python
```
```bash
>>> import wandb
>>> import pandas
>>> api = wandb.Api()
>>> run = api.run("YOUR_RUN_NAME_HERE")
>>> history = run.history(pandas=True)
>>> history.to_excel(r"/Output/Path/Here/OutputName.xlsx")
```
