# match_case.py - Coincidencia de patrones (Python 3.10+)
fruta = "naranja"
match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case _:
        print("Fruta desconocida.")

punto = (0, 5)
match punto:
    case (0, 0):
        print("El punto esta en el origen.")
    case (0, y):
        print(f"El punto esta en el eje Y en y={y}.")
    case (x, y):
        print(f"El punto esta en x={x}, y={y}.")