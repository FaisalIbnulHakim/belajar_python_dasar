# latihan
# kalkulator sederhana

print(10*"=")
print("Kalkulator sederhana")
print(10*"=" + "\n")

angka_1 = float(input("masukan angka 1 = "))
operator = input("operator apa yang dimasukan (+,-,x,/) : ")
angka_2 = float(input("masukan angka 2 = "))

# percabangannya

if operator == "+":
    hasil = angka_1 + angka_2
elif operator == "-":
    hasil = angka_1 - angka_2
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
elif operator == "/":
    hasil = angka_1 / angka_2
else:
    print("masukan yang benar ")
print(f"hasilnya adalah {hasil}")