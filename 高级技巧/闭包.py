
def outer(number1):
    def inner(number2):
        nonlocal number1
        number1 += number2
        return number1
    return inner


func1 = outer(0)
for i in range(1, 101):
    func1(i)
print(func1(0))












