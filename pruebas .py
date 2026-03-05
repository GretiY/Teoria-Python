autorizados = {"Carla", "Pedro", "Marta"}
print("¿Cual es tu nombre?")
nombre = input()
if nombre in autorizados:
    print(f"Bienvenido, {nombre}, estas en la lista de autorizados")
else:
    print("¿Quieres añadir tu nombre a la lista?")
    respuesta = input().lower()
    if respuesta == "si":
        autorizados.add(nombre)
        print(autorizados)
    else:
        print("hasta luego")


