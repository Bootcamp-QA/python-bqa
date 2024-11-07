# Definir la función para calcular el área de un triángulo
def calcular_area_rectangulo(base, altura):
    area = (base * altura)
    return area

# Solicitar al usuario la base y la altura
base = float(input("Introduce la base del triángulo: "))
altura = float(input("Introduce la altura del triángulo: "))

# Calcular y mostrar el área
area = calcular_area_rectangulo(base, altura)
print("El área del triángulo es:", area)


