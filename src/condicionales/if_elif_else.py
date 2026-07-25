# if_elif_else.py - Multiples condiciones en cadena
nota = 87
if nota >= 90:
    print("Calificacion: Sobresaliente")
elif nota >= 80:
    print("Calificacion: Notable")
elif nota >= 70:
    print("Calificacion: Aprobado")
else:
    print("Calificacion: Suspenso")

edad = 45
if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 anos.")