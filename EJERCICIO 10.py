print("\n*** Nombre 1: Daniel Franco     Matricula: 3111928 ***")
print("*** Nombre 2: Juan Pablo Gallardo   Matricula: 3099039 ***\n")

print("*** Ejercicio 10 Nivel de influencer ***\n")

# input() guarda texto; el usuario es texto, así que no lo convertimos
usuario = input("\nTu usuario: @")

# int() convierte a número entero para poder comparar
seguidores = int(input("¿Cuántos seguidores tienes? "))
# Si el usuario escribe 25000, ahora seguidores vale 25000

print(f"\n===== NIVEL DE @{usuario} =====")

# PREGUNTA 1: ¿Tiene menos de 1000?
if seguidores < 1000:
    print("Nivel: Principiante")

# PREGUNTA 2: si llegamos aquí, YA SABEMOS que tiene 1000 o más
elif seguidores < 10000:
    print("Nivel: Microinfluencer")

# PREGUNTA 3: si llegamos aquí, YA SABEMOS que tiene 10000 o más
elif seguidores < 100000:
    print("Nivel: Influencer")

# else: si ninguna fue True, tiene 100000 o más
else:
    print("Nivel: Celebridad digital")