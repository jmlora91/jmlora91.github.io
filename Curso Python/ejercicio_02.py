#2. Invertir palabras de una cadena dada.
def invertir_cadena(cadena):
    """
    Invierte una cadena de texto.

    Args:
        cadena (str): La cadena de texto que se desea invertir.

    Returns:
        str: La cadena de texto invertida.
    """
    return cadena[::-1]

def invertir_palabras(cadena):
    """
    Invierte el orden de las palabras en una cadena de texto.

    Args:
        cadena (str): La cadena de texto cuyas palabras se desean invertir.

    Returns:
        str: Una nueva cadena con las palabras en orden inverso.
    
    Ejemplo:
        >>> invertir_palabras("Hola mundo")
        "mundo Hola"
    """
    return ' '.join(cadena.split()[::-1])

# Ejemplo de uso
cadena = "Hola Mundo"
print(invertir_cadena(cadena))


# Ejemplo de uso para la nueva función
cadena_invertida = invertir_palabras(cadena)
print(cadena_invertida)