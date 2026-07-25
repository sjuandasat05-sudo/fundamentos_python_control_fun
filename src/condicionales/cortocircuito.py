# cortocircuito.py - evita errores usando and/or con evaluacion de cortocircuito
lista = []
if lista and lista[0] == "Python":
    print("El primer elemento es Python.")
else:
    print("La lista esta vacia, no se evaluo el segundo operando.")

divisor = 0
if divisor != 0 and 10 / divisor > 1:
    print("Resultado mayor que 1.")
else:
    print("No es posible dividir entre cero.")