print("\n*** Nombre 1: Daniel Franco     Matricula: 3111928 ***")
print("*** Nombre 2: Juan Pablo Gallardo   Matricula: 3099039 ***\n")

print("*** Ejercicio 12 Playlist según tu mood ***\n")

# Mostramos el menú de opciones
print("\n===== ¿CÓMO TE SIENTES HOY? =====")
print("1 = Feliz")
print("2 = Triste")
print("3 = Con energía")
print("4 = Estudiando")

# int() convierte el texto a número para compararlo con 1, 2, 3 y 4
mood = int(input("\nEscribe el número de tu mood: "))
# Si el usuario escribe 4, ahora mood vale 4

# Python revisa en orden y se detiene en la primera que sea True
if mood == 1:
    print("Te recomiendo una playlist de pop")
elif mood == 2:
    print("Te recomiendo una playlist de baladas")
elif mood == 3:
    print("Te recomiendo una playlist de reggaetón o K-pop")
elif mood == 4:
    print("Te recomiendo una playlist de lo-fi para concentrarte")
else:
    print("Ese mood no está en la lista")