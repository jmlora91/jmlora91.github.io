#09. Escriba un programa en Python para comprobar si un número es primo.
def es_primo(numero):
    """
    Función para comprobar si un número es primo.
    
    Un número es primo si es mayor que 1 y no tiene divisores
    positivos aparte de 1 y sí mismo.

    Parámetros:
    numero (int): El número a comprobar.

    Retorna:
    bool: True si el número es primo, False en caso contrario.
    """
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicitar al usuario un número
numero_usuario = int(input("Introduce un número: "))
if es_primo(numero_usuario):
    print("Es primo")
else:
    print("No es primo")