# continue dan pass

# pass -> sebagai dummy, tidak akan dieksekusi

# angka = 0
# while angka < 5:
#     angka += 1

#     if angka == 3:
#         pass  # tidak akan dieksekusi

#     print(angka)


# continue -> akan membuat loop meloncat ke step selanjutnya

angka = 0
print(f"angka sekarang -> {angka}")
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")  # aksi 1
    if angka == 3:
        print("nice")
        continue

    print("whassup")  # aksi 2

print("stop")
