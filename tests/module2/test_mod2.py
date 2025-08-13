from module2.mod2_a import mod2_a_func
from module2.mod2_b import mod2_b_func


class TestMod2:
    def test_mod2_a(self) -> None:
        assert mod2_a_func("hello") == "mod2_a_func('hello'), which calls mod2_b_func('hello')"

    def test_mod2_b(self) -> None:
        assert mod2_b_func("hello") == "mod2_b_func('hello')"
