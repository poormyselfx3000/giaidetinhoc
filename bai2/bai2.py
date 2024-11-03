filein = open("bai2.inp")

docfile1 = filein.readline()
docfile2 = filein.readline().split()

thchu = []
tvchu = {}

for chu in docfile2[0]:
    if chu not in thchu:
        thchu.append(chu)
        tvchu[chu] = 1
    else :
        tvchu[chu] += 1


counter = 0
th_chu_xh = []

for chu in thchu:
    if tvchu[chu] >= counter:
        counter = tvchu[chu]

for chu in thchu:
    if tvchu[chu] == counter:
        th_chu_xh.append(chu)

        
th_chu_xh.sort()

print(th_chu_xh[0])

kq = str(th_chu_xh[0])
fileout = open("bai2.out","w")
fileout.write(kq)