def bieu_thuc(x, y):
    p = x + 2*y
    #print(f"{p} = {x} + 2 * {y}") test
    return p

def la_so_nguyento(n): 
    if n < 2:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


filein = open("bieuthucnt.inp")
n = int(filein.read())

count = 0
for gtrx in range(1, n + 1):
    for gtry in range(1, n + 1):
        if la_so_nguyento(bieu_thuc(gtrx,gtry)):
            count += 1
            print(count)
print(count)

fileout = open("bieuthucnt.out","w")
fileout.write(f"{count}")
