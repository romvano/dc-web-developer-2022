from typing import TypeVar, Generic

T = TypeVar("T")

class LinkedList(Generic[T]):
    data: T
    next: "LinkedList[T]"

    def __init__(self, data: T):
        self.data = data

head_int: LinkedList[int] = LinkedList(1)
head_int.next = LinkedList(2)
head_int.next = 2  # error: Incompatible types in assignment (expression has type "int", variable has type "LinkedList[int]")
head_int.data += 1
head_int.data.replace("0", "1")  # error: "int" has no attribute "replace"

head_str: LinkedList[str] = LinkedList("1")
head_str.data.replace("0", "1")

head_str = LinkedList[str](1)  # error: Argument 1 to "LinkedList" has incompatible type "int"; expected "str"