ls1 = eval(input())
p = len(ls1)
l1 = []
for i in range(len(ls1)):
    if i == 0:
        l1.append(min(ls1))
        ls1.remove(min(ls1))
    elif i == p-1:
        l1.append(ls1[-1])
    else:
        for j in ls1:
            for k in ls1:
                if l1[-1][-1] == j[0] and j[-1] == k[0]:
                    l1.append(j)
                    ls1.remove(j)
print(l1)