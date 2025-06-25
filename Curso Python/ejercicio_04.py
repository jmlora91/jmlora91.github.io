#04. Escriba un código que calcule una lista de números proporcionados.
def suma_lista(numeros):
    """
    Suma todos los números en una lista.

    Args:
        numeros (list): Una lista de números (int o float) que se desea sumar.

    Returns:
        int or float: La suma total de los números en la lista.
    """
    return sum(numeros)
numeros = [1, 2, 3, 4, 5] 
resultado = suma_lista(numeros)
print("La suma de la lista es:", resultado)