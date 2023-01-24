# break -> akan menyelesaikan proses loop

# angka = 0
# print(f"angka sekarang -> {angka}")
# while angka < 5:
#     angka += 1
#     print(f"angka sekarang -> {angka}")  # aksi 1
#     if angka == 3:
#         print("nice")
#         break

#     print("whassup")  # aksi 2

# print("stop")

data_int = int(input("hitung sampai = "))
angka = 0
while True:
    angka += 1
    print(f"hitungan ke = {angka}")  # aksi 1
    if angka == data_int:
        print("nice")
        break

    print("whassup")  # aksi 2

print("stop")
