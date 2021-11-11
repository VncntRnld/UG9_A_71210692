#tempat input
print("=====MASUKAN JUMLAH MAKANAN YANG DIPESAN=====")
M1 = int(input("IKAN BAKAR     Rp 25.000,00    : "))
M2 = int(input("ES DOGER       Rp 6.000,00     : "))
M3 = int(input("RUJAK CINGUR   Rp 8.000,00     : "))

IB = 25000
ED = 6000
RC = 8000

t1 = M1 * IB
t2 = M2 * ED
t3 = M3 * RC
tsemua = t1 + t2 + t3

#output
print("=====TOTAL=====")
print("TOTAL IKAN BAKAR      : Rp ", t1)
print("TOTAL ES DOGER        : Rp ", t2)
print("TOTAL RUJAK CINGUR    : Rp ", t3)
print("Jumlah total biaya yang harus dibayar adalah Rp ", tsemua)
