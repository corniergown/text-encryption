import os
import caesarChiper as codeCaesar
import vigenereChiper as codeVigenere

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("\nCifrado de texto!\n")
    print("1. Caesar Chiper")
    print("2. Vigenere Chiper")
    print("3. Salir")

def main():
    menu()

    opt = int(input("\n~ Ingresa una opcion: "))
    clear_screen()

    if (opt == 1):
        text = str(input("\n~ Ingresa el texto a cifrar: "))
        shifts = int(input("~ Ingresa el numero de desplazamientos: "))

        clear_screen()
        print(f"\n[*] Texto cifrado: {codeCaesar.caesar_chiper(text, shifts)}")

    elif (opt == 2):
        # Entradad de datos para el cifrado de Vigenere
        text = str(input("\n~ Ingresa el texto a cifrar: "))
        key = str(input("~ Ingresa la clave: "))

        clear_screen()
        print(f"\n[*] Texto cifrado: {codeVigenere.vigenere_chiper(text, key)}")

    elif (opt == 3):
        print("Saliendo . . .\n")

    else:
        print("\nOpcion ivalida!")
        return 0

if __name__ == '__main__':
    main()
