# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:44:44 2020

@author: Usuario
"""
"""
Importamos las librerías

pandas: manejo de estructuras de datos
sympy: manejo de álgebra simbólica
"""
import pandas as pd
import sympy as sp
"""
La ecuación de aproximación de Lagrange se define de la siguiente manera:

Dadas las abcisas:
X=[x0,x1,...,xn]
Y las ordenadas:
Y=[y0,y1,...,yn]

Se tiene la función:
p(x)=y0*L0(x)+y1*L1(x)+...+yn*Ln(x)

Donde cada Li(x):
    
Li(x)=((x-x0)*(x-x1)*...*(x-xi-1)*(x-xi+1)*...*(x-xn))/((xi-x0)*(xi-x1)*...*(xi-xi-1)*(xi-xi+1)*...*(xi-xn)
"""

"""
la función funcL genera una función de Lagrange Li(x) para un índice i específico

Entradas:
x: array de valores de x (abcisas)
y: array de valores de y (ordenadas)
i: índice a evaluar

Salida:
Retorna una función sympy Li(x) multiplicada por su respectivo yi (yi*Li(x))
"""

def funcL(x,y,i):
    xSim=sp.symbols("x") #Definimos x como símbolo algebráico con la librería sympy
    xi=x[i] #Extraemos el xi de la lista de x
    yi=y[i] #Extraemos el yi de la lista de y
    funcion=1 #Inicializamos la variable de la función
    for indice in range(len(x)): #Recorremos los índices de la lista de x
        if indice!=i: #Comprobamos que el índice no coincida con el i ingresado
            funcion*=(xSim-x[indice])/(xi-x[indice]) #Multimplicamos la variable función por una estructura sympy de la forma (x-xj)/(xi-xj)
    return (yi*funcion) #Multiplicamos por el yi y retornamos la función yi*Li(x)

"""
La función Lagrange genera una ecuación de aproximación de Lagrange en base a
una lista de puntos ingresados

Entrada:
puntos: DataFrame de pandas que contiene en dos columnas las x (abcisas) y las y (ordenadas)

Salida:
Retorna una función sympy de la forma p(x)=y0*L0(x)+y1*L1(x)+...+yn*Ln(x)
"""
def Lagrange(puntos):
    funcion = 0 #Inicializamos la variable de la función
    for i in range(0,len(puntos)): #Recorremos cada uno de los pares ordenados
        funcion+=funcL(puntos["x"], puntos["y"], i) #Aplicamos funcL() para obtener cada uno de los yi*Li(x) por cada par ordenado y lo adicionamos
    return funcion #Retornamos la función p(x)

"""
La función aproxRaizLagrange() realiza aproximaciones de la función raiz cuadrada
y=x^(1/2) para un número determinado, empezando desde un orden de polinomio n
tomando como abcisas:
x=[0,1,4,9,...,n^2]
y como ordenadas:
y=[0,1,2,3,...,n]
evaluando y aumentando el orden del polinomio hasta que la diferencia entre el
valor real y el aproximado sea menor a un error dado

Entradas:
numero: número al cuál se le quiere evaluar la raiz
orden: determina el orden incial con el cual se empezará a evaluar el polinomio
de Lagrange
error: diferencia mínima entre el valor real y el valor aproximado de la raíz,
definido por defecto como 0.01

Salida:
Ninguna

Nota: la función va imprimiendo muestras de avance y los resultados a medida
que se desarrolla
"""
def aproxRaizLagrange(numero, orden, error=0.01):
    n=orden+1 #n es el número de puntos con el que se va a construir la función de Lgrange
    print("Evaluando polinomio de orden", orden,"...") #Mensaje de aviso
    xSim=sp.symbols("x") #Definimos x como símbolo algebráico con la librería sympy
    puntos=pd.DataFrame({
            "x":[i**2 for i in range(0,n)],
            "y":[i for i in range(0,n)]
            }) #Construímos un DataFrame con pandas dónde se definen x (abcisas) y y (ordenadas)
    funcion=Lagrange(puntos) #Usamos la función Lagrange para los puntos del DataFrame
    resultado=((funcion.subs(xSim,numero*64))/8).evalf() #Evaluamos la función en el número*64, y el resultado lo dividimos por 8 (raiz cuadrada de 64)
    original=numero**(1/2) #Generamos el número original para comparar
    diferencia=abs(resultado-original) #comparamos el resultado aproximado vs. el resultado real
    if diferencia<error: # Si la diferencia es menor al error, mostramos los resultados obtenidos
        print("Resultados")
        print("Raiz cuadrada de",numero,"aproximada:",resultado)
        print("Raiz cuadrada de",numero,"real:",original)
        print("Error:",diferencia)
        print("Orden del polinomio:",orden,"\n")
    else: #Sino, repetimos el proceso aumentando el orden del polinomio en 1 y mostramos el valor del error actual
        print("Error con orden",str(orden)+":",diferencia,"\n")
        aproxRaizLagrange(numero, orden+1, error)


#Probamos el método para 2
aproxRaizLagrange(2, 66)
#Probamos el método para 3
aproxRaizLagrange(3, 69)
