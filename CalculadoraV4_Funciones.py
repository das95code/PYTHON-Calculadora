# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:01:32 2021

@author: DavidAlcázarSánchez
"""
#DESCRIPCION DEL PROGRAMA
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

#______________________________________________________________________________________________________________________________

#FUNCIONES


def pedirNumeros():
    Num1 = float(input("Elige el primer número: "))
    Num2 = float(input("Elige el segundo número: "))
    return Num1, Num2

def sumaAB(Num1, Num2):
    print("\nHas elegido la opción suma de dos números.")
    print(f"El resultado de la suma de {Num1} y {Num2} es {Num1 + Num2}")

def restaAB(Num1, Num2):
    print("\nHas elegido la opción resta de dos números.")
    print(f"El resultado de la resta de {Num1} y {Num2} es {Num1 - Num2}")
    
def multiplicacionAB(Num1, Num2):
    print("\nHas elegido la opción multiplicación de dos números.")
    print(f"El resultado de la multiplicación de {Num1} por {Num2} es {Num1 * Num2}")
    
def divisionAB(Num1, Num2):
    print("\nHas elegido la opción división de dos números.")
    while Num2 == 0:
        print ("\n¡El divisor no puede ser 0!")
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
    print(f"El resultado de la división de {Num1} entre {Num2} es {Num1 / Num2}")
    
def moduloAB(Num1, Num2):
    print("\nHas elegido la opción módulo entre dos números.")
    while Num2 == 0:
        print ("\n¡El segundo número no puede ser 0!")
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
    print(f"El resultado de calcular el módulo de {Num1} entre {Num2} es {Num1 % Num2}")
    
def cocienteAB(Num1, Num2):
    print("Has elegido la opción cociente entre dos números.")
    while Num2 == 0:
        print ("\n¡El segundo número no puede ser 0!")
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
    print(f"El resultado de calcular el cociente de {Num1} entre {Num2} es {Num1 // Num2}")
    
def exponenteAB(Num1, Num2):
    print("\nHas elegido la opción exponente de un número elevado a otro.")
    print(f"El resultado del expontente de {Num1} elevado a {Num2} es {Num1**Num2}")
    
def paresCuadrados():
    print("\nHas elegido la opción calculadora de áreas de cuadrados para 'n' números pares.")
    y = 1
    x = int(input("Introduce la cantidad de números pares que que quieres que aparezcan en la operación: "))
    for i in range (1, (x*2+1)):
        if y <= x and i % 2 == 0:
            print(f"El área del cuadrado numero {y} para lado con valor", i, "es de", i**2, "metros cuadrados.")
            y= y+1

def paresCirculos():
    print("\nHas elegido la opción calculadora de áreas de círculos para 'n' números pares.")
    y = 1
    x = int(input("Introduce la cantidad de números pares que que quieres que aparezcan en la operación: "))
    for i in range (1, (x*2+1)):
        if y <= x and i % 2 == 0:
            print(f"El área del círculo numero {y} para radio valor", i, "es de", 3.14 * (i**2), "metros cuadrados.")
            y= y+1
    
#______________________________________________________________________________________________________________________________

#CODIGO


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
    \nIntroduce el número para la operación que quieras realizar: "))

       
    if Calculadora == 1:
        Num1, Num2 = pedirNumeros()
        sumaAB(Num1, Num2)
       
    elif Calculadora == 2:
        Num1, Num2 = pedirNumeros()
        restaAB(Num1, Num2)
        
    elif Calculadora == 3:
        Num1, Num2 = pedirNumeros()
        multiplicacionAB(Num1, Num2)
        
    elif Calculadora == 4:
        Num1, Num2 = pedirNumeros()
        divisionAB(Num1, Num2)
        
    elif Calculadora == 5:
        Num1, Num2 = pedirNumeros()
        moduloAB(Num1, Num2)
        
    elif Calculadora == 6:
        Num1, Num2 = pedirNumeros()
        cocienteAB(Num1, Num2)
        
    elif Calculadora == 7:
        Num1, Num2 = pedirNumeros()
        exponenteAB(Num1, Num2)
        
    elif Calculadora == 8:
        paresCuadrados()
        
    elif Calculadora == 9:
        paresCirculos()
    
    elif Calculadora < 0 or Calculadora >10: 
       print("\n \nIntroduce un comando entre el 1 y el 10, por favor.")
        
else:
    print ("\nHas seleccionado la opción salir. ¡Hasta luego!")