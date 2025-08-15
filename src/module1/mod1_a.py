from module1 import DATA_DIR
from module1.mod1_b import mod1_b_func
from module2.mod2_a import mod2_a_func


def mod1_a_func(string: str) -> str:
    with DATA_DIR.open("r") as f:
        data1 = f.read().strip()
    with open("data/others/other_file.txt", "r") as f:
        data2 = f.read().strip()

    return (f"This is mod1_a_func('{string}'), which calls {mod1_b_func(string)}.\n"
            f"It also calls the other module: {mod2_a_func(string)}\n"
            f"Module 1 also can access data, such as \"{data1}\" and \"{data2}\"")
