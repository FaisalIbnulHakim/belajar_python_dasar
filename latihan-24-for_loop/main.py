# perulangan (loop)

# for kondisi :
#     aksi

# ini dengan list
angka_list = [0, 2, 4, 6, 8]  # ini adalah list
print(angka_list)

for i in angka_list:
    print(f"i sekarang -> {i}")

print("akhir dari program 1\n")

# ini dengan range
angka_range = range(5)

for i in angka_range:
    print(f"i sekarang -> {i}")


print("akhir dari program 2\n")

# ini dengan range 2
angka_range2 = range(1, 10)

for i in angka_range2:
    print(f"i sekarang -> {i}")

print("akhir dari program 3\n")

# menggunakan string
data_str = "saya hebat beuttt"

for huruf in data_str:
    print(huruf)

print("akhir dari program 4\n")
