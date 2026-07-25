# pass_else.py - sentencia pass y clausula else en bucles
for numero in range(1, 6):
    if numero % 2 == 0:
        pass  # no hacemos nada con los pares
    else:
        print(f"Procesando numero impar: {numero}")

numeros = [4, 6, 8, 9, 10, 12]
for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"Encontrado un primo: {num}!")
        break
else:
    print("No se encontro ningun numero primo en la lista")