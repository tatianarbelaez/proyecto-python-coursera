# -*- coding: utf-8 -*-
"""
Todo debe poder calcularse con lo que se pide inicialmente
*peso en kilogramos
*altura en metros
*edad en años
*genero (mujer, hombre)
*actividad fisica
"""

"""
logica calculo IMC
"""
def calcular_IMC(peso: float, altura: float)->float:
    """
    Calcula el índice de masa corporal de una persona.
    Parametros:
        peso en Kg
        altura en metros
    """
    IMC = peso / (altura ** 2)
    return IMC

#--------------------------------------------------------------------------------
"""
logica calculo porcentaje de grasa
"""
def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, genero: str)->float:
    """
    Calcula el porcentaje de grasa de una persona
    Parametros:
        peso en kg
        altura en metros
        edad en años
        genero --> indica si el valor genero en el calculo es 0 o 10.8
    """
    IMC = calcular_IMC(peso, altura)
    genero_2 = genero.lower() 
    if genero_2 == 'mujer':
        valor_genero = 0
    elif genero_2 == 'hombre':
        valor_genero = 10.8
    else:
        print('Genero no permitido')
        exit()
    grasa_corporal = 1.2 * IMC + 0.23*edad-5.4-valor_genero
    return grasa_corporal

#--------------------------------------------------------------------------------
"""
logica calculo calorias que se gastan en reposo
"""
def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, genero: str)->float:
    """
    Calcula la cantidad de calorías que una persona quema estando en reposo
    (esto es, su tasa metabólica basal)
     Parametros:
        peso en kg
        altura en metros
        edad en años
        genero --> indica si el valor de genero debe ser 5 o -161
    """
    altura_2 = altura * 100
    genero_2 = genero.lower()
    if genero_2 == 'mujer':
        valor_genero = -161
    elif genero_2 == 'hombre':
        valor_genero = 5
    else:
        print('Genero no permitido')
        exit()
    TMB = 10*peso + 6.25*altura_2 - 5*edad + valor_genero
    return TMB

#--------------------------------------------------------------------------------
"""
logica calculo calorias que se gastan con actividad fisica
"""

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, genero: str, actividad: int)->float:
    """
    Calcula la cantidad de calorías que una persona quema al realizar algún tipo 
    de actividad física (esto es, su tasa metabólica basal según actividad física)
    Parametros:
        peso en kg
        altura en metros
        edad en años
        valor genero es un valor que varía según el género de la persona
    """
    altura_2 = altura * 100
    genero_2 = genero.lower()
    if genero_2 == 'mujer':
        valor_genero = -161
    elif genero_2 == 'hombre':
        valor_genero = 5
    else:
        print('Genero no permitido')
        exit()
    if actividad == 1:
        valor_actividad = 1.2
    elif actividad == 2:
        valor_actividad = 1.375
    elif actividad == 3:
        valor_actividad = 1.55
    elif actividad == 4:
        valor_actividad = 1.725
    elif actividad == 5:
        valor_actividad = 1.9
    else:
        print('actividad no permitida')
        exit()     
    TMB = 10*peso + 6.25*altura_2 - 5*edad + valor_genero
    TMB_ACTIVIDAD = TMB * valor_actividad
    return TMB_ACTIVIDAD
#--------------------------------------------------------------------------------
"""
logica calculo consumo de calorias recomendado para adelgazar
"""  
def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, genero: str)->str:
    """
    Calcula el rango de calorías recomendado, que debe consumir una persona 
    diariamente en caso de que desee adelgazar
    Parametros:
        peso en kg
        altura en metros
        edad en años
        valor genero es un valor que varía según el género de la persona
    """
    altura_2 = altura * 100
    genero_2 = genero.lower()
    if genero_2 == 'mujer':
        valor_genero = -161
    elif genero_2 == 'hombre':
        valor_genero = 5
    else:
        print('Genero no permitido')
        exit()
    TMB = 10*peso + 6.25*altura_2 - 5*edad + valor_genero
    minimo_calorias,maximo_calorias=(0.8*TMB,0.85*TMB)  
    mensaje = 'es recomendado que consumas entre: '+ str(round(minimo_calorias, 2)) + ' y ' + str(round(maximo_calorias, 2)) + ' calorías al día.' 
    return mensaje

"""
Funciones para interpretar los indices anteriores
"""  

#Interpretacion IMC
def categorizacion_segun_IMC (IMC: float)->str:
    if IMC < 16:
        categoria = 'Delgadez severa'
    elif (IMC > 16 and IMC < 16.99):
        categoria = 'Delgadez moderada'
    elif (IMC > 17 and IMC < 18.49):
        categoria = 'Delgadez aceptable'
    elif (IMC > 18.5 and IMC < 24.99):
        categoria = 'Peso normal'
    elif (IMC > 25 and IMC < 29.99):
        categoria = 'Sobrepeso'
    elif (IMC > 30 and IMC < 34.99):
        categoria = 'Obesidad tipo I'
    elif (IMC > 35 and IMC < 39.99):
        categoria = 'Obesidad tipo II'
    elif (IMC > 40 and IMC < 49.99):
        categoria = 'Obesidad tipo III o morbida'
    elif (IMC > 50):
        categoria = 'Obesidad tipo IV o extrema'
    else:
        print('IMC no permitido')
    return categoria

#Interpretacion porcentaje de grasa corporal 
import sys
def rango_normal_grasa_corporal(GC: float, edad: int, genero: str)-> str:
    genero_2 = genero.lower()
    if (edad >= 20 and edad <= 29):
        if genero_2 == 'mujer':
            rango_recomendado = '16% a 28%'
        elif genero_2 == 'hombre':
            rango_recomendado = '11% a 20%'
        else:
            print('genero no permitido')
            sys.exit()
    elif (edad >= 30 and edad <= 39):
        if genero_2 == 'mujer':
            rango_recomendado = '17% a 29%'
        elif genero_2 == 'hombre':
            rango_recomendado = '12% a 21%'
        else:
            print('genero no permitido')
            sys.exit()
    elif (edad >=  40 and edad <= 49):
        if genero_2 == 'mujer':
            rango_recomendado = '18% a 30%'
        elif genero_2 == 'hombre':
            rango_recomendado = '14% a 23%'
        else:
            print('genero no permitido')
            sys.exit()
    elif (edad >=  50 and edad <= 59):
        if genero_2 == 'mujer':
            rango_recomendado = '19% a 31 %'
        elif genero_2 == 'hombre':
            rango_recomendado = '15% a 24%'
        else:
            print('genero no permitido')
            sys.exit()
    else:
        print('edad no tiene un rango recomendado para este indice')
    return rango_recomendado









