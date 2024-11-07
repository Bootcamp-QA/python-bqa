# Archivo: e2area_triangulo.py

# Definir la función para calcular el área de un triángulo
def calcular_area_rectangulo(base, altura):
    return (base * altura)

# Solicitar al usuario la base y la altura
base = float(input("Introduce la base del triángulo: "))
altura = float(input("Introduce la altura del triángulo: "))

# Calcular y mostrar el área
area = calcular_area_rectangulo(base, altura)
print(f"El área del triángulo es: {area}")


