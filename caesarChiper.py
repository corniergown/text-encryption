def caesar_chiper(text, space) -> str:
    code_text = []

    for char in text:
        if ( char.isalpha() ):
            if ( char.isupper() ):
                code_text.append(chr(((ord(char) - 65 + space) % 26) + 65))  # Manejar letras mayúsculas
            else:
                code_text.append(chr(((ord(char) - 97 + space) % 26) + 97))  # Manejar letras minúsculas
        else:
            code_text.append(char)
    
    return ''.join(code_text)
