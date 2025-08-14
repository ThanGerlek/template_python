from module1.mod1_b import mod1_b_func
from module1.mod1_a import mod1_a_func


class TestMod1:
    def test_mod1_a(self) -> None:
        assert mod1_a_func("hello") == "mod1_a_func('hello'), which calls mod1_b_func('hello'). It also calls the other module: mod2_a_func('hello'), which calls mod2_b_func('hello')"

    def test_mod1_b(self) -> None:
        assert mod1_b_func("hello") == "mod1_b_func('hello')"
