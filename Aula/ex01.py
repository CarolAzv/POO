x = 1
while x <= 10:
    print(x, end=" ")
    x +=1

print()

for x in range (1, 11):
    print(x, end=" ")
print()

def prints(x, limite):
    if <=limite:
        return
    else:
        print(x, end=" ")
        print(prints(x+1, limite))

prints(1. 11)
print()