def mostrar_resultado_calorias(total_calorias):
    if total_calorias > 400:
        mensaje = "Objetivo alcanzado"
    else:
        mensaje = "Objetivo no alcanzado"
    return mensaje

def planificador_ejercicios():
    total_calorias = 0
    
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        print(f"\n{dia}:")
        ejercicio = input("Ejercicio realizado (Correr, Caminar, Nadar, Abdominales, Descanso): ").capitalize()
        tiempo_minutos = float(input("Tiempo en minutos: "))
        
        if ejercicio == "Correr":
            calorias = (200 * tiempo_minutos) / 60
        elif ejercicio == "Caminar":
            calorias = (100 * tiempo_minutos) / 60
        elif ejercicio == "Nadar":
            calorias = (150 * tiempo_minutos) / 60
        elif ejercicio == "Abdominales":
            calorias = (120 * tiempo_minutos) / 60
        elif ejercicio == "Descanso":
            calorias = 0
        
        total_calorias += calorias
        print(f"Calorías quemadas: {calorias} calorías")
    
    mensaje = mostrar_resultado_calorias(total_calorias)
    print(f"\nTotal de calorías quemadas en la semana: {total_calorias} calorías\n{mensaje}")

# Llamada principal
planificador_ejercicios()

