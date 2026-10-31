
print("*** Nombre 1: Daniel Franco     Matrícula: 3111928 ***")
print("*** Nombre 2: Juan Pablo Gallardo   Matrícula: 3099039 ***\n")

print("*** Ejercicio 2 CREA TU CUENTA ***\n")

nombre = input("¿Cómo te llamas? ")
anio = int(input("¿En qué año naciste? "))
red_social = input("¿Cuál es tu red social favorita? ")

edad = 2026 - anio
print(nombre + ", tienes", edad, "años")

if edad >= 13:
    print("Tu cuenta en", red_social, "fue creada")
else:
    print("Todavía no puedes crear tu cuenta, te faltan", 13 - edad, "años")

if edad >= 18:
    print("Compras dentro de la app activadas\n")
else:
    print("Compras dentro de la app desactivadas\n")
