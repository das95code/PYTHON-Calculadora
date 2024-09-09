# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:25:02 2021

@author: DavidAlcázarSánchez
"""

#Calculadora 
#Suma de 2 números
#Resta de dos números
#Multiplicación de dos números
#División de dos números
#Módulo entre dos números
#Cociente entre dos números
#Exponente de un número elevado a otro
#Calculadora de áreas de cuadrados para 'n' números pares simultáneos
#Calculadora de áreas de círculos para 'n' números pares simultáneos
#Salir
#Introduce una opción

Calculadora = 0
while Calculadora != 10:
    Calculadora = int(input("¡Hola! Soy tu calculadora. Introduzca el número asignado a la operación que quieras realizar.\n \n \
    Las opciones son:\n \
    1. Suma de dos números.\n \
    2. Resta de dos números.\n \
    3. Multiplicación de dos números.\n \
    4. División de dos números.\n \
    5. Módulo entre dos números. \n \
    6. Cociente entre dos números. \n \
    7. Exponente de un número elevado a otro número. \n \
    8. Calculadora de áreas de cuadrados para 'n' números pares. \n \
    9. Calculadora de áreas de círculos para 'n' números pares. \n \
    10. Salir. \n \
    \n Introduce el número para la operación que quieras realizar: "))
    
    if Calculadora == 1:
        Num1 = float(input("Has elegido el modo suma de dos números. Elige el primer número (puede tener dos decimales): "))
        Num2 = float(input("Elige el segundo número (puede tener también dos decimales): "))
        print(f"El resultado de la suma de {Num1} y {Num2} es {Num1 + Num2}")
        
    elif Calculadora == 2:
        Num1 = float(input("Has elegido el modo resta de dos números. Elige el primer número (puede tener dos cifras decimales): "))
        Num2 = float(input("Elige el segundo número (puede tener también dos decimales): "))
        print(f"El resultado de la resta de {Num1} y {Num2} es {Num1 - Num2}")
        
    elif Calculadora == 3:
        Num1 = float(input("Has elegido el modo multiplicación de dos números. Elige el primer número (puede tener dos cifras decimales): "))
        Num2 = float(input("Elige el segundo número (puede tener también dos decimales): "))
        print(f"El resultado de la multiplicación de {Num1} por {Num2} es {Num1 * Num2}")
        
    elif Calculadora == 4:
        Num1 = float(input("Has elegido el modo división de dos números. Elige el primer número (puede tener dos cifras decimales): "))
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
        while Num2 == 0:
            print ("¡El divisor no puede ser 0!")
            Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
        print(f"El resultado de la división de {Num1} entre {Num2} es {Num1 / Num2}")
        
    elif Calculadora == 5:
        Num1 = float(input("Has elegido el modo módulo de dos números. Elige el primer número (puede tener dos cifras decimales): "))
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
        while Num2 == 0:
            print ("¡El segundo número no puede ser 0!")
            Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
        print(f"El resultado de calcular el módulo de {Num1} entre {Num2} es {Num1 % Num2}")
        
    elif Calculadora == 6:
        Num1 = float(input("Has elegido el modo cociente de dos números. Elige el primer número (puede tener dos cifras decimales): "))
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales: "))
        while Num2 == 0:
            print ("¡El segundo número no puede ser 0!")
            Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
        print(f"El resultado de calcular el cociente de {Num1} entre {Num2} es {Num1 // Num2}")
        
    elif Calculadora == 7:
        Num1 = float(input("Has elegido el modo exponente entre dos números. Elige el primer número (puede tener dos cifras decimales): "))
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
        print(f"El resultado de elevar {Num1} a {Num2} es {Num1 ** Num2}")
        
    elif Calculadora == 8:
        y = 1
        x = int(input("Introduce la cantidad de números pares que que quieres que aparezcan en la operación: "))
        for i in range (1, (x*2+1)):
            if y <= x and i % 2 == 0:
                print(f"El área del cuadrado numero {y} para lado con valor", i, "es de", i**2, "metros cuadrados.")
                y= y+1
        
    elif Calculadora == 9:
        y = 1
        x = int(input("Introduce la cantidad de números pares que que quieres que aparezcan en la operación: "))
        for i in range (1, (x*2+1)):
            if y <= x and i % 2 == 0:
                print(f"El área del círculo numero {y} para radio valor", i, "es de", 3.14 * (i**2), "metros cuadrados.")
                y= y+1
    
    elif Calculadora < 0 or Calculadora >10: 
       print("\n \n Introduce un comando entre el 1 y el 10, por favor.")
        
else:
    print ("Has seleccionado la opción salir. ¡Hasta luego!")
    