# kita belajar casting
# merubah dari satu tipe ke tipe yang lain

print("======INTEGER======")
data_int = 9;
print("data = ",data_int,",type = ",type(data_int))

data_float = float(data_int) ;
data_str   = str(data_int);
data_bool  = bool(data_int); # akan false jika nilai int = 0
print("data = ",data_float,",type = ",type(data_float))
print("data = ",data_str,",type = ",type(data_str))
print("data = ",data_bool,",type = ",type(data_bool)) 

print("======FLOAT======")
data_float = 9;
print("data = ",data_float,",type = ",type(data_float))

data_int = int(data_float); # akan dibulatkan ke bawah
data_str   = str(data_float);
data_bool  = bool(data_float); # akan false jika nilai float = 0
print("data = ",data_int,",type = ",type(data_int))
print("data = ",data_str,",type = ",type(data_str))
print("data = ",data_bool,",type = ",type(data_bool)) 

print("======BOOLEAN======")
data_bool = False;
print("data = ",data_bool,",type = ",type(data_bool))

data_int  = int(data_bool); 
data_float = float(data_bool) ;
data_str   = str(data_bool); # akan tertulis sesuai boolean nya
print("data = ",data_int,",type = ",type(data_int))
print("data = ",data_float,",type = ",type(data_float)) 
print("data = ",data_str,",type = ",type(data_str))

print("======STRING======")
data_str = "10";
print("data = ",data_str,",type = ",type(data_str))

data_int   = int(data_str); # string harus angka jika tidak maka error
data_float = float(data_str) ;# string harus angka jika tidak maka error
data_bool  = bool(data_str); # false jika string kososng
print("data = ",data_int,",type = ",type(data_int))
print("data = ",data_float,",type = ",type(data_float))
print("data = ",data_bool,",type = ",type(data_bool)) 