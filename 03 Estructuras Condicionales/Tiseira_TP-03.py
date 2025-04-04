print("Ejercicio 1")
print(f'1) Escribir un programa que solicite la edad del usuario. \nSi el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.')
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

print("Fin Ejercicio 1\n")


print("Ejercicio 2")
print(f'2) Escribir un programa que solicite su nota al usuario. \nSi la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.')
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("Fin Ejercicio 2\n")



print("Ejercicio 3")
print(f'3) Escribir un programa que permita ingresar solo números pares. \nSi el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".')
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print("Fin Ejercicio 3\n")




print("Ejercicio 4")
print(f'4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: \n●​ Niño/a: menor de 12 años. \n●​ Adolescente: mayor o igual que 12 años y menor que 18 años. \n●​ Adulto/a joven: mayor o igual que 18 años y menor que 30 años. \n●​ Adulto/a: mayor o igual que 30 años.')
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

print("Fin Ejercicio 4\n")



print("Ejercicio 5")
print(f'5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). \nSi el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".')
contrasena = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print("Fin Ejercicio 5\n")




print("Ejercicio 6")
print(f'escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.\n Imprimir el resultado por pantalla.')

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("Lista de números aleatorios: ", numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print("Moda: ", moda)
print("Mediana: ", mediana)
print("Media: ", media)
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")
else:
    print("No se puede determinar un sesgo claro")

print("Fin Ejercicio 6\n")

print("Ejercicio 7")
print(f'7) Escribir un programa que solicite una frase o palabra al usuario.\n Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.')
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)
print("Fin Ejercicio 7\n")
 
print("Ejercicio 8")
print(f"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
      1.​ Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
      2.​ Si quiere su nombre en minúsculas. Por ejemplo: pedro.
      3.​ Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
      El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
      Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.""")
nombre = input("Ingrese su nombre: ")
print("Seleccione una opción:")
print("1. Mayúsculas")
print("2. Minúsculas")
print("3. Primera letra mayúscula")
opcion = int(input("Ingrese una opción (1, 2 o 3): "))
if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
elif opcion == 3:
    nombre = nombre.title()
else:
    print("Opción no válida")
print(nombre)
print("Fin Ejercicio 8\n")

print("Ejercicio 9")
print(f"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
●​ Menor que 3: "Muy leve" (imperceptible).
●​ Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
●​ Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
●​ Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
●​ Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
●​ Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).""")

magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

print("Fin Ejercicio 9\n")

print("Ejercicio 10")
print(f"""10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
┌───────────────────────────────────────────┬─────────────────────────────┬─────────────────────────────┐
│ Periodo del año                           │ Hemisferio norte            │       Hemisferio sur        │
├───────────────────────────────────────────┼─────────────────────────────┼─────────────────────────────┤
│ Desde el 21 de diciembre hasta el 20 de   │ Invierno                    │ Verano                      │
│ marzo (incluidos)                         │                             │                             │
├───────────────────────────────────────────┼─────────────────────────────┼─────────────────────────────┤
│ Desde el 21 de marzo hasta el 20 de junio │ Primavera                   │ Otoño                       │
│ (incluidos)                               │                             │                             │
├───────────────────────────────────────────┼─────────────────────────────┼─────────────────────────────┤
│ Desde el 21 de junio hasta el 20 de       │ Verano                      │ Invierno                    │
│ septiembre (incluidos)                    │                             │                             │
├───────────────────────────────────────────┼─────────────────────────────┼─────────────────────────────┤
│ Desde el 21 de septiembre hasta el 20 de  │ Otoño                       │ Primavera                   │
│ diciembre (incluidos)                     │                             │                             │
└───────────────────────────────────────────┴─────────────────────────────┴─────────────────────────────┘

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.""")
mes = input("Ingrese el mes (1-12): ")
dia = int(input("Ingrese el día (1-31): "))
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
if hemisferio == "N":
    if (mes == "12" and dia >= 21) or (mes == "1") or (mes == "2") or (mes == "3" and dia <= 20):
        print("Invierno")
    elif (mes == "3" and dia >= 21) or (mes == "4") or (mes == "5") or (mes == "6" and dia <= 20):
        print("Primavera")
    elif (mes == "6" and dia >= 21) or (mes == "7") or (mes == "8") or (mes == "9" and dia <= 20):
        print("Verano")
    elif (mes == "9" and dia >= 21) or (mes == "10") or (mes == "11") or (mes == "12" and dia <= 20):
        print("Otoño")
    else:
        print("Fecha no válida")
elif hemisferio == "S":
    if (mes == "12" and dia >= 21) or (mes == "1") or (mes == "2") or (mes == "3" and dia <= 20):
        print("Verano")
    elif (mes == "3" and dia >= 21) or (mes == "4") or (mes == "5") or (mes == "6" and dia <= 20):
        print("Otoño")
    elif (mes == "6" and dia >= 21) or (mes == "7") or (mes == "8") or (mes == "9" and dia <= 20):
        print("Invierno")
    elif (mes == "9" and dia >= 21) or (mes == "10") or (mes == "11") or (mes == "12" and dia <= 20):
        print("Primavera")
    else:
        print("Fecha no válida")
else:
    print("Hemisferio no válido")
print("Fin Ejercicio 10\n")      