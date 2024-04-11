import random
import numpy as np
import matplotlib.pyplot as plt
import math

#Funcion para generar un numero aleatorio entre 0 y 1
def generador_nro_rnd():
    nro_rnd = round(random.random(),4)
    return nro_rnd

#Funcion para generar x cantidad de numeros aleatoreos entre a y b utilizando el generador de numeros rnd
def generador_uniforme_a_b(cantidad, a, b):
    c = b - a
    listado = [round(a + generador_nro_rnd() * c,4) for _ in range(cantidad)]
    return listado

# Función para generar números aleatorios utilizando la distribución exponencial
def generador_exponencial(cantidad, lambd):
    numeros_generados = []
    for _ in range(cantidad):
        # Generar un número aleatorio entre 0 y 1
        rnd = random.random()
        # Aplicar la inversa de la función de distribución acumulativa exponencial
        numero_generado = -math.log(1 - rnd) / lambd
        numeros_generados.append(numero_generado)
    return numeros_generados

def generador_normal(cantidad, media, desviacion):
    numeros_generados = []
    for _ in range(cantidad):
        u1 = random.random()
        u2 = random.random()
        z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
        numero_generado = z1 * desviacion + media
        numeros_generados.append(numero_generado)
    return numeros_generados



def generador_histograma_uniforme(k, datos):
    # Crear el histograma
    n, bins, _ = plt.hist(datos, bins=k, color='blue', edgecolor='black')

    # Calcular el ancho de cada intervalo
    bin_width = bins[1] - bins[0]

    # Calcular los límites inferiores y superiores de cada intervalo
    lower_limits = bins[:-1]
    upper_limits = bins[1:]

    # Agregar etiquetas y título
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.suptitle('Histograma de Distribución Uniforme')
    # Agregar la amplitud justo debajo del título
    plt.title(f"Amplitud: {round(bin_width,4)}")
    

    # Establecer las marcas y etiquetas del eje x con los límites inferiores y superiores
    plt.xticks(np.arange(lower_limits.min(), upper_limits.max() + bin_width, bin_width), rotation=45)
    
    # Mostrar el histograma
    plt.show()
    






