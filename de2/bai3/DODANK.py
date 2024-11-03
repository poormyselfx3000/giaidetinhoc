filein = open("DODANK.INP")

line1 = filein.readline().split()
A = list(map(int, filein.readline().split()))

B = A
n = line1[0]
k = int(line1[1])

# can tim ra nhung so co khoang cach 2 trong A de B get

for aj in range(1, len(A)+1):
    for ai in range(1, len(A)+1):
        print(f"{int(A[aj-1]) + int(A[ai-1])}")
        if aj - ai >= k:
            print(f"get {int(A[aj-1]) + int(A[ai-1])}")
            B.append(int(A[aj-1]) + int(A[ai-1]))

fileout = open("DODANK.OUT","w")
fileout.write(f"{sum(B)}")


