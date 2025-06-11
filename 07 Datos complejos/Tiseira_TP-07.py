print("Trabajo Práctico - Estructuras de datos complejos")
print("Nombre: Tiseira, Gustavo")
print("Ejercicio 1")
print("""1) Dado el diccionario precios_frutas
      precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
      
      Añadir las siguientes frutas con sus respectivos precios:          
      ● Naranja = 1200
      ● Manzana = 1500
      ● Pera = 2300\n""")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
print(f"Dicionario original: {precios_frutas}")
print(f"Agregando precio...")
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(f"Dicionario final: {precios_frutas}")
print("Fin Ejercicio 1\n")
input("Precione Enter para continuar...")


print("Ejercicio 2")
print("""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
       desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
      ● Banana = 1330
      ● Manzana = 1700
      ● Melón = 2800\n""")
print(f"Dicionario original - punto 2: {precios_frutas}")
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(f"Dicionario actualizado - punto 2: {precios_frutas}")
print("Fin Ejercicio 2\n")
input("Precione Enter para continuar...")

print("Ejercicio 3")
print("""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
      desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
      precios.\n""")

lista_claves = list(precios_frutas.keys())
print(lista_claves)
print("Fin Ejercicio 3\n")
input("Precione Enter para continuar...")

print("Ejercicio 4")
print("""4) Escribí un programa que permita almacenar y consultar números telefónicos.
      • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
      • Luego, pedí un nombre y mostrale el número asociado, si existe.
      Ejemplo:
      contactos={"juan":123456, "ana":987654}\n""")
contactos = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    numero = input(f"Ingrese el número de teléfono de {nombre}: ")
    contactos[nombre] = numero
print(f"Contactos ingresados: {contactos}")
nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in contactos:
    print(f"El número de teléfono de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"No se encontró el contacto {nombre_consulta}.")
    
print("Fin Ejercicio 4\n")
input("Precione Enter para continuar...")

print("Ejercicio 5")
print("""5) Solicita al usuario una frase e imprime:
      • Las palabras únicas (usando un set).
      • Un diccionario con la cantidad de veces que aparece cada palabra.
      Ejemplo:
      #Entrada -> "Hola mundo Hola"
      Palbras_unicas = {'Hola','mundo'}
      recuento = {'hola':2 ,'mundo':1}\n""")
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento de palabras: {recuento}")
print("Fin Ejercicio 5\n")
input("Precione Enter para continuar...")

print("Ejercicio 6")
print("""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.      
      Luego, mostrá el promedio de cada alumno.
      Ejemplo:
      alumnos = {
        'sofia':(10,9,8),
        'luis':(10,9,6)\n""")
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas = tuple(float(input(f"Ingrese la nota {j + 1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas
print("Notas ingresadas:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {notas} - Promedio: {promedio:.2f}")
print("Fin Ejercicio 6\n")
input("Precione Enter para continuar...")

print("Ejercicio 7")
print("""U7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
      y Parcial 2:
      • Mostrá los que aprobaron ambos parciales.
      • Mostrá los que aprobaron solo uno de los dos.
      • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).""")
parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {103, 104, 106, 107}
aprobados_ambos = parcial_1.intersection(parcial_2)
aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2)
aprobados_total = parcial_1.union(parcial_2)
print(f"Estudiantes que aprobaron ambos parciales: {aprobados_ambos}")
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {aprobados_solo_uno}")
print(f"Lista total de estudiantes que aprobaron al menos un parcial: {aprobados_total}")
print("Fin Ejercicio 7\n")
input("Precione Enter para continuar...")

## Ejercicio 8
print("Ejercicio 8")
print("""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
      Permití al usuario:
      • Consultar el stock de un producto ingresado.
      • Agregar unidades al stock si el producto ya existe.
      • Agregar un nuevo producto si no existe.\n""")
stock_productos = {
    'Manzanas': 50,
    'Peras': 30,
    'Bananas': 20,
    'Naranjas': 15
}
print("Stock de productos:", stock_productos)
producto_consulta = input("Ingrese el nombre del producto a consultar: ")
if producto_consulta in stock_productos:
    stock_anterior = stock_productos[producto_consulta]
    stock_productos[producto_consulta] += 1
    print(f"El stock de {producto_consulta} era: {stock_anterior} y ahora es: {stock_productos[producto_consulta]}")
else:
    print(f"{producto_consulta} no existe en el stock.")    
    stock_productos[producto_consulta] = 1
print("Actualización del stock:", stock_productos)
print("Fin Ejercicio 8\n")
input("Precione Enter para continuar...")

print("Ejercicio 9")
print("""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
      Ejemplo:
      agenda = {
      ("lunes","10:00") : "Reunion",
      ("Martes","11:00") : "Clases",      
      }""")
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "11:00"): "Clases",
    ("miércoles", "09:00"): "Desayuno con amigos"
}
print("Agenda actual:")
for fecha, evento in agenda.items():
    print(f"{fecha[0].capitalize()} a las {fecha[1]}: {evento}")
fecha_consulta = input("Ingrese el día de la semana (ejemplo: lunes) para consultar eventos: ").lower() 
hora_consulta = input("Ingrese la hora (ejemplo: 10:00) para consultar eventos: ")
evento_consulta = agenda.get((fecha_consulta, hora_consulta))
if evento_consulta:
    print(f"Evento programado para {fecha_consulta.capitalize()} a las {hora_consulta}: {evento_consulta}") 
else:
    print(f"No hay eventos programados para {fecha_consulta.capitalize()} a las {hora_consulta}.")
    agregar_evento = input("¿Desea agregar un evento? (s/n): ")
    if agregar_evento.lower() == 's':
        nuevo_evento = input("Ingrese el nombre del evento: ")
        agenda[(fecha_consulta, hora_consulta)] = nuevo_evento
        print(f"Evento agregado: {nuevo_evento} para {fecha_consulta.capitalize()} a las {hora_consulta}.")
    else:
        print("No se agregó ningún evento.")

    print("Agenda actualizada:")
    for fecha, evento in agenda.items():
        print(f"{fecha[0].capitalize()} a las {fecha[1]}: {evento}")
print("Fin Ejercicio 9\n")
input("Precione Enter para continuar...")

print("Ejercicio 10")
print("""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
      • Las capitales sean las claves.
      • Los países sean los valores.
      Ejemplo:
      original= {"Argentina":"Buenos Aires", "Chile":"Santiago"}
      invertido= {"Buenos Aires":"Argentina", "Santiago":"Chile"}\n""")
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais
print("Diccionario original:", original)
print("Diccionario invertido:", invertido)
print("Fin Ejercicio 10\n")
input("Precione Enter para continuar...")