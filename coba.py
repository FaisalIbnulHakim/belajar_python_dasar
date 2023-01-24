nilai = int(input("masukan nilai: "))

if(nilai > 100):
    print("Nilai lebih dari batas maximum input")
elif (nilai >= 80):
    print("A")
elif (nilai >= 70):
    print("B")
elif (nilai >= 60):
    print("C")
elif (nilai >= 40):
    print("D")
elif (nilai < 0):
    print("Nilai kurang dari batas minimum input")
else :
    print("E")