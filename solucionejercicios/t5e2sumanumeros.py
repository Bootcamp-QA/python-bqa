def suma(numero1,numero2):
    total = numero1 + numero2
    return total
# Solicitar al usuario la base y la altura
numero1 = float(input("Introduce un numero "))
numero2 = float(input("Introduce otro numero: "))

# Calcular y mostrar el área
total = suma(numero1,numero2)
print("El total de la suma es:", total)