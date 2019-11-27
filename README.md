# pyschool
Examples of Pythonic patterns

## Principles

## `D.R.Y.` it out

Strive for `D.R.Y.` (don't repeat yourself).  Avoid `W.E.T.` (write everything twice).  When code is wet, dry it out.

## `Convention > Configuration`

Code should just run the first time, without clients needing to spend excessive amount of time configuring prior to the run.  Use default values.  Allow clients to modify the default values.

## Kill all verbs

`Get` and `Set` are dead-weight verbs that can be inferred from whether a value is being returned (a getter) or passed (a setter).  When `get` and `set` are eliminated from the API, client code gets more compact, more noun-driven, more attribute-rich, and less procedural.  


## References

* [Effective-Python](https://hacktec.gitbooks.io/effective-python/content/en/Chapter1/Chapter1.html)
