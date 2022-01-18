#!/bin/bash

# TODO: Use this script with Continuous Integration, thus W.E.T. -> D.R.Y.

# References: ruxi/make_conda_env.sh
# https://gist.github.com/ruxi/949e3d326c5a8a24ecffa8a225b2be2a 
#
# Google's best practices for shell script:
# https://google.github.io/styleguide/shellguide.html

# echo "Select an environment name (e.g., pyschoolenv):"
# read environ
environ='pyschoolenv' # the conda environment of interest

echo "This shell script (re)creates the conda environment"
echo "for use with Pyschool module:"
echo "  - pyschool"
echo "The name of the conda environment to be (re)created is:"
echo $environ

echo "Verifying that conda is up-to-date:"
conda activate base
conda update --yes -n base -c defaults conda

# remove existing environment, if it exists
echo "Should it already exist, this environment will be removed:" 
echo $environ
conda env remove --name $environ
echo "(Re)creating the conda environment:"
conda create --yes --name $environ

conda init bash
eval "$(conda shell.bash hook)"
conda activate $environ

conda install --yes python=3.9
conda install --yes numpy
conda install --yes -c conda-forge black=21.7b0
conda install --yes -c anaconda flake8
conda install --yes -c anaconda ipykernel
conda install --yes -c anaconda matplotlib
conda install --yes -c anaconda notebook
conda install --yes -c anaconda pytest
conda install --yes -c anaconda pytest-cov
conda install --yes -c anaconda seaborn
conda install --yes -c anaconda scikit-image
conda install --yes -c anaconda scipy
conda install --yes -c anaconda flask

echo "Upgrading pip"
python -m pip install --upgrade pip
python -m pip install pyyaml
python -m pip install pytest-bdd
python -m pip install invoke
#

echo "Installing the pyschool module in developer mode..."
cd ~/pyschool
pip install -e .
#

echo "-----------------------------------"
echo "The shell script has now completed."
echo "-----------------------------------"

# You may need to use the following to install
# python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pyglet
