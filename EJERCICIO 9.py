print("\n*** Nombre 1: Daniel Franco     Matricula: 3111928 ***")
print("*** Nombre 2: Juan Pablo Gallardo   Matricula: 3099039 ***\n")

print("*** Ejercicio 9 Tamaño de tu bebida ***\n")

# Mostramos el menú para que el usuario sepa qué puede elegir
print("\n===== MENÚ DE TAMAÑOS =====")
print("1 = Chico  ($55)")
print("2 = Mediano ($70)")
print("3 = Grande  ($85)")

# input() pregunta y guarda la respuesta como TEXTO
# int() la convierte a número entero para poder compararla con 1, 2 y 3
opcion = int(input("\n¿Qué tamaño quieres? Escribe 1, 2 o 3: "))

if opcion == 1:
    print("Elegiste tamaño CHICO, son $55")
elif opcion == 2:
    print("Elegiste tamaño MEDIANO, son $70")
elif opcion == 3:
    print("Elegiste tamaño GRANDE, son $85")
else:
    print("Opción no válida, elige 1, 2 o 3")

# Esta línea no tiene sangría, no pertenece al if, por eso se muestra siempre
print("\n¡Gracias por tu compra!")