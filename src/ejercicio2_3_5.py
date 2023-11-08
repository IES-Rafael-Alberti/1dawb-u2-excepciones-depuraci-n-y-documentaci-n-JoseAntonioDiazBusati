"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""

def PedirPassword(contrasenia:str)->str:
    password="Pass word"
    if(contrasenia==password):
        print("Bienvenido")
    else:
        raise NameError

def main():
    try:
        contrasenia=str(input("Introduce la contraseña: "))
        PedirPassword(contrasenia)
    except NameError:
        print("Incorrect Password!!")

if __name__ == "__main__":
    main()