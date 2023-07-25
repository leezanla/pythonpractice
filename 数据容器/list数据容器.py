lst = [x * x for x in range(1, 11)]
j = 0
for i in lst:
    if i == 9:
        del lst[j]
        break
    j += 1
print(lst)
print(lst[0])
print(lst[len(lst) - 1])

