import time
start_time = time.time()

print("hello")
print("world")
print("Hello World")

# ini adalah comment
a = 10 # ini adalah coment juga
""""ada apa dengan kamu
dalam comment multiline"""
print(a)
print(time.time() - start_time, "detik")
# kita bisa mengcompile python ke
# yang namanya bytecode
# cara mengompile, buka terminal dan tuliskan
# python -m py_compile main.py