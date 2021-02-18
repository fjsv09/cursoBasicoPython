import random


def generador_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E']
    minusculas = ['a', 'b', 'c', 'd', 'e']
    simbolos = ['!', '#', '&', '/']
    numeros = ['1', '2', '3', '5', '6']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = ''.join(contrasena)
    return contrasena


def run():
    contrasena = generador_contrasena()
    print('Tu nueva contrasena es: ' + contrasena)


if __name__ == '__main__':
    run()
