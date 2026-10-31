print("\n*** Nombre 1: Daniel Franco     Matricula: 3111928 ***")
print("*** Nombre 2: Juan Pablo Gallardo   Matricula: 3099039 ***\n")

print("*** Ejercicio 4 MIS ESTADÍSTICAS ***\n")

usuario = input("¿Cuál es tu usuario? ")
seguidores = int(input("¿Cuántos seguidores tienes? "))
likes = int(input("¿Cuántos likes tuvo tu último video? "))

if seguidores >= 1000:
    print("Ya puedes hacer lives")
else:
    print("Te faltan", 1000 - seguidores, "seguidores para hacer lives")

if likes > seguidores:
    print("¡Tu último video se hizo viral!\n")
else:
    print("Sigue publicando, vas bien\n")