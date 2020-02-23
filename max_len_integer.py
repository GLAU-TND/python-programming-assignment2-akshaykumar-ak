from itertools import permutations
x = eval(input())
l=list(map(str,x))
p=list(permutations(l))
max=0
for i in p:
    s="0"
    for j in i:
        s=s+j
    if int(s) > max:
        max=int(s)
print(max)