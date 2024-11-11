# Lista de los meses del año
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def mostrar_mes(numero):
    if 1 <= numero <= 12:
        mes = meses[numero - 1]
        if mes == "Junio":
            mensaje = mes + " EL MEJOR MES"
        else:
            mensaje = "El mes correspondiente es: " + mes
    else:
        mensaje = "Número inválido, introduce un número entre 1 y 12."
    return mensaje

# Solicitar al usuario que ingrese un número del 1 al 12
numero = int(input("Introduce un número del 1 al 12 para conocer el mes: "))

# Llamar a la función y mostrar el resultado
resultado = mostrar_mes(numero)
print(resultado)
