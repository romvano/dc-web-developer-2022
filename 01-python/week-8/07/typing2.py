from typing import Union, Dict

def some_func(arg: Union[Dict[str, str], str]) -> int:
    return len(arg)


some_func({"a": "b"})
some_func("abc")
some_func({"a": 1})