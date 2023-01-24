# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

# -----CELCIUS-----
print("1. KONVERSI DARI CELCIUS KE LAINNYA\n")

C = float(input("Masukan suhu dalam celcius : "))
print("suhu adalah",C,"Celcius")

# Reamur
R = (4/5) * C
print("suhu dalam reamur adalah ", R,"Reamur")

# fahrenheit
F = ((9/5) * C) + 32
print("suhu dalam fahrenheit adalah ",F,"Fahrenheit")

# Kelvin 
K = C + 273
print("suhu dalam kelvin adalah ",K,"Kelvin")
 
# -----REAMUR----- 
print("\n2. KONVERSI DARI REAMUR KE LAINNYA\n")

R = float(input("Masukan suhu dalam reamur : "))
print("suhu adalah",R,"Celcius")

# Celcius
C = (5/4) * R
print("suhu dalam celcius adalah ", C,"Celcius")

# fahrenheit
F = ((9/4) * R) + 32
print("suhu dalam fahrenheit adalah ",F,"Fahrenheit")

# Kelvin 
K = ((5/4) * R) + 273
print("suhu dalam kelvin adalah ",K,"Kelvin")

# -----FAHRENHEIT-----
print("\n3. KONVERSI DARI FAHRENHEIT KE LAINNYA\n")

F = float(input("Masukan suhu dalam fahrenheit : "))
print("suhu adalah",F,"Fahrenheit")

# Celcius
C = (5/9) * (F - 32)
print("suhu dalam celcius adalah ",C,"Celcius")

# Reamur
R = (4/9) * (F - 32)
print("suhu dalam reamur adalah ", R,"Reamur")

# Kelvin 
K = ((5/9) * (F - 32)) + 273
print("suhu dalam kelvin adalah ",K,"Kelvin")

# -----KELVIN-----
print("\n4. KONVERSI DARI KELVIN KE LAINNYA\n")

K = float(input("Masukan suhu dalam kelvin : "))
print("suhu adalah",K,"Kelvin")

# Celcius
C = K - 273
print("suhu dalam celcius adalah ",C,"Celcius")

# Reamur
R = (4/5) * (K - 273)
print("suhu dalam reamur adalah ", R,"Reamur")

# Fahrenheit 
F = ((9/5)*(K - 273)) + 32
print("suhu dalam kelvin adalah ",F,"Fahrenheit")
