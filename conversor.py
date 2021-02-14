pesos = input("¿Cuántoas soles tienes?: ")
pesos = float(pesos)
valor_dolar = 3.6
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

print("Tienes $" + dolares + " dolares")
