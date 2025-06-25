#3. Realizar una suma de los elementos de una tupla
def suma_tupla(tupla):
    """
    Suma todos los elementos de una tupla numérica.

    Args:
        tupla (tuple): Una tupla que contiene números.

    Returns:
        int or float: La suma de los elementos de la tupla.
    """
    return sum(tupla)

# Ejemplo de uso
resultado = suma_tupla((1, 2, 3, 4, 5))
print(resultado)  # Salida: 15