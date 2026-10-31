print("\n*** Nombre 1: Daniel Franco     Matricula: 3111928 ***")
print("*** Nombre 2: Juan Pablo Gallardo   Matricula: 3099039 ***\n")

print("*** Ejercicio MI META DE AHORRO ***\n")

producto = input("¿Qué quieres comprar? ")
precio = float(input("¿Cuánto cuestan? "))
ahorrado = float(input("¿Cuánto tienes ahorrado? "))
ahorro_semanal = float(input("¿Cuánto ahorras por semana? "))

if ahorrado >= precio:
    print("¡Ya puedes comprar tus", producto + "!")
else:
    faltante = precio - ahorrado
    semanas = faltante / ahorro_semanal
    print("Te faltan $", faltante, " para tus ", producto, sep="")
    print("Ahorrando $", ahorro_semanal, " por semana, los tendrás en ", semanas, " semanas", sep="")

print("\n")