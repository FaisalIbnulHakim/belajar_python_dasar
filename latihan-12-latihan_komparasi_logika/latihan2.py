# latihan  2
# ++++++0--------5++++++8-------10+++++++
inputUser = float(input("\nmasukan angka yang bernilai kurang dari 0 dan lebih besar dari 5,serta kurang dari 8 dan lebih besar dari 10 : "))

# +++++++0--------
isKurangSatu = inputUser < 0
print("kurang dari 0 = ",isKurangSatu)

# -------5+++++++
isLebihSatu = inputUser > 5
print("Lebih dari 5 = ",isLebihSatu)

# +++++++8--------
isKurangDua = inputUser < 8
print("kurang dari 8 = ",isKurangDua)

# -------10+++++++
isLebihDua = inputUser > 10
print("Lebih dari 10 = ",isLebihDua)

# ++++++0--------5++++++8-------10+++++++
isCorrect = (isKurangSatu or (isLebihSatu and isKurangDua) or isLebihDua)
print("angka yang anda masukan : ",isCorrect)