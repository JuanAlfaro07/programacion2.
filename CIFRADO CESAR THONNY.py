def cifrado_cesar(palabra, desplazamiento):
    resultado = ''
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                resultado += chr((ord(letra) - 65 + desplazamiento) % 26 + 65)
            elif letra.islower():
                resultado += chr((ord(letra) - 97 + desplazamiento) % 26 + 97)
        else:
            resultado += letra
    return resultado
palabra = input("Ingrese la palabra a cifrar: ")
desplazamiento = int(input("Ingrese el desplazamiento (+/-): "))
print("Palabra cifrada:", cifrado_cesar(palabra, desplazamiento))
