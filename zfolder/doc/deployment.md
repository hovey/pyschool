# Deployment

## Deployment Server

```bash
# -----------------
# deployment server
# -----------------
# verify conda is up-to-date
(base) $ conda update -n base -c defaults conda
(base) $ conda create --name deploy python=3.8 

# (base) $ conda activate zmathenv # environment previously created via ~/pyschool/zfolder/env_create.sh
(base) $ conda activate deploy

# update environment if necessary
# (zmathenv) $ python -m pip install --user --upgrade setuptools wheel
# (zmathenv) $ python -m pip install --user --upgrade twine
(deploy) $ python -m pip install --user --upgrade setuptools wheel
(deploy) $ python -m pip install --user --upgrade twine

(deploy) $ cd ~/pyschool/zfolder

# delete prior deployments
(deploy) $ rm -r build/ # if it exists, if not, skip this step
(deploy) $ rm -r dist/ # if it exists, if not, skip this step
(deploy) $ rm -r zmath.egg-info/ # if it exists, if not, skip this step

(deploy) $ vim setup.py   # update setup.py, typically increment the version, version is here and possibly in the README.md

# build to the dist/ subdirectory
(deploy) $ python setup.py sdist bdist_wheel

# assure the PyPI API token for the server is created on pypi.org and saved on the server at ~/.pypirc
# deploy
(deploy) $ python -m twine upload dist/*

# end of deployment, now test a developer client or production client
(deploy) $ conda deactivate
(base) $
```

## Development Client

Use the [`env_dev_create.sh`](../env_dev_create.sh), which uses 
the `-e` or `--editable` option to allow
pip to install directly from version control. [[1]](#1)

```bash
# ----------------------
# development deployment
# ----------------------
(base) [~/pyschool/zfolder]$ ./env_dev_create.sh
```

Verify the `zmath` package has been installed with pip:

```bash
(base) [~]$ conda activate zmathenv-dev
(zmathenv-dev) [~]$ conda list
... # truncated list
zlib                      1.2.11               h1de35cc_3  
zmath                     0.0.10                    dev_0    <develop>
zstd                      1.4.5                h41d2c2f_0 
... # truncated list
(zmathenv-dev) [~]$ pip list
... # truncated list
wheel              0.35.1
zipp               3.3.0
zmath              0.0.10     /Users/sparta/pyschool/zfolder/src
... # truncated list
(zmathenv-dev) [~]$
```

Then do a quick command line test that the `zmath` package works for the development client:

```python
(zmathenv-dev) [~]$ python
Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import zmath.zalculator as zc
>>> myZ = zc.Zalculator()
The Zalculator is initialized.
>>> myZ.add(3, 4)
7
>>> quit()
```

## Production Client

```bash
# ---------------------
# production deployment
# ---------------------
(base) [~/pyschool/zfolder]$ ./env_create.sh
```

Verify the `zmath` package has been installed with pip:

```bash
(base) [~]$ conda activate zmathenv
(zmathenv) [~]$ conda list
... # truncated list
zlib                      1.2.11               h1de35cc_3  
zmath                     0.0.10                   pypi_0    pypi
zstd                      1.4.5                h41d2c2f_0 
... # truncated list
(zmathenv) [~]$ pip list
... # truncated list
webencodings      0.5.1
wheel             0.35.1
zmath             0.0.10
... # truncated list
(zmathenv) [~]$
```

Then do a quick command line test that the `zmath` package works for the production client:

```python
(tempenv) [apollo ~/temp]$ python
Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import zmath.zalculator as zc
>>> myZ = zc.Zalculator()
The Zalculator is initialized.
>>> myZ.add(3, 4)
7
>>> quit()
```

See [this](https://packaging.python.org/tutorials/installing-packages/#installing-from-a-local-src-tree) for details on installing from a local source.

Then, delete the virutal environment:

```bash
(tempenv) $ conda deactivate
(base) $ conda env remove --name tempenv
(base) $ conda env list # verify tempenv no longer in list
```

## References

* [Dowling, Samuel.  2020.  How to set up a Python project and development environment.](https://www.samueldowling.com/2020/06/08/how-to-set-up-a-python-project-and-development-environment/)
* [Layman, Matt.  2018.  Consistent Python code with Black.](https://www.mattlayman.com/blog/2018/python-code-black/)
* [Griffioen, Henk.  2017.  How to Start a Data Science Projects in Python](https://godatadriven.com/blog/how-to-start-a-data-science-project-in-python/) for folder structure of package.
* [van der Geer, Rogier.  2019.  A Practical Guide to Using Setup.py](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/)

## Back to: [Learn](learn.md)
## Back to: [Configuration](configuration.md)

## Notes:

### 1

* Git, Subversion, Mercurial, and Bazaar are supported.
* Existing check out:
  * Example: `pip install -e path/to/repo`
* New check out:
  * Example: `pip install -e svn+http://svn.colorstudy.com/INITools/trunk#egg=initools-dev`
  * The repo URL must 
    * start with one of the following: `git+`, `svn+`, `hg+` or `bzr+`), 
    * must end with and end with `#egg=packagename`
