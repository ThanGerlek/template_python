from src.module2.mod2_b import mod2_b_func


def mod2_a_func(string: str) -> str:
    return f"mod2_a_func('{string}'), which calls {mod2_b_func(string)}"
