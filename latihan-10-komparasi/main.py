# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,!=,is,is not

a = 4
b = 2

# lebih besar dari >

print("======LEBIH BESAR DARI (>)======")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari <

print("======KURANG DARI (<)======")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# leboh dari sama dengan >=

print("======LEBIH DARI SAMA DENGAN (>=)======")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <=

print("======KURANG DARI SAMA DENGAN (<=)======")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan ==

print("======SAMA DENGAN (==)======")
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)

# tidak sama dengan !=

print("======TIDAK SAMA DENGAN (!=)======")
hasil = a != 3
print(a,'!=',3,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)

# 'is' sebagai komparasi object identity
print("======OBJECT IDENTITY (is)======")
x = 5 # ini adalah assignment membuat object
y = 5 
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

x = 6 # ini adalah assignment membuat object
y = 5 
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

# 'is not' sebagai komparasi object identity
print("======OBJECT IDENTITY (is not)======")
x = 5 # ini adalah assignment membuat object
y = 5 
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is not y = ', hasil)

x = 6 # ini adalah assignment membuat object
y = 5 
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is not y = ', hasil)