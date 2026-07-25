# docstrings.py - documentacion de funciones con docstrings
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de numeros.

    Args:
        numeros: lista de valores numericos

    Returns:
        El promedio como valor flotante
    """
    return sum(numeros) / len(numeros)

def es_mayor_de_edad(edad):
    """Determina si una persona es mayor de edad (18 anos o mas)."""
    return edad >= 18

print(calcular_promedio.__doc__)
print("Promedio:", calcular_promedio([10, 20, 30]))
print("Es mayor de edad:", es_mayor_de_edad(20))