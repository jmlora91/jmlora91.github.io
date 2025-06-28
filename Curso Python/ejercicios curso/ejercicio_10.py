#10. Escribir un programa en Python para comprobar si un número es capicúa. Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.
def es_capicua(numero):
    """
    Función para comprobar si un número es capicúa.
    
    Un número es capicúa si se lee igual de derecha a izquierda que de izquierda a derecha.
    
    Parámetros:
    numero (int): El número a comprobar.
    
    Retorna:
    bool: True si el número es capicúa, False en caso contrario.
    """
    # Convertir el número a cadena para facilitar la comparación
    numero_str = str(numero)
    
    # Comparar la cadena con su reverso
    return numero_str == numero_str[::-1]

# Ejemplo de uso
numero = int(input("Introduce un número: "))
if es_capicua(numero):
    print(f"{numero} es capicúa.")
else:
    print(f"{numero} no es capicúa.")