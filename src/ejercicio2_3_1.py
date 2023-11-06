"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""


def PedirEdad(anios: str)->int:
    edad=None
    try:
        edad=int(input(anios))
        if edad<0:
            raise Exception
    except ValueError:
        print("***Error*** Edad no válida.")
    except Exception:
        print("***No puede ser negativa***")
    return edad


def main():
    contador=1
    edad=PedirEdad("Introduce su edad: ")
    if edad!=None:
        while contador<=edad:
            print(contador)
            contador+=1

if __name__ == "__main__":
    main()