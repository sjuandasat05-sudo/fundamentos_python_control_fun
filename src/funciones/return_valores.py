# parametros_argumentos.py - tipos de parametros
def saludar(nombre, mensaje="Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

def sumar(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

saludar("Carlos")                       # usa mensaje predeterminado
saludar("Maria", "Como estas?")         # mensaje personalizado
saludar(nombre="Luis", mensaje="Hey!")  # argumento por nombre

print("Suma:", sumar(1, 2, 3, 4))       # *args

mostrar_info(nombre="Python", anio=1991)  # **kwargs