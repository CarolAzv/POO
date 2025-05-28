n1, n2, n3 = map(int, input().split())

def maior(x, y, z):
    mai = 0
    if x > y:
        mai = x
    else:
        mai = y
    if z > mai:
        mai = z
    return mai

print(maior(n1, n2, n3))
