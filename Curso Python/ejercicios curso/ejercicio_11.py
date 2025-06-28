#11. Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.
def ordenar_datos(datos):
    """
    Ordena un conjunto de datos numéricos utilizando el algoritmo de ordenación por burbuja.

    Parámetros:
    datos (list): Lista de números a ordenar.

    Retorna:
    list: Lista de números ordenados.
    """
    n = len(datos)
    # Recorremos todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Si el elemento encontrado es mayor que el siguiente
            if datos[j] > datos[j+1]:
                # Intercambiamos si están en el orden incorrecto
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos

# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
numeros_ordenados = ordenar_datos(numeros)
print("Lista ordenada:", numeros_ordenados)