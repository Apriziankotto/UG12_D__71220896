print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
input("Masukkan model matematika yang diinginkan 1/2: ")
bilangan= int(input("Menampilkan table matematika dari angka:"))
for a in range (1,11):
        hasil= bilangan * a
        print(bilangan, "x",a,"=", hasil)

print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
input("Masukkan model matematika yang diinginkan 1/2: ")
bilangan= int(input("Menampilkan table matematika dari angka:"))
for a in range (50,66):
        hasil= a / bilangan
        print(a, ":",bilangan,"=", hasil)

print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
pilihan= int(input("Masukkan model matematika yang diinginkan 1/2:"))
if (pilihan>2):
        print("pilihan tidak tersedia, jangan ngasal!")