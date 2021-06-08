#importamos la libreria math para poder hacer uso de la funcion raiz cuadrada
from math import sqrt 

def reglaTrapecio(a,b,n,tolerancia,v_anterior,derivada,grado):
    suma = integral = 0
    h = (b-a)/n #delta x

    #procederemos a hacer la suma de riemmann
    for i in range(1, n): #inicia en 1 y termina en n
        suma += horner(grado,derivada,(a+(i*h)))

    #formula de la regla del trapecio
    integral = ((b-a)/(2*n))*(horner(grado, derivada, a)+ 2*suma +horner(grado, derivada, b))
    error = ((integral - v_anterior)/integral)*100;
    print("La aproximacion de la integral es: "+str(integral)+" obtenida con n = "+str(n)+". El error es: "+str(error))

    if(abs(error)>=tolerancia):
        n +=10
        v_anterior = integral
        return reglaTrapecio(a,b,n,tolerancia,v_anterior,derivada,grado)

    print("El resultado de la integral es: "+str(integral))
    print("Calculado con "+str(n)+" particiones")

def horner(grado, derivada, x):
    polinomio = 0
    for i in range(grado):
        polinomio = polinomio + (derivada[i] *pow(x,i))
    polinomio = sqrt(1+pow(polinomio,2))
	# Al término de este ciclo WHILE, la variable polinomio tiene el valor del P(x)
    return polinomio


def reglaSimpson(a,b,n,tolerancia,v_anterior,derivada,grado):
    suma1 = suma2 = integral = 0
    h = (b-a)/n #delta x

    #procederemos a hacer la suma de riemmann
    for i in range(1, n): #inicia en 1 y termina en n
        if i%2 == 0:
            suma2 += horner(grado,derivada,(a+(i*h)))
        else:
            suma1 += horner(grado,derivada,(a+(i*h)))
    
    #formula de la regla de simpson
    integral = (h/3)*(horner(grado, derivada, a)+ 4*suma1 + 2*suma2 +horner(grado, derivada, b))
    error = ((integral - v_anterior)/integral)*100;
    print("La aproximacion de la integral es: "+str(integral)+" obtenida con n = "+str(n)+". El error es: "+str(error))

    if(abs(error)>=tolerancia):
        n +=10
        v_anterior = integral
        return reglaSimpson(a,b,n,tolerancia,v_anterior,derivada,grado)

    print("El resultado de la integral es: "+str(integral))
    print("Calculado con "+str(n)+" particiones")

# Funcion de derivacion que deriva el polinomio
def deriva(coeficientes):
    derivada = []
    k = 1
    if((len(coeficientes)) == 1):
        derivada.append(0)
    else:
        while(len(coeficientes)>k): 
            derivada.append(coeficientes[k]*k)
            k=k+1
    return derivada 
