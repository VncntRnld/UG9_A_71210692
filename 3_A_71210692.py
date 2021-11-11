#variabel

D1list = []
D2list = []

D1 = (input("Masukkan daftar belanja 1: "))
D2 = (input("Masukkan daftar belanja 2: "))

D1list.append (D1) 
D2list.append (D2)

D1t = input("Tambahkan data ke daftar belanja 1: ")
D2t = input("Tambahkan data ke daftar belanja 2: ")

D1list.append (D1t) 
D2list.append (D2t)

#output
print("Daftar belanja 1 adalah ", D1list)
print("Daftar belanja 2 adalah ", D2list)
