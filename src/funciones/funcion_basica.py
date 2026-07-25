# funcion_basica.py - definicion y llamado de funciones
def saludar():
    print("Hola, mundo!")

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

saludar()
resultado = calcular_area_rectangulo(5, 3)
print(f"El area del rectangulo es: {resultado}")