#5. Escriba un código que desordene al azar una lista.

import random

def desordenar_lista(lista):
    random.shuffle(lista)
    return lista

# Ejemplo de uso
mi_lista = ["manzana", "banana", "cereza", "datil"]
lista_desordenada = desordenar_lista(mi_lista)
print(lista_desordenada)