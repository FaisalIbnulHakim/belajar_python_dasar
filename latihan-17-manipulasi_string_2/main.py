# operator dalam bentuk methods

## merubah case dari string
# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
nama = "Faisal Ibnul H"
print("normal = " + nama)
nama = nama.upper()
print("lower = " + nama)

## pengecekan dengan menggunakan isX method

# contoh untuk pengecekan lower case
salam = "cok!"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
nama = "Fiuls"
cek_nama = nama.isalpha() # hasil bool
print(nama + " is alpha = " + str(cek_nama))

nama = "F1uls"
cek_nama = nama.isalpha() # hasil bool
print(nama + " is alpha = " + str(cek_nama))

# isalnum() <-- huruf dan angka
angka = "i2345"
cek_angka = angka.isalnum() # hasil bool
print(angka + " is alnum = " + str(cek_angka))

angka = "i234$"
cek_angka = angka.isalnum() # hasil bool
print(angka + " is alnum = " + str(cek_angka))

# isdecimal() <-- angka saja
angka = "12345"
cek_angka = angka.isdecimal() # hasil bool
print(angka + " is decimal = " + str(cek_angka))

angka = "i2345"
cek_angka = angka.isdecimal() # hasil bool
print(angka + " is decimal = " + str(cek_angka))

# isspace() <-- spasi, tab, newline \n

# istitle() <-- semua kata dimulai dengan huruf besar
judul = "It Is Alright"
cek_judul = judul.istitle() # hasil bool
print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith()
cek_start = "Satu Dua Tiga" .startswith("Satu")
print("start = " + str(cek_start))
 
cek_end = "Satu Dua Tiga" .endswith("Tiga")
print("end = " + str(cek_end))

## penggabugan komponen join() split()
pisah = ['aku','benci','manusia']
print(pisah)
gabung = ','.join(pisah)
print(gabung)
gabung = ' '.join(pisah)
print(gabung)

gabungan = "faisal ibnul hakim"
print(gabungan.split(' '))

# alokasi karakter
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(10)
print("'"+tengah+"'")
fiuls = "fiuls".center(15,"-")
print("'"+fiuls+"'")

# kebalikannya -> strip()
fiuls = fiuls.strip("-") # menghilangkan tanda
print("'"+fiuls+"'")
