import timeit


import fibonacci_cy as fib_cy  # imports fibonacci_cy.cypthon-38-darwin.so

nums: int = 11
for x in range(nums):
    y: int = fib_cy.fib(x)
    print(f"Fibonacci of {x} is {y}")

cy = timeit.timeit("fibonacci_cy.fib(11)", setup="import fibonacci_cy", number=100)
py = timeit.timeit("fibonacci_py.fib(11)", setup="import fibonacci_py", number=100)

print("Absolute times:")
print(f"Cython: {cy} seconds")
print(f"Python: {py} seconds")
print("Relative times:")
ratio: float = py / cy
print(f"Cython is {ratio} times faster than Python.")
