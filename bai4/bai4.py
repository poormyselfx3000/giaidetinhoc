

filein = open("bai4.inp")
dong1 = filein.readline().split() 
baiktr = filein.readline().split()
btdalam = []
diemkynang = int(dong1[1])
sobt = int(dong1[0])                 #khai bao nhieu qua :)
i = True
sobtconlai = 0

while i == True:#neu ky nang van con thi van tiep tuc lap

    sobtconlai = sobt - len(btdalam)
    for dokho in baiktr:
        
        if diemkynang >= int(dokho) and dokho not in btdalam: # ktr xem co du knang lm bai kh va ktr xem neu lam bai do roi thi cx kh tinh
            diemkynang += int(dokho)     
            btdalam.append(dokho)
            
    if sobt == sobtconlai + len(btdalam):
        i = False


print(len(btdalam))

#xuat ra file out
fileout = open("bai4.out","w")
fileout.write(f"{len(btdalam)}")