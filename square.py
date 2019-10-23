from typing import Tuple


def square(x: int) -> int:
    return x**2

square(3)

# this will raise an error when running mypy square.py
square(5)
# error: Argument 1 to "square" has incompatible type "str"; expected "int"


class Photo:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    def get_dimensions(self) -> Tuple[int, int]:
        return self.width, self.height
