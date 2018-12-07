
L = [1, 2 ,4, 8, 16, 32, 64, 128]
X = 5
check = 2 ** X
if check in L:
    print("found at index " + str(L.index(check)))
else:
    print ("not found")