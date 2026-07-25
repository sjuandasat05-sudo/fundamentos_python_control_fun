# break_continue.py - control de flujo dentro de bucles
for numero in range(1, 11):
    if numero == 5:
        print("Encontrado el 5! Saliendo del bucle...")
        break
    print(f"Numero actual: {numero}")

for numero in range(1, 11):
    if numero % 2 == 0:
        continue
    print(f"Numero impar: {numero}")