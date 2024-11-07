def manipular_lista_numeros():
    # Declarar lista de números
    numeros = [1, 2, 3, 4, 5]
    
    # Agregar un nuevo número a la lista
    numeros.append(6)
    
    # Eliminar un número de la lista
    numeros.remove(3)  # Puedes cambiar el número a eliminar
    
    # Imprimir la lista actualizada y su longitud
    print("Lista actualizada de números:", numeros)
    print("Longitud de la lista:", len(numeros))
    
    # Mostrar el primer número de la lista
    print("Primer número de la lista:", numeros[0])


# Llamada a la función
manipular_lista_numeros()