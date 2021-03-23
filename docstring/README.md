# Docstrings

## Standard Format SIBL [repository](https://github.com/sandialabs/sibl)

* Default to keyword-only arguments over positional arguments when possible.
* Docstrings in properties should be defined in the getter by not in the setter..

```python
@property
def state(self, arg_1, arg_2, *, verbose : bool = False) -> np.ndarray:
    """np.ndarry: The current value of the state as a numpy array given by
    (x, y, z).

    Arguments:
	arg_1 (type): Description 1.
	arg_2 (type): Description 2.

    Keyword Arguments:
	verbose (bool): Enhanced command line feedback during run.  Defaults 
	    to False.

    Raises:
        TypeError: description

    Returns:
        Type: description

    Example:
        >>> import numpy as np
        >>> from some_module import state_factory
        >>> state = state_factory(
                silent=True,
                discrete=False,
                state_kwargs=None,
            )
        >>> state.state
        np.array([0.0, 0.0, 0.0, 0.0])
        >>> state.state = np.array([1.0, -1.0, 0.25, -0.25])
        >>> state.state
        np.array([1.0, -1.0, 0.25, -0.25])
    """
    return np.array([self._x_pos, self._y_pos, self._x_vel, self._y_vel])

@state.setter
def state(self, val: np.ndarray):
    self._x_pos, self._y_pos, self._x_vel, self._y_vel = val
```

For all other scenarios, follow the [scikit-learn](https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/model_selection/_split.py) format.

## References

* [Black](https://black.readthedocs.io/en/stable/the_black_code_style.html) code style.
* Google docstring [examples](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* Werner N.  Python Docstring Generator [plugin](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) for VS Code.

