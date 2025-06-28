#06. Escriba un código que pueda contar todas las palabras mayúsculas de un archivo
def contar_palabras_mayusculas(archivo):
    """
    Cuenta el número de palabras en un archivo que están en mayúsculas.

    Args:
        archivo (str): La ruta del archivo de texto que se va a leer.

    Returns:
        int: El número de palabras en mayúsculas encontradas en el archivo.
    """
    with open(archivo, 'r') as f:
        texto = f.read()
    palabras = texto.split()
    contador = sum(1 for palabra in palabras if palabra.isupper())
    return contador

# Llamada a la función con la ruta del archivo
ruta_archivo = '/Users/macbookpro/Desktop/Josema/Curso HTML/GitHub/jmlora91.github.io/Curso Python/ejercicio_06.py'
print(f'Número de palabras mayúsculas: {contar_palabras_mayusculas(ruta_archivo)}')