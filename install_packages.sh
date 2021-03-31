#!/bin/bash
# Packages to install via conda or pip
# Requires miniconda (preferred), or anaconda

# Install packages
echo "Installing conda packages"
conda install --yes numpy
conda install --yes -c conda-forge black
conda install --yes -c anaconda pytest
conda install --yes -c anaconda pytest-cov
conda install --yes -c anaconda flake8
conda install --yes -c anaconda matplotlib

echo "Installing pip packages"
# python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org sacred
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org torchtest
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pyglet

