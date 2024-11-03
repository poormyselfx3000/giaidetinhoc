
def timb(mang): # thuat toan tim so nho nhat khong ton tai trong mang
    lowest_money = 1
    for so in range(1, so_qua + 1):
        if lowest_money in mang:
            lowest_money = so
    if lowest_money in mang:
            lowest_money += 1
    return lowest_money


filein = open("tangqua.inp")

so_qua = int(filein.readline())
gia_tien = filein.readline().split()

list_theo_luot =[]
fileout = open("tangqua.out","w")

for luot in range(so_qua):
    list_theo_luot.append(int(gia_tien[luot]))
    fileout.write(f"{timb(list_theo_luot)} ")
    print(f"luot {luot + 1} {list_theo_luot} > b = {timb(list_theo_luot)}")