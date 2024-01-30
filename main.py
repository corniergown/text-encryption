import os
import caesarChiper as codeCaesar
import vigenereChiper as codeVigenere

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("Cifrado de texto!")
    print("1. Caesar Chiper")
    print("2. Vigenere Chiper")
    print("3. Salir")

def main():
    opt = int(input("Ingresa una opcion: "))

    if (opt == 1):
        codeCaesar.saludar()
        
    elif (opt == 2):
        codeVigenere.saludar()

    elif (opt == 3):
        print("Saliendo . . .\n")

if __name__ == '__main__':
    main()
