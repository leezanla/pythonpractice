s1 = "hello"
print(len(s1))


def length(s: str) -> int:
    count = 0
    for i in s:
        count += 1
    return count


print(length(s1))








