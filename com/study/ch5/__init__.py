#coding=utf-8

L1 = [2 , 3, 4]
L2 = L1
L1[0] = 24
print(L1, L2)


L1 = [2 , 3, 4]
L2 = L1[:]  # copy
L1[0] = 24
print(L1, L2)

print(list(map(ord, 'spam')))

x = list(map(ord, 'spam'))

print([ chr(i) for i in x])

i = 0
while i < 10:
    i += 1
    if i == 5 or i == 7:
        print("break")
        break
else:
    print("abad" + str(i))
print("abad" + str(i + 1))


S = 'spam'

for (o, item) in enumerate(S):
    print(item , o)
