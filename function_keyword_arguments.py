def belajar_python(name, age):
    print("Halo, Saya %s. Umur Saya %d" % (name, age))

# Contoh Function di atas. Jika kita memanggil Function dan mengirim Arguments tanpa nama "key" nya
# maka kita harus menuliskannya secara berurutan (name, age)
belajar_python("Ali", 26) # Halo, Saya Ali. Umur Saya 25

# Tetapi jika kita memanggil Function dan mengirim Arguments dengan nama "key" nya
# maka kita tidak harus menulliskannya secara berurutan (age, name)
belajar_python(age = 25, name="Alfa") # Halo, Saya Alfa. Umur Saya 25