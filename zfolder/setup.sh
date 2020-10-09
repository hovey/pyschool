#!/bin/bash
y='zmathenv' # the conda environment of interest
echo This is setup.sh, shell script to recreate the conda environment: $y

echo Verifying that conda is up-to-date:
conda update -n base -c defaults conda

echo Current conda environments:
conda env list

# remove existing environment, if it exists
echo Removing existing $y environment, should it exist...
conda env remove --name $y
echo Conda environments after attempt at removal of old environment:
conda env list

echo Recreating a new $y environment...
conda create --name $y python=3.8 black flake8 matplotlib pytest pytest-cov scipy

echo Activating the new $y environment...
conda init bash
conda activate $y

echo Finally, some pip items...
echo The pip listing prior to install...
pip list

echo Installing the zmath module in developer mode...
pip install -e .

echo The pip listing after install...
pip list

echo -----------------------------------------------
echo The shell script setup.sh and is now completed.
echo -----------------------------------------------
