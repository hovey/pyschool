#!/bin/bash

# References: ruxi/make_conda_env.sh
# https://gist.github.com/ruxi/949e3d326c5a8a24ecffa8a225b2be2a 
#
# Google's best practices for shell script:
# https://google.github.io/styleguide/shellguide.html

# echo "Select an environment name (e.g., pyschoolenv):"
# read y
y='pyschoolenv' # the conda environment of interest

echo "This shell script (re)creates the conda environment"
echo "for use with Pyschool"
echo "modules:"
echo "  - pyschool"
echo "The name of the conda environment to be (re)created is:"
echo $y

echo "Verifying that conda is up-to-date:"
conda activate base
conda update --yes -n base -c defaults conda

echo "Current conda environments:"
conda env list

# remove existing environment, if it exists
echo "Should it already exist, this environment will be removed:" 
echo $y
conda env remove --name $y

echo "Conda environments after attempt at removal of old environment:"
conda env list

echo "(Re)creating the conda environment:"
echo $y

# pip install black==21.7b0 get the new blac, but conda default channel does not
# conda create --yes --name $y python=3.9 black=21.7b0 flake8 ipykernel matplotlib notebook pytest pytest-cov seaborn scikit-image scipy
# 2021-07-24 Install other libraries, e.g., black, from other channels, not conda
conda create --yes --name $y python=3.9

# echo Activating the new $y environment...
conda init bash
eval "$(conda shell.bash hook)"
conda activate $y

# black flake8 ipykernel matplotlib notebook pytest pytest-cov seaborn scikit-image scipy
# conda install --yes numpy
# conda install --yes -c conda-forge black
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

# echo "Using internal pip mirror"
# pip config --user set global.index https://nexus.web.sandia.gov/repository/pypi-proxy
# pip config --user set global.index-url https://nexus.web.sandia.gov/repository/pypi-proxy/simple

# 
echo "Upgrading pip"
python -m pip install --upgrade pip
#
echo "The pip listing prior to install:"
pip list
# 
echo "Installing the pyschool module in developer mode..."
cd ~/sibl/pyschool
pip install -e .
#
echo "The pip listing after install..."
pip list

echo "-----------------------------"
echo "The script has now completed."
echo "-----------------------------"

# You may need to use the following to install
# python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pyglet
