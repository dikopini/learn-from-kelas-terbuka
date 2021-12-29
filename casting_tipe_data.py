# kita belajar casting
# merubah dari satu tipe data ke tipe data yang lain
# tipe data = int, str, float, bool

#INTEGER
print("====INTEGER====")
data_int = 9
print(f"data = {data_int}, type data = {type(data_int)}")

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print(f"data = {data_float}, type data = {type(data_float)}")
print(f"data = {data_str}, type data = {type(data_str)}")
print(f"data = {data_bool}, type data = {type(data_bool)}")

#FLOAT
print("\n====FLOAT====")
data_float = 9.5
print(f"data = {data_float}, type data = {type(data_float)}")

data_int = int(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilainya = 0
print(f"data = {data_int}, type data = {type(data_int)}")
print(f"data = {data_str}, type data = {type(data_str)}")
print(f"data = {data_bool}, type data = {type(data_bool)}")

#BOOLEAN
print("\n====BOOLEAN====")
data_bool = True
print(f"data = {data_bool}, type data = {type(data_bool)}")

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print(f"data = {data_int}, type data = {type(data_int)}")
print(f"data = {data_str}, type data = {type(data_str)}")
print(f"data = {data_float}, type data = {type(data_float)}")

#STRING
print("\n====STRING====")
data_str = "10"
print(f"data = {data_str}, type data = {type(data_str)}")

data_int = int(data_str)
data_bool = bool(data_str)
data_float = float(data_str)
print(f"data = {data_int}, type data = {type(data_int)}")
print(f"data = {data_bool}, type data = {type(data_bool)}")
print(f"data = {data_float}, type data = {type(data_float)}")