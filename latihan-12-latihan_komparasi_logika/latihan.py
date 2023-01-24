# latihan  1
# --------0+++++++5-------8+++++++10-------
inputUser = float(input("\nmasukan angka yang bernilai lebih besar dari 0 dan kurang dari 5,serta lebih besar dari 8 dan kurang dari 10 : "))

# --------0+++++++
isLebihSatu = inputUser > 0
print("Lebih dari 0 = ",isLebihSatu)

# +++++++5-------
isKurangSatu = inputUser < 5
print("kurang dari 5 = ",isKurangSatu)

# --------8+++++++
isLebihDua = inputUser > 8
print("Lebih dari 8 = ",isLebihDua)

# +++++++10-------
isKurangDua = inputUser < 10
print("kurang dari 10 = ",isKurangDua)

# --------0+++++++5-------8+++++++10-------
isCorrect = ((isKurangSatu and isLebihSatu) or (isKurangDua and isLebihDua))
print("angka yang anda masukan : ",isCorrect)


