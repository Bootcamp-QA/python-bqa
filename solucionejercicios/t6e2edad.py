# Archivo: e2edad.py

# Definir la función para categorizar la edad
def clasificar_edad(edad):
    if edad < 18:
        return "Eres menor de edad."
    elif 18 <= edad < 65:
        return "Eres adulto."
    else:
        return "Eres senior."

# Solicitar al usuario su edad
edad = int(input("Introduce tu edad: "))

# Determinar la categoría de edad y mostrar el resultado
mensaje = clasificar_edad(edad)
print(mensaje)
