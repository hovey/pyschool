# Dev

## Set up local development environment

* Install [Visual Studio Code](https://code.visualstudio.com/)
* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* Create a virtual environment called `zmathenv` and then activate that newly-created environment:

```bash 
(base) $ conda create --name zmathenv python=3.8 pytest flake8 black
(base) $ conda activate zmathenv
(zmathenv) $
```

* Register ssh keys between local and repository.
* Clone the repo

```bash
(zmathenv) $ git@github.com:hovey/pyschool.git
```

* Install the existing `zmath` library in developer mode:

```bash
(zmathenv) $ cd ~/pyschool
(zmathenv) $
(zmathenv) $
```

| Previous |  Next |
|----------|------:|
| [learn](learn.md) | [propose](propose.md) | 