#8. Escriba un programa para producir la serie Fibonacci en Python.

def fibonacci(n):
    """
    Generar una serie de Fibonacci de longitud n.

    La serie de Fibonacci es una secuencia de números donde cada número 
    es la suma de los dos anteriores, comenzando generalmente con 0 y 1.

    Parámetros:
    n (int): La longitud de la serie de Fibonacci a generar.

    Retorna:
    list: Una lista que contiene la serie de Fibonacci de longitud n.
    """
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

num_elements = int(input("¿Cuántos elementos de la serie Fibonacci desea? "))
print(fibonacci(num_elements))