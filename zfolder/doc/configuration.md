# Configuration

## Previous: [Learn](learn.md)

## Set up local development environment

* Install [Visual Studio Code](https://code.visualstudio.com/)
* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* Create a virtual environment called `zmathenv` and then activate that newly-created environment:

### Virtual Environment

A virtual environment ensures you will have all the necessary modules required to run the workflow, and that
the modules installed are compatable with each other.  First, check to make sure you don't already have a
virtual environment called `zmathenv` 

```bash
conda env list
```

Next, create the virtual environment:

```bash 
(base) $ conda create --name zmathenv python=3.8 numpy matplotlib pytest pytest-cov flake8 black pylint
(base) $ conda activate zmathenv
(zmathenv) $
```

* [Connect](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh) to GitHub with ssh.
* Clone the repo:

```bash
(zmathenv) $ git@github.com:hovey/pyschool.git
```

* Install the existing `zmath` library in developer mode:

```bash
(zmathenv) $ cd ~/pyschool
(zmathenv) $ # to come, ask Anirudh on this step.
```

## Check out the master branch repository

To come.

## Next: [Dev](dev.md)
