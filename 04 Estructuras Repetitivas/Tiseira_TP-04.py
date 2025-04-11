print("Trabajo Práctico 4")
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
    print(f"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
    (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.""")
    for i in range(101):
        print(i)
    print("Fin Ejercicio 1\n")

if opcion == 2 or opcion == 11:
    ## Ejercicio 2
    print("Ejercicio 2")
    print(f"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
    dígitos que contiene.""")
    numero = int(input("Ingrese un número entero: "))
    contador = 0
    while numero > 0:
        numero //= 10
        contador += 1
    print(f"La cantidad de dígitos es: {contador}")
    print("Fin Ejercicio 2\n")

if opcion == 3 or opcion == 11:
    ## Ejercicio 3
    print("Ejercicio 3")
    print(f"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
    dados por el usuario, excluyendo esos dos valores.""")
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = 0
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    for i in range(valor1 + 1, valor2):
        suma += i
    print(f"La suma de los números enteros entre {valor1} y {valor2} es: {suma}")
    print("Fin Ejercicio 3\n")

if opcion == 4 or opcion == 11:
    ## Ejercicio 4
    print("Ejercicio 4")
    print(f"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
    secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
    un 0.""")
    cierreDePrograma = False
    suma = 0
    while not cierreDePrograma:
        numero = int(input("Ingrese un número entero (0 para salir): "))
        if numero == 0:
            cierreDePrograma = True
        else:
            suma += numero
    print(f"La suma de los números ingresados es: {suma}")
    print("Fin Ejercicio 4\n")

if opcion == 5 or opcion == 11:
    ## Ejercicio 5
    print("Ejercicio 5")
    print(f"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
    programa debe mostrar cuántos intentos fueron necesarios para acertar el número.""")
    import random
    numeroAleatorio = random.randint(0, 9)
    numeroUsuario = -1
    intentos = 0
    while numeroUsuario != numeroAleatorio:
        numeroUsuario = int(input("Adivina el número (entre 0 y 9): "))
        intentos += 1
        if numeroUsuario < numeroAleatorio:
            print("El número es mayor")
        elif numeroUsuario > numeroAleatorio:
            print("El número es menor")
        else:
            print(f"¡Felicidades! Adivinaste el número {numeroAleatorio} en {intentos} intentos.")
    print("Fin Ejercicio 5\n")

if opcion == 6 or opcion == 11:
    ## Ejercicio 6
    print("Ejercicio 6")
    print(f"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
    entre 0 y 100, en orden decreciente.""")
    for i in range(100, -1, -2):
        print(i)                        
    print("Fin Ejercicio 6\n")

if opcion == 7 or opcion == 11:
    ## Ejercicio 7
    print("Ejercicio 7")
    print(f"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
    número entero positivo indicado por el usuario.""")
    numeroPositivo = True
    while numeroPositivo:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("El número no es positivo. Intente nuevamente.")
        else:
            numeroPositivo = False    
    suma = 0
    for i in range(numero + 1):
        suma += i
    print(f"La suma de los números enteros entre 0 y {numero} es: {suma}")
    print("Fin Ejercicio 7\n")

if opcion == 8 or opcion == 11:
    ## Ejercicio 8
    print("Ejercicio 8")
    print(f"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
          programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
          negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
          menor, pero debe estar preparado para procesar 100 números con un solo cambio).""")
    contadorPares = 0
    contadorImpares = 0
    contadorNegativos = 0
    contadorPositivos = 0
    RANGO = 100
    for i in range(RANGO):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        if numero % 2 == 0:
            contadorPares += 1
        else:
            contadorImpares += 1
        if numero < 0:
            contadorNegativos += 1
        else:
            contadorPositivos += 1
    print(f"Cantidad de números pares: {contadorPares}")
    print(f"Cantidad de números impares: {contadorImpares}")
    print(f"Cantidad de números negativos: {contadorNegativos}")
    print(f"Cantidad de números positivos: {contadorPositivos}")    
    print("Fin Ejercicio 8\n")

if opcion == 9 or opcion == 11:
    ## Ejercicio 9
    print("Ejercicio 9")
    print(f"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
          media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
          poder procesar 100 números cambiando solo un valor).""")
    contador = 0
    suma = 0
    RANGO = 100
    for i in range(RANGO):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        suma += numero
        contador += 1
    media = suma / contador
    print(f"La media de los números ingresados es: {media}")    
    print("Fin Ejercicio 9\n")

if opcion == 10 or opcion == 11:
    ## Ejercicio 10
    print("Ejercicio 10")
    print(f"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
          usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.""")
    numero = input("Ingrese un número: ")
    numeroInvertido = ""
    for i in range(len(numero) - 1, -1, -1):
        numeroInvertido += numero[i]
    print(f"El número invertido es: {numeroInvertido}")    
    print("Fin Ejercicio 10\n")