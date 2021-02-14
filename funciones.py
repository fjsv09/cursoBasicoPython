# def imprimir_mensaje():
#     print("Mensaje especial")
#     print("Estoy aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(mensaje):
    print("Hola")
    print("Cómo estás")
    print("Eligiste la opción " + mensaje)
    print("Adios")


opcion = input("Elige una opción (1, 2, 3): ")

if opcion == "1":
    conversacion(opcion)
elif opcion == "2":
    conversacion(opcion)
elif opcion == "3":
    conversacion(opcion)
else:
    print("Escribe la opción correcta")
