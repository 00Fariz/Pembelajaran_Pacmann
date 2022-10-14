# KOMBINATORIKA

# Dalam pembuatan sebuah set, terkadang diperlukan pengolahan terlebih dahulu. Misal, contoh sederhana:
#---Menghitung kombinasi cara pemasangan pakaian.
#---Kombinasi penarikan kartu.
#---Ada berapa kali cara 3 kejadian sukses (barang defect, customer churn) dalam 5 observasi?

# Dalam kombinatorik, digunakan 2 metode dasar untuk menjawab pertanyaan tersebut:
#---Permutasi
#---Kombinasi

"""Permutasi
Permutasi adalah cara penyusunan dengan urutan pada suatu kumpulan objek.
Misalkan kita memiliki 4 objek huruf {A,H,L,O}
Jika 4 huruf ini disusun, maka dapat terbentuk:"""

from itertools import permutations
huruf = {'A','H','L','O'}
perm = permutations(huruf)
for i in list(perm):
    print(i)                                       #  Menampilkan hasil permutasi

#Bagaimana jika hanya diambil elemen sejumlah  𝑘 ?
k = 2
perm_k = permutations(huruf, k)
for i in list(perm_k):
    print(i)

# Kombinasi
# Banyaknya subset yang dapat dibentuk dari suatu set awal:
# Misal, anda memiliki 3 teman  {Joko, Budi, Seno}
# Namun, anda hanya bisa mengajak 2 dari mereka untuk naik mobil anda.
# Kombinasi yang mungkin adalah: {Joko, Budi}
# {Joko, Budi }, {Joko, Seno}. {Joko, Seno},{Budi, Seno}

# Kombinasi vs Permutasi
# Kombinasi tidak terpengaruh oleh urutan.
# Dalam kombinasi:  {Joko, Budi}={Budi, Joko}
# Dalam permutasi:  {Joko, Budi}≠{Budi, Joko}

from itertools import combinations
teman = {'Joko', 'Budi', 'Seno'}
comb = combinations(teman,2)
for i in list(comb):                                    # Menampilkan hasil kombinasi
    print(i)

