data = "ini adalah string"
print(data)
print(type(data))

# 1 cara membuat string

# dengan menggunakan single quote '...'
# dengan menggunakan double quote "..."

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar"')
print("'Halo, apa kabar'")
print("ini adalah hari jum'at")

# 2 menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\Fiuls")

# tab
print("gunakan\t\tini untuk memberi space lebih")

# backspace
print("gunakan, \bini untuk mengurangi space ")

# newline
print("Baris pertama.\nbaris kedua") # LF -> line feed -> unix,macos,linux
print("Baris pertama.\rbaris kedua") # CR -> carriage return -> commodorn,corn
print("Baris pertama.\r\nbaris kedua") # CRLF -> line feed carriage return -> windows

# 3 string literal atau raw

# hati hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Faisal ibnul hakim
Kelamin : Laki laki
""")

# multiline literal string dan raw
print(r"""
Nama : Faisal ibnul hakim
Kelamin : Laki laki \ man
website : 203040027.pw.id.unpas.ac.id
""")