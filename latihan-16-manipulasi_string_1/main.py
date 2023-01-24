# operasi dan manipulasi string

# 1. menyambung string(concatenate)
nama_pertama = "faisal"
nama_tengah = "ibnul"
nama_akhir = "hakim"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2 menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3 operator untuk string

# mengecek apakah ada komponen char atau string di string

i = "i"
status = i in nama_lengkap
print("string " + i + " ada di " + nama_lengkap + " = " + str(status))

i = "o"
status = i not in nama_lengkap
print("string " + i + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(10*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-9 : " + nama_lengkap[9])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-5) : " + nama_lengkap[-5])
print("index ke-[0:6] : " + nama_lengkap[0:7]) # angka terakhir tidak dihitung jadi hanya sampai ke 6
print("index ke-[0,2,3,4,6,8] : " + nama_lengkap[0:9:2]) # titik dua terakhit adalah inkrement

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah : " + str(ascii_code))
data = 117
print("char untul ASCII 117 adalah " + chr(data))

# 4 operator dalam bentuk method

data = "faisal ibnul hakim"
jumlah = data.count("a")
print("jumlah a pada " + data + " = " + str(jumlah))
