# libigl

## Installation

[documentation](https://libigl.github.io/libigl-python-bindings/) igl python bindings

```bash
> cd ~/pyschool/source/pyschool/geo
> conda activate pyschool-env
> conda install -c conda-forge igl
> conda install -c conda-forge meshplot 
> jupyter notebook
> jupyter notebook c0ex0.ipynb
> mkdir data
> cd ~/libigl-python-bindings/tutorial/data
> cp bunny_small.off ~/pyschool/src/pyschool/geo/data/.
```

Move from Jupyter Notebook to [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

```bash
> conda install -c conda-forge jupyterlab
> jupyter lab  # start up the application
```

```bash
> cd ~/
> git clone git@github.com:libigl/libigl-tutorial-data.git
> git clone https://github.com/skoch9/meshplot.git
```

## Outline

* Surface point cloud
* Surface triangularization via Poisson surface reconstruction
* Decimation
* Volume via Tetrahedralization

## References

* [Computational Geometry Algorithms Library](https://www.cgal.org/)
* [Poisson Surface Reconstruction: 3D point cloud](https://pypi.org/project/surface-reconstruction/) by [Felipe Michel](https://github.com/mfdeveloper/surface_reconstruction_python)
* Alec Jacobson [Barycentric versus voronoi regional area in mass matrices](https://www.alecjacobson.com/weblog/?p=1146)