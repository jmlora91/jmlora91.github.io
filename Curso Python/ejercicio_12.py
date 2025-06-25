#12. ¿Cuál de las siguientes declaraciones es inválida?
#a) abc = 1.000.000
#b) a b b c = 1000 2000 3000
#c) a,b,c = 1,000,000
#d) a_b_c = 1,000,000
#Solución: b) a b b c = 1000 2000 3000
# Esta función verifica cuál de las declaraciones es inválida en Python
def check_invalid_statements():
    """
    Verifica las declaraciones de variables y determina cuáles son inválidas.
    
    Las declaraciones que se verifican son:
    a) abc = 1.000.000
    b) a b b c = 1000 2000 3000
    c) a,b,c = 1,000,000
    d) a_b_c = 1,000,000
    """
    try:
        abc = 1.000.000  # Esto generará un SyntaxError
    except SyntaxError:
        print("a) abc = 1.000.000 es inválida")
    try:
        a b b c = 1000 2000 3000  # Esto generará un SyntaxError
    except SyntaxError:
        print("b) a b b c = 1000 2000 3000 es inválida")
    try:
        a, b, c = 1, 000, 000  # Esto es válido, pero 000 se trata como 0
        print("c) a,b,c = 1,000,000 es válida")
    except SyntaxError:
        print("c) a,b,c = 1,000,000 es inválida")
    try:
        a_b_c = 1, 000, 000  # Esto es válido, pero 000 se trata como 0
        print("d) a_b_c = 1,000,000 es válida")
    except SyntaxError:
        print("d) a_b_c = 1,000,000 es inválida")

check_invalid_statements()
print("Solución: b) a b b c = 1000 2000 3000 es inválida")