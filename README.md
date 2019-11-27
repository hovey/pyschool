# pyschool
Examples of Pythonic patterns

## Principles

## D.R.Y. it out

Strive for `D.R.Y.` (don't repeat yourself).  Avoid `W.E.T.` (write everything twice).  When code is wet, dry it out.

## Convention > Configuration

Code should just run the first time, without clients needing to spend excessive amount of time configuring prior to the run.  Use default values.  Allow clients to modify the default values.

## Kill all verbs

`Get` and `Set` are dead weight verbs that can be inferred from whether a value is being returned (a getter) or passed (a setter).  When `get` and `set` are eliminated from the API, client code gets more compact, more noun-driven, more attribute-rich, and less procedural.  

Consider
```python
  set_color(self, new_color):  # bloated
    self._color = new_color
```
versus
```python
  color(self, value):  # lead
    self._color = value
 ```

Verbs, in general, can harbor lots of dead weight and bloat.  Instead of `set` other verbs that could be used with `color` are `calculate` (e.g., RBG or alpha channels) or `update` or `render` or `draw` or `paint` or `apply`... and really these verbs are hallmarks of implementation, not interface; they start to expose the service's internals for returning a color to the client.  

Thus, verbs invite the slippery slope of coupling client to a service's implementation, which is bad.  Prefer to couple the client to the service's interface.  That way, then the implementation needs to change, it does not propagate changes to the client, forcing them to update how they use the service.

## References

* [Effective-Python](https://hacktec.gitbooks.io/effective-python/content/en/Chapter1/Chapter1.html)
