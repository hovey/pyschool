#!/bin/bash
# Setup script
# Requires miniconda (preferred), or anaconda

# Set up git flow
# git flow init

# Check that conda is installed
echo "Checking for conda"
CONDA_INSTALLED=$(which conda)
if [ "" = "$CONDA_INSTALLED" ]; then
    echo "Conda is not installed. Exiting script"
    exit
else
    echo "Conda is installed! Continuing installation"
fi

# Creating new conda environment
conda update --yes -n base -c defaults conda
conda create --yes -n pyschool-env python=3.8
eval "$(conda shell.bash hook)"
conda activate pyschool-env

bash install_packages.sh

## Install packages
echo "Installing pyschool library as a developer"
pip install -e .

echo "setup.sh installation script is now completed."

