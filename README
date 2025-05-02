## CSU Chemistry Theory Group Masterclass: Artificial Neural Networks
#### Sabari Kumar, 20250502

This repo is meant to be a template/guide to creating simple ANN models using pytorch.  
Also present is boilerplate config for pre-commit and a pyproject.toml file.  
  
To install:
Fork, then `git clone` the repo.
Run `pip install -e .` to install as an editable package.  

This project structure is loosely based on [CCDS](https://cookiecutter-data-science.drivendata.org/).  
Directory structure:
- data: Data files, code to process them into model inputs and load them. Data processing workflows should be set up here as scripts that act on files from `raw`, and write to `processed`. No bulk data processing in jupyter notebooks!
   - raw: Raw data files. These should be treated as read-only.
   - processed: Processed input data, ready to feed into a model
- model: Files associated with model structure, such as layers, model definitions, etc.
- runtime: Scripts used to run model training and inference, such as python training scripts, slurm batch scripts, etc.
- sandbox: Exploratory/prototyping code. Jupyter notebooks should live here.
- results: Model logs and checkpoint files.
