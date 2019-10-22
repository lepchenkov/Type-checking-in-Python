def square(x: int) -> int:
    return x**2

square(3)

# this will raise an error when running mypy square.py
square('text')
# error: Argument 1 to "square" has incompatible type "str"; expected "int"