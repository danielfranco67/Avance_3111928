
print("\n*** Nombre 1: Daniel Franco   Matrícula: 3111928 ***")
print("*** Nombre 2: Juan Pablo Gallardo   Matrícula: 3099039 ***\n")

print("*** Ejercicio 1: Estado de mi celular ***\n")

bateria = int(input("¿Cuanta bateria tienes?"))
espacio = int(input("¿Cuántos GB libres tienes? "))
notificaciones = int(input("¿Cuántas notificaciones sin leer tienes? "))

if bateria <= 20:
    print("Batería baja, conecta tu cargador")

if espacio < 5:
    print("Poco espacio, borra fotos o apps que no uses")

if notificaciones > 0:
    print("Tienes", notificaciones, "notificaciones sin leer\n")
else:
    print("Estás al día, no tienes notificaciones\n")




