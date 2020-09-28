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
(base) $ conda env list
```

Create the virtual environment:

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

## Overview of Git Branching

Show available branches:

```bash
(zmathenv) [apollo ~/pyschool]$ git branch
* master
```

The branch with an asterisk ("`*`") is the current branch.

Create a new branch called `dev-branch-typo`, which will be a development branch, 
and a typographical error (we show this to demonstrate how to delete a branch too), 
then list all the branches again:

```bash
(zmathenv) [apollo ~/pyschool]$ git branch
  dev-branch-typo
* master
```

Notice the `*` remained on `master` since we only *created* the `dev-branch-typo`
branch but did not check it out. 

Delete the errant branch and confirm it has been deleted.  

* The `-d` is git's safe delete, which prevents you from deleting 
a branch if it has unmerged changes.  
* Alternatively, the use of `-D` will force deletion of the specified branch, even if 
unmerged changes exist.  The `-D` is useful in the case when the developer wants 
to discard all commits on a particular branch.

```bash
(zmathenv) [apollo ~/pyschool]$ git branch -d dev-branch-typo
Deleted branch dev-branch-typo (was 186cfb4).
(zmathenv) [apollo ~/pyschool]$ git branch
* master
```

In practice, you will use the following *Branch Workflow*:

* Create a new development branch
* Develop and test the code
* Merge the development branch into the main code base
* Delete the development branch

Below is an example of that workflow on a tiny piece of code.

## Branch Workflow

```bash
(zmathenv) [apollo ~/pyschool]$ git branch dev-branch-test
(zmathenv) [apollo ~/pyschool]$ git branch
  dev-branch-test
* master
(zmathenv) [apollo ~/pyschool]$ git pull
Already up-to-date.
```


## Next: [Dev](dev.md)
