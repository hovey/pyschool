# pyschool
Examples of Pythonic patterns

## Principles

## D.R.Y. it out

Strive for `D.R.Y.` (don't repeat yourself).  Avoid `W.E.T.` (write everything twice).  When code is wet, dry it out.

## Convention > Configuration

Code should just run the first time, without clients needing to spend excessive amount of time configuring prior to the run.  Services should use default values.  Allow clients to modify the default values through the service's API.

## Kill all non-C.R.U.D. verbs in APIs

`Get` and `Set` are dead weight verbs that can be inferred from whether a value is being returned (a getter) or passed (a setter).  When `get` and `set` are eliminated from the API, client code gets more compact, more noun-driven, more attribute-rich, and less procedural.  

Consider
```python
  set_color(self, new_color):  # bloated
    self._color = new_color
```
versus
```python
  color(self, value):  # not bloated
    self._color = value
 ```

Verbs, in general, can harbor lots of dead weight and bloat.  Instead of `set` other verbs that could be used with `color` are `calculate` (e.g., RBG or alpha channels) or `update` or `render` or `draw` or `paint` or `apply`... and really these verbs are hallmarks of implementation, not interface; they start to expose the service's internals for returning a color to the client.  And, they are unnecessary noise for the client, who either just wants to get or set the color, and not worry about how the same is implemented. 

Thus, verbs, *in the service API*, invite the slippery slope of coupling client to a service's implementation, which is bad.  Prefer to couple the client to the service's interface.  That way, should the implementation change, it does not propagate changes to the client, forcing them to update how they use the service.

### C.R.U.D.

From the database standard, there are four main verbs that snap all tranactions: 

* **CREATE** - aka calculate, generate, make, new
* **READ** *this is **get***, copy, fetch
* **UPDATE** *this is **set***, serialize, write
* **DELETE** typically not used except for memory management

## Code Smell

Consider the string of `if` checking:
```python
  if barks:
    # do something with Dog objects
  
  if meows:
    # do something with Cat objects
    
  if tweets:
    # do something with Bird objects
```

This is an example of `code smell`, which means the code has sufficent *function* but has weak *form*.  In this example, the client is forever checking the myriad of different `Animal` descendants.  As the number of `Animals` increases, clients must modify their code everyhere they used this smelly pattern.  

More on this pattern later.

## References

* [Effective-Python](https://hacktec.gitbooks.io/effective-python/content/en/Chapter1/Chapter1.html)
