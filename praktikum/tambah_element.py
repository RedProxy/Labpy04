# Tambah element list
print("================ Menambah List =========================")
print()
a=[10, 20, 30, 40, 50]
b=[60, 70, 80, 90, 100]

## Mengambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
print("Mengambil 2 bagian dari list A dan jadikan list ke B :")
b.append(a[0:2])
print(b)
print()

## Menambah list B dengan nilai string
print("Menambah list B dengan nilai string :")
b.append("25")
print(b)
print()

## Menambah list B dengan 3 nilai
print("Menambah list B dengan 3 nilai :")
print(b+[26, 27, 28])
print()

## Menggabungkan list B dengan list A
print("Menggabungkan list B dengan list A :")
print(a+b)
