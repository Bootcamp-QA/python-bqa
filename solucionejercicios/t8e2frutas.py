# Archivo: e2frutas.py

def manipular_lista_frutas():
    # Declarar lista de frutas
    frutas = ["manzana", "banana", "naranja", "uva"]
    
    # Agregar una nueva fruta a la lista
    frutas.append("pera")
    
    # Eliminar una fruta de la lista
    frutas.remove("naranja")  # Puedes cambiar la fruta a eliminar
    
    # Imprimir la lista actualizada y su longitud
    print("Lista actualizada de frutas:", frutas)
    print("Longitud de la lista:", len(frutas))
    
    # Mostrar la primera fruta de la lista
    if frutas:
        print("Primera fruta de la lista:", frutas[0])
    else:
        print("La lista está vacía.")

# Llamada a la función
manipular_lista_frutas()
