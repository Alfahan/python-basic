def belajar_python(**student):
    print("Halo, Saya %s. Umur Saya %d" % (student['name'], student['age']))

# Memanggil Function belajar_python dengan Arbitrary Keyword Arguments
belajar_python(age=26, name="Alfa") # Halo, Saya Alfa. Umur Saya 26