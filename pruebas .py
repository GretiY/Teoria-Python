#Ejercicio 18: 
print("Introduzca una contraseña segura que : ")
print("Minimo 8 chars\nAl menos una mayuscula\nAl menos un numero\Al menos un simbolo ( ! , @ , #, $, %)")

contraseña = input()
longitud_ok = len(contraseña) >=8
tiene_mayuscula = False
tiene_numero = False
tiene_simbolo = False
simbolos = ["!", "@","$","%"]

for caracter in contraseña:
    if caracter.isupper():
        tiene_mayuscula = True
       
    if caracter.isdigit():
        tiene_numero = True
        
    
    if caracter in simbolos:
        tiene_simbolo = True
        

print(f"Longitud ok : {longitud_ok}")
print(f"Tiene mayuscula : {tiene_mayuscula}")
print(f"Tiene numero : {tiene_numero}")
print(f"Tiene simbolo : {tiene_simbolo}")


es_valida = longitud_ok and tiene_mayuscula and tiene_numero and tiene_simbolo

if es_valida:
    print(f"la contraseña {contraseña} es valida")
else:
    print(f"contraseña no valida")