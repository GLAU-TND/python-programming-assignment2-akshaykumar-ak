num = int(input("Enter the number"))
t = bin(num)
print(t)
t = t[2:]
z = t.split('0')
print(z)
x = max(map(len,z))
if(x>1):
    print(x)
else:
    print("No Consecutive 1's present")