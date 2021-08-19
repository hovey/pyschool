#!/bin/bash

# reference: ruxi/make_conda_env.sh
# https://gist.github.com/ruxi/949e3d326c5a8a24ecffa8a225b2be2a 
echo This shell script recreates the development conda environment
echo for use with the zmath module.

# echo "Select an environment name (e.g., zmathenv):"
# read y
# y='zmath-env-dev' # the conda environment of interest
# echo Creating conda environment: $y

echo Verifying that conda is up-to-date:
# conda activate base
conda update -n base -c defaults conda

echo Current conda environments:
conda env list

# remove existing environment, if it exists
# echo Removing existing $y environment, should it exist...
# conda env remove --name $y
# echo Conda environments after attempt at removal of old environment:
# conda env list

# echo Recreating a new $y environment...
echo Creating environment...
# conda create --name $y python=3.8 black flake8 matplotlib pytest pytest-cov scipy
conda env create -f environment-dev.yml

# if [ `uname` == Linux ]; then
#     if [ "$PY_VER" == "2.7" ]; then
#         pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.6.0-cp27-none-linux_x86_64.whl
#     else
#         pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.6.0-cp34-none-linux_x86_64.whl
#     fi
# fi

# echo Activating the new $y environment...
echo Activating the new environment...
# conda init bash
# conda activate $y
#
# Can't execute `conda activate` from bash script #7980
# https://github.com/conda/conda/issues/7980
source /opt/miniconda3/etc/profile.d/conda.sh
conda activate zmathenv-dev
# 
echo Finally, some pip items...
echo The pip listing prior to install...
pip list
# 
echo Installing the zmath module in developer mode...
pip install -e .
# 
echo The pip listing after install...
pip list

echo -----------------------------------------------
echo The shell script setup.sh and is now completed.
echo -----------------------------------------------
