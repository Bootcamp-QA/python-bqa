# Archivo: e2saludo.py

# Solicitar el nombre del usuario
nombre = input("Introduce tu nombre: ")

# Crear el saludo
saludo = "Hola, " + nombre + "!"

# Manipulaciones del saludo
longitud_saludo = len(saludo)
saludo_mayusculas = saludo.upper()
saludo_minusculas = saludo.lower()
saludo_reemplazo = saludo.replace("Hola", "Adios")

# Imprimir resultados
print("Saludo:", saludo)
print("Longitud del saludo:", longitud_saludo)
print("Saludo en mayúsculas:", saludo_mayusculas)
print("Saludo en minúsculas:", saludo_minusculas)
print("Saludo con reemplazo:", saludo_reemplazo)
