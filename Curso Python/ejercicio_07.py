#7. ¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que sería la lista 1 [-1]?
#Solución:"-1" siempre se refiere al último índice de la lista, por lo tanto, la respuesta seria 3.
def get_last_element(lst):
    """
    Returns the last element of a given list.

    Parameters:
    lst (list): The list from which to retrieve the last element.

    Returns:
    The last element of the list. If the list is empty, an IndexError will be raised.
    """
    return lst[-1]

lista_1 = [4, 6, 8, 1, 0, 3]
resultado = get_last_element(lista_1)
print(f"¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que sería la lista 1 [-1]?")
print(f"-1 siempre se refiere al último índice de la lista, por lo tanto, la respuesta sería {resultado}")