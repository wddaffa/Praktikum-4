List_kota = ['Jakarta', 'Bekasi', 'Bogor', 'Sukabumi', 'Yogyakarta']
print("Tampilkan Elment ke 3", List_kota[2])
print("Tampilkan Elment ke 2 - 4", List_kota[1:4])
print("Tampilkan Elment ", List_kota[4])
#Merubah Elment yang ada 
List_kota[3] = "Aceh"
print("Mengunah Elment ke 4", List_kota)
List_kota[3:5] = "Aceh", "Maluku"
print("Merubah Elment ke 4 s/d terakhir", List_kota)
#Menambahkan Elment List
List_kota1 = ['Jakarta', 'Bekasi', 'Bogor', 'Sukabumi', 'Yogyakarta']
List_kota2 = ['Semarang', 'Surabaya', 'Bandung', 'Purwokerto', 'Malang']
List_kota2.append(List_kota1[1:3])
print("2 Bagian dari list 1 di jadikan list 2 :", List_kota2)
#Menambahkan List 2 dengan nilai string
List_kota2.append("Berebes")
print("Menambahkan List 2 dengan nilai string :", List_kota2)
#Menambahkan List 2 dengan 3 nilai 
print("Menambahkan List 2 dengan 3 nilai :", List_kota2+['Tegal', 'Pemalang', 'Cilacap'])
#Gabungkan List 1 dengan list 2
List_kota3 = List_kota1+List_kota2
print("Gabungkan List kota 1 dengan list kota 2 :", List_kota3)
