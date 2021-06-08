#Ugalde Carreño Paulina 19141209

#importamos la libreria math para poder hacer uso de la funcion raiz cuadrada
from math import sqrt 
from ReglasIntegracion import *

def longitudArco():
    derivada = deriva(coeficientes)
    print(derivada)

    if opc == 1:
        reglaSimpson(a,b,n,tolerancia,v_anterior,derivada,grado)
    elif opc == 2:
        reglaTrapecio(a,b,n,tolerancia,v_anterior,derivada,grado)

# ------------------------------------------------------------------------------------------------------
#Pedimos el grado del polinomio y este debe ser mayor a 1
grado = 0
while grado<=0:
    grado = int(input("Grado del polinomio (>1): "))

#Array donde se guardaran los coeficientes de nuestro polinomio
coeficientes = []

# Ingresamos los coeficientes del polinomio comenzando con el termino de mayor grado y terminando 
print("Ingresa los coeficientes comenzando por el termino de mayor grado y terminando con el termino independiente ")
for i in range(grado+1):
    coeficiente = float(input("Ingresa el coeficiente: "))
    coeficientes.append(coeficiente)
coeficientes.reverse()

a = b = 0
# a y b no pueden ser iguales ni tampoco el limite inferior debe ser mayor al superior
while a == b or a > b:
    a = float(input("\nLimite inferior: "))
    b = float(input("Limite superior: "))
n = 6

#Pedimos las cifras significativas
csig = int(input("Cifras significativas: "))
tolerancia = 0.5*(10**(2-csig))
v_anterior = 0

print("\n1.- Metodo Simpson\n2.- Metodo Trapecios")
opc = int(input("Ingresa el metodo de solucion: "))

print("\nLa tolerancia es "+str(tolerancia)+" para obtener "+str(csig)+" cifras significativas.\n")
longitudArco()