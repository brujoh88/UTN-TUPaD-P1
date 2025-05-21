print("Trabajo Práctico 6")
print("Nombre: Tiseira, Gustavo")
print("Eliga que ejercicio desea ejecutar")
print("1) Ejercicio 1")
print("2) Ejercicio 2")
print("3) Ejercicio 3")
print("4) Ejercicio 4")
print("5) Ejercicio 5")
print("6) Ejercicio 6")
print("7) Ejercicio 7")
print("8) Ejercicio 8")
print("9) Ejercicio 9")
print("10) Ejercicio 10")
print("11) Todos")
print("12) Salir")

opcion = int(input("Ingrese su opción: "))
if opcion == 1 or opcion == 11:
    ## Ejercicio 1
    print("Ejercicio 1")
    print(f"""Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
    range.""")
    lista = []
    for i in range(4, 101, 4):
        lista.append(i)
    print(f"Los números múltiplos de 4 son: {lista}")
            
    print("Fin Ejercicio 1\n")

if opcion == 2 or opcion == 11:
    ## Ejercicio 2
    print("Ejercicio 2")
    print(f"""Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
    penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
    indexing con números negativos!""")
    lista = ["Texto", True, ["Sublista", False], "Objetivo", 5]
    print(f"El penúltimo elemento de la lista es: {lista[-2]}")
    print(f"El penúltimo elemento de la lista es: {lista[len(lista) - 2]}")            
    print("Fin Ejercicio 2\n")

if opcion == 3 or opcion == 11:
    ## Ejercicio 3
    print("Ejercicio 3")
    print(f"""Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
    pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
    ejemplo:
    lista_vacia = []""")
    
    lista_vacia = []
    lista_vacia.append("Hola")
    lista_vacia.append("Mundo")
    lista_vacia.append("Python")
    print(f"La lista es: {lista_vacia}")

    print("Fin Ejercicio 3\n")

if opcion == 4 or opcion == 11:
    ## Ejercicio 4
    print("Ejercicio 4")
    print(f"""Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
    respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
    en los videos o bien investigar cómo funciona el indexing con números negativos!
    animales = ["perro", "gato", "conejo", "pez"]""")

    animales = ["perro", "gato", "conejo", "pez"]
    print(f"La lista original es: {animales}") 
    animales[1] = "loro"
    animales[-1] = "oso"
    print(f"La lista modificada es: {animales}")
    
    print("Fin Ejercicio 4\n")

if opcion == 5 or opcion == 11:
    ## Ejercicio 5
    print("Ejercicio 5")
    print(f"""Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.\n          
          numeros = [8, 15, 3, 22, 7]
          numeros.remove(max(numeros))
          print(numeros)\n""")
    
    print(f"""El programa crea una lista llamada "numeros" con cinco elementos.
    Luego, utiliza la función max() para encontrar el valor máximo de la lista y lo elimina con el método remove().
    Finalmente, imprime la lista resultante sin el número máximo.\n""")
    
    print("Fin Ejercicio 5\n")

if opcion == 6 or opcion == 11:
    ## Ejercicio 6
    print("Ejercicio 6")
    print(f"""Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
    pantalla los dos primeros.""")   

    lista = []
    for i in range(10, 31, 5):
        lista.append(i)
    print(f"Los dos primeros números de la lista son: {lista[0:2]}")
    print(f"Los dos primeros números de la lista son: {lista[:2]}") 
    
    print("Fin Ejercicio 6\n")

if opcion == 7 or opcion == 11:
    ## Ejercicio 7
    print("Ejercicio 7")
    print(f"""Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
    cualesquiera.
    autos = ["sedan", "polo", "suran", "gol"]""")   

    autos = ["sedan", "polo", "suran", "gol"]
    print(f"La lista original es: {autos}")
    autos[1] = "nuevo valor 1"
    autos[2] = "nuevo valor 2"
    print(f"La lista modificada es: {autos}")
        
    print("Fin Ejercicio 7\n")

if opcion == 8 or opcion == 11:
    ## Ejercicio 8
    print("Ejercicio 8")
    print(f"""Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
    directamente. Imprimir la lista resultante por pantalla.""")

    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    print(f"La lista es: {dobles}")    

    print("Fin Ejercicio 8\n")

if opcion == 9 or opcion == 11:
    ## Ejercicio 9
    print("Ejercicio 9")
    print(f"""Dada la lista “compras”, cuyos elementos representan los productos comprados por
    diferentes clientes:
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
    ["agua"]]
          
    a) Agregar "jugo" a la lista del tercer cliente usando append.
    b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    c) Eliminar "pan" de la lista del primer cliente.
    d) Imprimir la lista resultante por pantalla""")

    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    print(f"La lista original es: {compras}")
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    print(f"La lista modificada es: {compras}")
        
    print("Fin Ejercicio 9\n")

if opcion == 10 or opcion == 11:
    ## Ejercicio 10
    print("Ejercicio 10")
    print(f"""Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
    ● Posición lista_anidada[0]: 15
    ● Posición lista_anidada[1]: True
    ● Posición lista_anidada[2][0]: 25.5
    ● Posición lista_anidada[2][1]: 57.9
    ● Posición lista_anidada[2][2]: 30.6
    ● Posición lista_anidada[3]: False
    Imprimir la lista resultante por pantalla.""")

    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print(f"La lista anidada es: {lista_anidada}")

    print("Fin Ejercicio 10\n")