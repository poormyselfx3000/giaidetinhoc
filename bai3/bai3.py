# bai 3 

def la_so_nguyento(n):
    if n < 2:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

def tinhtong_n_den_m(n,m):
    list_i = []
    dong2 = str(dongs[1])
    dong2 = dong2.split()
    tong = 0
    for i in range(int(n)-1,int(m)):
        list_i.append(i)

    for i in list_i:
        tong += int(dong2[i])
    return tong

def out(loop):
    dongi = str(dongs[loop])
    dongi = dongi.split()
    if la_so_nguyento(tinhtong_n_den_m(dongi[0],dongi[1])):
       return True
    else: return False


filein = open("bai3.inp")
docfile = filein.readlines()
dongs = []

fileout = open("bai3.out","w")

for dong in docfile:
    dongs.append(dong.strip())

thongso = str(dongs[0])
thongso = thongso.split()
outkq = []

for i in range(2, int(thongso[1])+2):
     
    if out(i):
        outkq.append(str("1\n"))
    else: 
        outkq.append(str("0\n"))
outkq[-1] =outkq[-1].strip()
kq = "".join(outkq)
print(kq)
fileout.write(kq)



    


