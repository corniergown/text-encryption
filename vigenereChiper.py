def saludar():
    print("Soy el archivo VigenereChiper")


# Aqui comienza el codigo de VigenereChiper
def vigenere_chiper(text, key) -> str:
    result = ""
    key_index = 0
    key = key.upper()
    text = text.upper()
    
    for char in text:
        if char.isalpha():
            result += chr(((ord(char) + ord(key[key_index]) - 2 * 65) % 26) + 65)
            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            result += char
    return result