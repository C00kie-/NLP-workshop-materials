#!/bin/bash

ENV_NAME=$1
PYTHON_VERSION=$2

# Create a new environment with the specified name and installs Python $PYTHON_VERSION
conda create --name $ENV_NAME python=$PYTHON_VERSION

# Install Jupyter Lab and Notebook in the created environment.
conda install -c conda-forge jupyterlab notebook

# Install IPython Kernel in the created environment.
conda install ipykernel

# Create a new kernel for the specified environment and displays it as "Python ($ENV_NAME)".
python -m ipykernel install --user --name $ENV_NAME --display-name "Python ($ENV_NAME)"

# Start Jupyter Lab, serving notebooks from the local directory.
jupyter lab
