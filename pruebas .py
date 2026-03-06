texto = input("Introduce el texto: ")
n = int(input("Desplazamiento: "))
accion = input("¿Cifrar o descifrar? (c/d): ")

if accion == "d":
    n = -n          # ← descifrar es simplemente desplazar al revés

resultado = ""

for caracter in texto:
    if caracter.isalpha():
        if caracter.islower():
            # cifra minúscula...
            resultado += chr((ord(caracter) - ord("a") + n) % 26 + ord("a"))
        else:
            # cifra mayúscula... (mismo esquema pero con ord("A"))
            resultado += chr((ord(caracter) - ord("A") + n) % 26 + ord("A"))
    else:
        resultado += caracter    # ← espacios y símbolos sin cambios

print(resultado)