#01. Dados dos números, escriba un código Python para encontrar el mínimo de estos dos números
def encontrar_minimo(num1, num2):
    """
    Encuentra el número mínimo entre dos números.

    Esta función recibe dos números y devuelve el más pequeño. 
    Si num1 es menor que num2, devuelve num1; de lo contrario, devuelve num2.

    Args:
        num1 (int, float): El primer número a comparar.
        num2 (int, float): El segundo número a comparar.

    Returns:
        int, float: El número más pequeño entre num1 y num2.
    """
    return num1 if num1 < num2 else num2

# Programa para encontrar el número más pequeño entre dos números introducidos por el usuario
# Solicita al usuario que introduzca dos números y muestra el más pequeño
# Solicita al usuario que introduzca el primer número
numero1 = float(input("Introduce el primer número: "))
# Solicita al usuario que introduzca el segundo número
numero2 = float(input("Introduce el segundo número: "))
# Llama a la función encontrar_minimo con los dos números introducidos
minimo = encontrar_minimo(numero1, numero2)
# Imprime el resultado en la consola
print("El número más pequeño es: {minimo}")