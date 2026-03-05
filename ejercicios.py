# Ejercicio 1: Saludo personalizado 

print("¿Cuál es tu nombre? ")
nombre = input()
print("¿Cuál es tu edad? ")
edad = input()
print(f"Hola {nombre}, me alegro que estes aprendiendo Python a los {edad} años de edad")


#Ejercicio 2: Calculadora de I.V.A.

print("¿Cual es el precio del producto del que desea calcular el I.V.A.?")
precio = float(input())
iva = precio * 0.21
print(f"El I.V.A. del producto deseado es de {iva} euros")


#Ejercicio 3: Mayor de edad

print("¿Cual es tu edad?")
edad = int(input())
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
if edad != int(input()):
    print("No has introducido un número válido")

#Alternativa 

print("¿Cual es tu edad?")
match edad:
    case edad if edad >= 18:
        print("Eres mayor de edad")
    case edad if  edad < 18:
        print("Eres menor de edad")
    case edad if edad !=int(input()):
        print("No has introducido un número válido")

#Ejercicio 4: Conversor de temperaturas farenheit 
print("¿Cual es la temperatura en grados farenheit que deseas convertir a grados celsius?")
celsius = float(input())
farenheit = (celsius * 9/5) + 32
print(f"{celsius} grados son equivalentes a {farenheit} grados farenheit")


#PYTHON STRINGS (metodos mas comunes)

string = "Hola mundo"
for letra in string:
    print(letra)

string = "Estoy programando en Python y me encanta"
print(string[0])
print(string[5])
print(type(string))
print(len(string))
print("python" in string)

#Ejercicio 5: validador de contraseñas
print("Introduce la contraseña: ")
llave = "python123"
contraseña = input().lower()
if contraseña == llave:
    print("Contraseña correcta, acceso concedido")
else: 
    print("Contraseña incorrecta, acceso denegado")


# Ejercicio 6: lista de la compra
print("¿Cuántos productos deseas comprar?")

# Guardamos la entrada en una variable primero
entrada = input()

if entrada.isdigit():
    # Usamos la variable que ya tenemos, no pedimos otra
    cantidad = int(entrada)
    lista = []
    
    # Es mejor avisar de qué número de producto toca introducir
    for i in range(cantidad):
        print(f"Introduce el producto {i+1}:")
        producto = input()
        lista.append(producto)
        
    print("\nTu lista de la compra es:")
    for producto in lista:
        print("-", producto)
else:
    print("Error: Tienes que introducir un número entero válido.")

#Ejercicio 7: contador de numeros pares
print("Introduce un número entero: ")
numero = int(input())
contadorPares = 0 
for i in range(0, numero+1):    # El rango va de 0 a numero+1 porque el rango no incluye el número final, entonces si queremos incluir el número que el usuario ha introducido, tenemos que poner numero+1
    if i % 2 == 0:
        contadorPares += 1      #
        print(i)
print(f"Hay {contadorPares} números pares entre 0 y {numero}")

#Ejercicio 8: contador de vocales
print("Introduce una frase: ")
frase = input().lower()
contadorVocales = 0
for letra in frase:
    if letra in "aeiou":
        contadorVocales += 1
print(f"Hay {contadorVocales} vocales en la frase que has introducido")

#Ejercicio 9: par o impar
print("introduce un numero entero: ")
entrada = input()
if entrada.isdigit():
    numero = int(entrada)
    if numero % 2 ==0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")
else:
    print(f"Error: {entrada} no es un número entero válido")

#Ejercicio 10: generador de tablas de multiplicar
print("Introduce un número entero para generar su tabla de multiplicar: ")
entrada = input()
if entrada.isdigit():
    numero = int(entrada)
    print(f"Tabla de multiplicar del {numero}: ")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Error: No has introducido un número entero válido")
    
#Ejercicio 11: gestion de inventario
frutas = ["manzana", "platano", "cereza"]
print("¿Qué fruta deseas agregar al inventario?")
nueva_fruta = input().lower()
frutas.append(nueva_fruta)
print("Debes eliminar una fruta del inventario, ¿Cuál deseas eliminar?")
fruta_eliminar = input().lower()
frutas.remove(fruta_eliminar)
print("El inventario actualizado es: ")
for fruta in frutas:
    print(f"- {fruta}")

#Ejercicio 12: coordenadas inmutables
coordenadas = (10, 20)
try:
    coordenadas.append(30)  # Esto generará un error porque las tuplas son inmutables
except AttributeError as e:
    print("Error: No se pueden modificar las coordenadas porque son inmutables.")
    print(e)

#Ejercicio 13: invitados unicos
lista1 = ["Juan", "Maria", "Pedro", "Ana", "Jose"]
lista2 = ["Ana", "Maria", "Luis", "Carlos", "Jose"]
invitados_unicos = set(lista1) | set(lista2)  # Usamos la unión de conjuntos para obtener los invitados únicos
print("La lista de invitados únicos es: ")
print("La lista de invitados únicos es: ")
for invitado in invitados_unicos:
    print(f"- {invitado}")

# Ejercicio 14: diccionario de traducciones
# Diccionario inicial
traducciones = {
    "red": "rojo",
    "blue": "azul",
    "green": "verde"
}

color_buscado = input("Introduce un color en inglés: ").lower().strip()

# Comprobamos si la clave existe en el diccionario
if color_buscado in traducciones:
    print(f"La traducción de '{color_buscado}' es: {traducciones[color_buscado]}")
else:
    print(f"Lo siento, no conozco el color '{color_buscado}'.")
    
    # "Enseñamos" al programa
    nueva_traduccion = input(f"¿Cómo se dice '{color_buscado}' en español? ")
    
    # Añadimos el nuevo par clave-valor
    traducciones[color_buscado] = nueva_traduccion
    print("¡Gracias! He actualizado mi diccionario.")

# Imprimimos el estado final del diccionario
print("\nDiccionario actualizado:")
for ingles, espanol in traducciones.items():
    print(f"{ingles} -> {espanol}")

#Ejercicio 15: analista de textos
#No esta del todo bien
print("Introduce una frase larga: ")
frase = input()
palabras = frase.split()
contador = 0 
for palabra in palabras:
    contador +=1
print(f"Hay tantas palabras {contador} en tu frase")
unicas = set(frase.split())
contador2 = 0
for unica in unicas:
    contador2 +=1
print(f"Hay tantas palabras unicas : {contador2} y son : {unicas}")

#Alternativa 

print("Introduce una frase larga: ")
frase = input()
palabras = frase.split()    #queremos dividir en palabaras la cadena de texto
contadorFrase = len.palabras()
print(f"Hay tantas palabras {contadorFrase} en la frase {frase}")
unicas = set(palabras)
print(f"Estas son las palabras no repetidas:  {unicas}")

#Ejercicio 16: registro de alumnos (diccionario mas tuplas)
print("Ingrese al informacion del alumno: ")
print("Nombre: ")
nombre = input()
print("Edad: ")
edad = input()
print("Nota: ")
nota = input()
diccionario = {
    nombre: (edad,nota)
}
print("Ingrese el valor que desea buscar dentro del diccionario")
valor = input()
if valor in diccionario:
    datos = diccionario[valor]
    print(f"Informacion de {valor}: ")
    print(f" - Edad: {datos[0]}")
    print(f" - Edad: {datos[1]}")
else:
    print(f"No se encuentras {valor} en el diccionario")

#Ejercicio 17: control de acceso

autorizados = {"Carla", "Pedro", "Marta"}
print("¿Cual es tu nombre?")
nombre = input()
if nombre in autorizados:
    print(f"Bienvenido, {nombre}, estas en la lista de autorizados")
else:
    print("¿Quieres añadir tu nombre a la lista?")
    respuesta = input().lower
    if respuesta == "si":
        autorizados.append(nombre)
        print(autorizados)
    else:
        print("hasta luego")



