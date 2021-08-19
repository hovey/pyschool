# D.R.Y.

* `D.R.Y.` is don't repeat yourself.
* `W.E.T.` is write everything twice.
* **Prefer dry code to wet code.**

Dry code appears in the code base one and *only* one time.  Code that appears more than once it is not dry, it is wet.  

When code is repeated `[2, 3, ...n]` times, it creates two code liabilities:

1. **Maintainence** - a change to dry code requires only one update; the change is isolated to one location in the code base.  A change to wet code requires that all instances of the code snippet be updated, a tedious and potentially time consuming task when the repeated code is pervasive throughout the code base.  A project-wide search and replace may help find all instances, but requires additional maintainence effort.  
2. **Bugs** -  moreover, wet code can be highly error prone.  A lurking instance of wet code that was not discovered when a maintainence update ocurred exposes the developer to risk code bugs stemming from unanticipated behavior.

