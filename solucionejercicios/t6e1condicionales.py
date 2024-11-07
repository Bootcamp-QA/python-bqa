# Archivo: e1condicionales.py

# Definir la función para comparar dos números
def comparar_numeros(num1, num2):
    if num1 > num2:
        return "El primer número es mayor que el segundo."
    elif num1 < num2:
        return "El primer número es menor que el segundo."
    else:
        return "Ambos números son iguales."

# Solicitar al usuario dos números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Comparar y mostrar el resultado
resultado = comparar_numeros(numero1, numero2)
print(resultado)
