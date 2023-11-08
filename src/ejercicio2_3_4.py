"""
Escribir un programa que pida al usuario un número entero, 
si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""
def PedirNumero(numero:int)->str:
    if (type(numero)!= int):
        raise ValueError
    else:
        return print("La entrada es correcta.")

def main():
    try:
        numero=int(input("Introduce un numero entero: "))
        PedirNumero(numero)
    except ValueError:
        return  print("La entrada no es correcta.")

if __name__ == "__main__":
    main()