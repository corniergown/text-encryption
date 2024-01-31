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
        # Entradad de datos para el cifrado de Vigenere
        text = str(input("~ Ingresa el texto a cifrar: "))
        key = str(input("~ Ingresa la clave: "))

        print(f"[*] Texto cifrado: {codeVigenere.vigenere_chiper(text, key)}")

    elif (opt == 3):
        print("Saliendo . . .\n")

if __name__ == '__main__':
    main()
