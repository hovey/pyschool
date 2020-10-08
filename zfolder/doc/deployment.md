# Deployment

## Deploy Library 

```bash
# -----------------
# production server
# -----------------
$ conda activate zmathenv

# update environment if necessary
$ python -m pip install --user --upgrade setuptools wheel
$ python -m pip install --user --upgrade twine

$ cd ~/pyschool/zfolder

# delete prior deployments
$ rm -r build/ # if it exists, if not, skip this step
$ rm -r dist/ # if it exists, if not, skip this step
$ rm -r zmath.egg-info/ # if it exists, if not, skip this step

$ vim setup.py   # update setup.py, typically increment the version, version is here and possibly in the README.md

# build to the dist/ subdirectory
$ python setup.py sdist bdist_wheel

# assure the PyPI API token for the server is created on pypi.org and saved on the server at ~/.pypirc

# remove any old .gz and .whl files in dist/ subdirectory
$ cd dist/  # rm old .gz and old .whl
$ cd ../  # back to the ~/sibl/xyfigure directory

# deploy
$ python -m twine upload dist/*

# end of deployment, now test a client
$ conda deactivate

# ------
# client
# ------
# verify conda is up-to-date
(base) $ conda update -n base -c defaults conda

$ cd ~/pyschool/zfolder
$ conda activate 

$ mkdir temp
$ cd ~/temp
(base) $ conda create --name tempenv python=3.8
(base) $ conda activate tempenv

$ pip list # concept: verifiy zmath package is not listed; 
# OR,
$ pip uninstall zmath  # if it exists, later we show the update method alternative to uninstall

$ pip install --user ~/pyschool/zfolder/dist/zmath-0.0.n-py3-none-any.whl # where n is the desired version number

# or install from local
$ pip install --user -e zmath-0.0.n-py3-none-any.whl 
# see https://packaging.python.org/tutorials/installing-packages/#installing-from-a-local-src-tree
$ pip list # verify zmath now exist in the list
```

Then do a quick command line test that the `zmath` package works for the client:

```python
(tempenv) [apollo ~/temp]$ python
Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from zmath.zalculator import Zalculator as zc
>>> testobj = zc()
The Zalculator is initialized.
>>> testobj.add(2, 3)
5
>>> 
```


See [this](https://packaging.python.org/tutorials/installing-packages/#installing-from-a-local-src-tree) for details on installing from a local source.


## References

* [Layman, Matt.  2018.  Consistent Python code with Black.](https://www.mattlayman.com/blog/2018/python-code-black/)
* [Griffioen, Henk.  2017.  How to Start a Data Science Projects in Python](https://godatadriven.com/blog/how-to-start-a-data-science-project-in-python/) for folder structure of package.
* [van der Geer, Rogier.  2019.  A Practical Guide to Using Setup.py](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/)
