"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
def PedirNumero(numero:str)->int:
    num=None
    try:
        num=int(input(numero))
        if num<0:
            raise Exception
    except ValueError:
        print("***Error*** Número no válido")
    except Exception:
        print("***No puede ser valor negativo***")
    return num

def main():
    contador=1
    cadena=""
    num=PedirNumero("Introduce un numero: ")
    if num!=None:
        while contador<=num:
            cadena=cadena+str(contador)+", "
            contador+=2
    print(cadena[:-2:1])
    
if __name__ == "__main__":
    main()