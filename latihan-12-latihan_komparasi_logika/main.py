# latihan logika dan komparasi 

# membuat gabungan area rentang dari angka

# ++++++3---------10++++++

inputUser = float(input("masukan angka yang bernilai kurang dari 3 atau lebih besar dari 10 : "))

# ++++++3------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 = ",isKurangDari)

# ---------10+++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari 3 = ",isLebihDari)

# ++++++3---------10++++++

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan : ",isCorrect)




# ------3+++++++++10--------
# kasus irisan
inputUser = float(input("\nmasukan angka yang bernilai lebih besar dari 3 dan kurang dari 10 : "))

# ------3++++++++
isLebihDari = inputUser > 3
print("Lebih dari 3 = ",isLebihDari)

# ++++++++10---------
isKurangDari = inputUser < 10
print("kurang dari 10 = ",isKurangDari)

# ------3+++++++++10--------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan : ",isCorrect)


