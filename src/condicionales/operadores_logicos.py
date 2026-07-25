# operadores_logicos.py - and, or, not
edad = 25
ingresos = 30000
if edad >= 18 and ingresos >= 20000:
    print("Eres elegible para el credito.")

dia = "sabado"
if dia == "sabado" or dia == "domingo":
    print("Es fin de semana.")

llueve = False
if not llueve:
    print("Podemos salir al parque.")