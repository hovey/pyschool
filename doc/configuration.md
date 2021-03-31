# Configuration

## Previous: [Learn](learn.md)

To set up your local development environment, *install* and 
possibly *configure* the the dev tools below.

## Git

### Existing Installation

Check the existing install version

```bash
$ git --version
git version 2.6.4
```

If your version is sufficiently old compared to the current version, consider updating your Git.  On Linux, to install or upgrade:

```bash
sudo apt-get install git
```

On a new installer file for
* [Mac](https://git-scm.com/download/mac)
* [PC](https://git-scm.com/download/win) e.g., `Git-2.28.0-64-bit.exe`

### New Installation

Download the [installer](https://git-scm.com/).

If not yet configured, your username and email are set as follows
and are used set for commit transactions:

```bash
$ git config --global user.name "your-name-here" (e.g., "James Bond")
$ git config --global user.email "your-email@example.com" (e.g., "bond@gmail.com")
$ git config --global color.ui auto  # colorize the command line interface 
```

To edit these items in the future, directly update the `~/.gitconfig` file.

* [Connect](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh) local to GitHub repo via ssh.
* Clone the repo to local:

```bash
$ git clone git@github.com:hovey/pyschool.git
```

## Miniconda

* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Verify the version number and install location:

```bash
$ python --version 
Python 3.8.3

$ which python
/c/Users/chovey/Miniconda3/python
```

Verify conda is up-to-date:

```bash
(base) $ conda update -n base -c defaults conda
```

*Note:* If you are using the Git Bash shell, you may need to 

```bash
(base) $ conda init bash
```

then close and reopen the Git Bash shell for conda commands to work.


### Virtual Environment Configuration

A virtual environment ensures you will have all the necessary modules required to run the workflow, and that
the modules installed are compatable with each other.

To see the current conda environments:

```bash
(base) $ conda env list
```

Follow the [developer client](deployment.md#developer-client) instructions.

## VS Code

* [Visual Studio Code](https://code.visualstudio.com/)
* [Black integration with vim](https://black.readthedocs.io/en/stable/editor_integration.html#vim)

## To Branch or Not to Branch?

There are two main Git [workflows](https://www.atlassian.com/git/tutorials/comparing-workflows):

* A [Centralized Repository Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows#centralized-workflow)
* A [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)

For now, we maintain a Centralized Workflow, but keep [notes](branching.md) for event Branching Workflows in the future.

## Next: [Dev](dev.md)
