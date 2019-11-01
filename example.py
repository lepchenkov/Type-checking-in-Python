from typing import Tuple


def square(x: int) -> int:
    return x**2

square(3)

# this will raise an error when running mypy square.py
square('some string')
# error: Argument 1 to "square" has incompatible type "str"; expected "int"


class Photo:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    def get_dimensions(self) -> Tuple[int, int]:
        return (self.width, self.height)


photos = [Photo(320, 320), Photo(640,540)]

# photos.append('foo')
# causes error: Argument 1 to "append" of "list" 
# has incompatible type "str"; expected "Photo"

from typing import Optional

class Foo:
    def __init__(self, id: int) -> None:
        self.id = id


def get_foo(foo_id: Optional[int]) -> Optional[Foo]:
    if foo_id is None:
        return None
    return Foo(foo_id)

get_foo(3)


from typing import TypeVar

Anystr = TypeVar('Anystr', str, bytes)

def concat(a: Anystr, b: Anystr) -> Anystr:
    return a+b

concat('foo', 'bar')

# concat('foo', b'bar')
#  error: Value of type variable "Anystr" of "concat" cannot be "object"
