# while_eventos.py - while con condicion de salida basada en eventos
saldo = 1000
gastos = [200, 150, 900, 0]  # 0 simula la senal de "salir"
i = 0
while saldo > 0 and i < len(gastos):
    gasto = gastos[i]
    i += 1
    if gasto == 0:
        break
    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue
    saldo -= gasto
    print(f"Gasto de {gasto}. Saldo actual: {saldo}")
print("Saldo final:", saldo)