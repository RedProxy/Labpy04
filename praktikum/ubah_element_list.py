# Ubah element list
print("======================= Mengubah List ==========================")
print()
negara = ['china', 'taiwan', 'korea', 'singapura', 'australia', 'kanada']
print("List:", negara)
print()

## ubah elemen ke-4 dengan nilai lainnya
print("Mengubah Elemen ke-4 dengan nilai lainnya :")
print("List sebelum di ubah :", negara)
print()
negara[4]='jepang'
print("List sesudah di ubah :", negara)
print()

## ubah elemen ke 4 sampai dengan elemen terakhir
print("Mengubah Elemen ke-4 sampai dengan elemen terakhir :")
negara[4:]=["hongkong", "makau"]
print("Ubah element ke-4 hingga akhir :", negara)
print()
