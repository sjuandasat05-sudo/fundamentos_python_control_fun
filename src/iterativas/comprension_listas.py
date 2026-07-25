# comprension_listas.py - crear listas de forma concisa con for
cuadrados = [x**2 for x in range(1, 6)]
print("Cuadrados:", cuadrados)

pares = [x for x in range(10) if x % 2 == 0]
print("Pares:", pares)