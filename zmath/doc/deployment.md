# Deployment

## Deploy Environment

## Deploy Library 

```bash
# -----------------
# production server
# -----------------
$ cd ~/pyschool/zmath
$ rm -r zmath.egg-info/ # if it exists, if not, skip this step
$ vim setup.py   # update setup.py, typically increment the version, version is here and possibly in the README.md

# update server if necessary
$ python -m pip install --user --upgrade setuptools wheel
$ python -m pip install --user --upgrade twine

# build to the dist/ subdirectory
$ python setup.py sdist bdist_wheel

# assure the PyPI API token for the server is created on pypi.org and saved on the server at ~/.pypirc

# remove any old .gz and .whl files in dist/ subdirectory
$ cd dist/  # rm old .gz and old .whl
$ cd ../  # back to the ~/sibl/xyfigure directory

# deploy
$ python -m twine upload dist/*

# ------
# client
# ------
$ pip list
$ pip uninstall zmath  # if it exists, later we show the update method alternative to uninstall
$ cd ~/pyschool/zmath/dist
# then either install from pypi.or; or..
$ pip install --user zmath-0.0.n-py3-none-any.whl # where n is the desired version number
# or install from local
$ pip install --user -e zmath-0.0.n-py3-none-any.whl 
# see https://packaging.python.org/tutorials/installing-packages/#installing-from-a-local-src-tree
$ pip list # verify zmath now exist in the list
```

See [this](https://packaging.python.org/tutorials/installing-packages/#installing-from-a-local-src-tree) for details on installing from a local source.


## References

* [Layman, Matt.  2018.  Consistent Python code with Black.](https://www.mattlayman.com/blog/2018/python-code-black/)
