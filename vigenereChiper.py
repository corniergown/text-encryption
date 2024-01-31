def vigenere_chiper(text, key) -> str:
    result = ""
    key_index = 0
    key = key.upper()
    text = text.upper()
    
    for char in text:
        if char.isalpha(): # Evalua si el caracter es una letra
            result += chr(((ord(char) + ord(key[key_index]) - 2 * 65) % 26) + 65) #Cifrado de Vigenere
            key_index += 1

            if key_index == len(key): # Si el indice de la clave es igual a su longitud, se reinicia
                key_index = 0
        else:
            result += char
    return result
