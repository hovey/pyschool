# Configuration

## Previous: [Learn](learn.md)

To set up your local development environment, *install* and 
then *configure* the the dev tools below.

## Installation

* Install [Git](https://git-scm.com/)
* Install [Visual Studio Code](https://code.visualstudio.com/)
* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* Create a virtual environment called `zmathenv` and then activate that newly-created environment:

## Configuration

### Git Configuration

If not yet configured, your username and email are set as follows
and are used set for commit transactions:

```bash
(base) $ git config --global user.name "your-name-here"
(base) $ git config --global user.email "your-email@example.com"  
(base) $ git config --global color.ui auto  # colorize the command line interface 
```

* [Connect](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh) local to GitHub repo via ssh.
* Clone the repo to local:

```bash
(base) $ git@github.com:hovey/pyschool.git
```

### Virtual Environment Configuration

A virtual environment ensures you will have all the necessary modules required to run the workflow, and that
the modules installed are compatable with each other.  First, check to make sure you don't already have a
virtual environment called `zmathenv` 

```bash
(base) $ conda env list
```

Create the virtual environment:

```bash 
(base) $ conda create --name zmathenv python=3.8 numpy matplotlib pytest pytest-cov flake8 black pylint
(base) $ conda activate zmathenv
(zmathenv) $
```

* Install the existing `zmath` library in developer mode:

```bash
(zmathenv) $ cd ~/pyschool
(zmathenv) $ # to come, ask Anirudh on this step.
```

### To Branch or Not to Branch?

There are two main Git [workflows](https://www.atlassian.com/git/tutorials/comparing-workflows):

* A [Centralized Repository Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows#centralized-workflow)
* A [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)

For now, we maintain a Centralized Workflow, but keep [notes](branching.md) for event Branching Workflows in the future.

## Next: [Dev](dev.md)
