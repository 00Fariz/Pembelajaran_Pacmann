# Pertemuan 2 - Set and Counting

# Notasi Himpunan
# Penulisan himpunan digunakan kurung kurawal 𝐴={1,2,3,4,5,6,7,…}
# Himpunan dapat tidak memiliki isi, disebut himpunan KOSONG B={} / B= ∅
# Himpunan dengan isi 1 s.d. 7
A = {1, 2, 3, 4, 5, 6, 7}
print(type(A))                                                     # --> set

# Himpunan kosong
B = set()
print(type(B))                                                     # --> set

# ELEMEN PADA HIMPUNAN, contoh: Hari={Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu}

# Hari Senin merupakan anggota dari set Hari. Secara matematis dapat ditulis
# Senin ∈ Hari

Hari = {'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'}
print("Senin" in Hari)                                               # --> True

# Namun Januari bukan merupakan anggota dari set Hari
# Januari ∉ Hari

print("Januari" in Hari)                                              # --> False

# Menambah Elemen Baru
# Untuk menambah elemen pada set kita dapat menggunakan perintah add()
basic_set = {1,2,3}
basic_set.add(5)
print(basic_set)                                                      #  --> {1, 2, 3, 5}

# Untuk menambah lebih dari satu elemen pada set kita dapat menggunakan perintah : mupdate()
basic_set = {1,2,3}
basic_set.update(basic_set,(5,7,8))
print(basic_set)                                                      #  --> {1, 2, 3, 5, 7, 8}

# Menghapus elemen
# Untuk mengurangi elemen pada list, ada 2 perintah yang dapat kita gunakan: remove()
basic_set.remove(3)
print(basic_set)                                                      #  --> {1, 2, 5, 7, 8}

# Menghitung Jumlah Elemen
# Notasi Jumlah Elemen: |Hari|=7
print(len(Hari))                                                      #   --> 7




# OPERASI HIMPUNAN / SET

# 1. Intersection ( Irisan )
# Fungsi intesection() digunakan untuk menghasilkan set baru yang berisi elemen yang sama dari kedua set
x_set = {1,2,3,4}                   # 𝑋={1,2,3,4}
y_set = {3,4,5,6,7}                 # 𝑌={3,4,5,6,7}
print(x_set.intersection(y_set))    # 𝑋 ∩ 𝑌 = ?                          --> {3,4}
print(x_set & y_set)                # 𝑋 ∩ 𝑌 = ? ( alternatif kode )      --> {3,4}
print(y_set.intersection(x_set))    # Y ∩ X = ?                          --> {3,4}

# 2. Union ( Gabungan )
# Fungsi union() digunakan untuk menghasilkan set yang merupakan menggabungkan dari kedua set
print(x_set.union(y_set))           # 𝑋 U 𝑌 = ?                          --> {1, 2, 3, 4, 5, 6, 7}
print(x_set | y_set)                # 𝑋 U 𝑌 = ? ( alternatif kode )      --> {1, 2, 3, 4, 5, 6, 7}
print(y_set.union(x_set))           # Y U X = ?                          --> {1, 2, 3, 4, 5, 6, 7}

# Difference / Komplemen
# Fungsi diffence() digunakan untuk menghasilkan set baru yang terdiri dari elemen yang tidak ada pada set lain
print(x_set.difference(y_set))      # 𝑋−𝑌=?                              --> {1, 2}
print(y_set.difference(x_set))      # y−x=?                              --> {5, 6, 7}

# Subset & Superset
'''Jika memiliki dua set: misal P dan Q
Set B adalah subset dari A jika semua elemen B ada di A'''
P = {1,2,3,4,5,6,7}
Q = {1,3,5,7}

print(Q.issubset(P))              #mengecek apakah merupakan subset dari set lain
print(P.isdisjoint(Q))            #mengecek apakah kedua set tidak memiliki elemen yang sama
print(P.issuperset(Q))            #mengecek apakah set mengandung semua elemen set lain

import matplotlib.pyplot as plt
import matplotlib_venn as venn

S = {-1, 0, 1, 2, 3,4,5,7, 20,90}
A = {1, 2, 3,4,5}
B = {0, 2, -1, 5,7}
C = {20,90}
D = {100}

# Diagram Venn untuk Himpunan diatas
venn.venn3([A, B, C], set_labels=('A','B', 'C'))
plt.show()

#Dari Himpunan diatas dapat dicari :

#1. |𝐴|,|𝐵|,|𝐶|
print(len(A))
print(len(B))
print(len(C))


