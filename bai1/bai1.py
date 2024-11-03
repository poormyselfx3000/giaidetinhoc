N = []
solonnhat = 0


filein = open("bai1.inp")
docfile = filein.read().split()

# de tach phan tu va them vao tap hop N
for phantu in docfile[0]:
    N.append(int(phantu))

tong = sum(N)

for phantu in N:
    if phantu >= solonnhat:
        solonnhat = phantu

so_sinh = tong * solonnhat

print(so_sinh)

fileout = open("bai1.out","w")

fileout.write(f"{so_sinh}")
