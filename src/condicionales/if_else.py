# if_else.py - Estructura if-else
numero = 15
if numero % 2 == 0:
    print("El numero es par.")
else:
    print("El numero es impar.")

saldo = 300
retiro = 500
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso. Nuevo saldo:", saldo)
else:
    print("Fondos insuficientes. Saldo actual:", saldo)