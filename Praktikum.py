#Program Input Data Mahasiswa
i           =   0
Nama        =   []
Nim         =   []
Nilaitugas  =   []
Nilaiuts    =   []
Nilaiuas    =   []
Nilaiakhir  =   []

while True :
    Nama1           =   input("Masukan Nama :")
    Nama.append(Nama1)
    Nim1            =   input("Masukan No NIM :")
    Nim.append(Nim1)
    Nilaitugas1     =   input("Masukan Nilai Tugas :")
    Nilaitugas.append(Nilaitugas1)
    Nilaiuts1       =   input("Masukan Nilai UTS :")
    Nilaiuts.append(Nilaiuts1)
    Nilaiuas1        =   input("Masukan Nilai UAS :")
    Nilaiuas.append(Nilaiuas1)

    Nilaiakhir1 = (int(Nilaitugas1)*0.30) + (int(Nilaiuts1)*0.35) + (int(Nilaiuas1)*0.35)
    Nilaiakhir.append(Nilaiakhir1)

    more = ""
    while more != "Y" and more  != "T" :
        more = input("Tambah Data (Y/T) ? ")
    i += 1
    if more == "T" :
        break

print("_________________________________________________________________________________________________________")
print("|                                       Daftar Mahasiswa                                                |")
print("|_______________________________________________________________________________________________________|")
print("|   No  |        Nama        |       NIM      |    Tugas    |     UTS      |    UAS    |   Nilai Akhir  |")
print("|-------------------------------------------------------------------------------------------------------|")
for n in range (i) :
    print("| ",n+1," |      ",Nama[n],"      |     ",Nim[n],"      |    ",Nilaitugas[n],"   |   ",Nilaiuts[n],"   |     ",Nilaiuas[n],"    |    ",Nilaiakhir[n],"   |")
    print("|-------------------------------------------------------------------------------------------------------|")