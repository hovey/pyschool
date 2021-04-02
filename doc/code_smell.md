# Code Smell

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
