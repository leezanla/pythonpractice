from typing import TypeVar

T = TypeVar("T", str, list, tuple)  # 如果不写后面的三个，表示是可以是任何的类型


def func(data: T, data2: T) -> T:
    return data + data2


print(func("11", 22))













