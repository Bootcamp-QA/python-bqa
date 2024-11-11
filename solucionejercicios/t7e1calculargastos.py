def calcular_gasto_semana(comida, ocio, vivienda):
    total_semana = comida + ocio + vivienda
    return total_semana

def mostrar_resultado_gasto(gasto_mes):
    if gasto_mes > 800:
        mensaje = "Gasto elevado (mayor a 800 €)"
    elif gasto_mes < 300:
        mensaje = "Gasto bajo (menor a 300 €)"
    else:
        mensaje = "Gasto normal"
    return mensaje

def calcular_gasto_total():
    mes = input("Introduce el nombre del mes: ").upper()
    gasto_mes = 0
    
    for semana in range(1, 5):
        print(f"\nSemana {semana}:")
        comida = float(input("Gasto en comida: "))
        ocio = float(input("Gasto en ocio: "))
        vivienda = float(input("Gasto en vivienda: "))
        
        total_semana = calcular_gasto_semana(comida, ocio, vivienda)
        print(f"Gasto total en la semana {semana}: {total_semana} €")
        gasto_mes += total_semana
    
    mensaje = mostrar_resultado_gasto(gasto_mes)
    print(f"\nGasto total en {mes}: {gasto_mes} €\n{mensaje}")


calcular_gasto_total()

