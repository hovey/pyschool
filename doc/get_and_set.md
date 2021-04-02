# Get and Set

## Eliminate non-C.R.U.D. verbs in APIs

`Get` and `Set` are dead weight verbs that can be inferred from whether a value is being returned (a getter) or passed (a setter).  When `get` and `set` are eliminated from the API, client code gets more compact, more noun-driven, more attribute-rich, and less procedural.  

Consider
```python
  set_color(self, value):  # bloated
    self._color = value
```
versus
```python
  color(self, value):  # not bloated
    self._color = value
 ```

Verbs, in general, can harbor lots of dead weight and bloat.  Instead of `set` other verbs that could be used with `color` are `calculate` (e.g., RBG or alpha channels) or `update` or `render` or `draw` or `paint` or `apply`... and really these verbs are hallmarks of implementation, not interface; they start to expose the service's internals for returning a color to the client.  And, they are unnecessary noise for the client, who either just wants to get or set the color, and not worry about how the same is implemented. 

Thus, verbs, *in the service API*, invite the slippery slope of coupling client to a service's implementation, which is bad.  Prefer to couple the client to the service's interface.  That way, should the implementation change, it does not propagate changes to the client, forcing them to update how they use the service.

From the REST API notes, [How to Design a REST API](https://restfulapi.net/rest-api-design-tutorial-with-example/)

> Notice that these URIs do not use any verb or operation. It’s very important to not include any verb in URIs. URIs should all be nouns only.