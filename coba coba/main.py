tb = int(input("Tinggi badan anda dalam centimeter = "))
tb = tb/100
print("Tinggi badan anda dalam meter= ",tb)
bb = int(input("Berat badan anda = "))
bmi = (bb/(tb*tb))
print("Body Mass Index anda = ",bmi)

if(bmi >= 25):
    print("OLAHRAGA GOBLOK JANGAN CUMA DIEM DI RUMAH")
elif(bmi <= 18):
    print("ANDA KURANG MAKAN, MAKANLAH MAKANAN BERGIZI")
elif(bmi > 18 & bmi < 25):
    print("BMI ANDA SUDAH BAGUS PERTAHANKAN")