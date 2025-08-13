from module1.mod1_b import mod1_b_func
from module2.mod2_a import mod2_a_func


def mod1_a_func(string: str) -> str:
    return f"mod1_a_func('{string}'), which calls {mod1_b_func(string)}. It also calls the other module: {mod2_a_func(string)}"
