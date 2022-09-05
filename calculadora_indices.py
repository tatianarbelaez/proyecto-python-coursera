# -*- coding: utf-8 -*-
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
def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float)->float:
    """
    Calcula el porcentaje de grasa de una persona
    Parametros:
        peso en kg
        altura en metros
        edad en años
        valor genero es un valor que varía según el género de la persona
        en caso de ser masculino debe ser 10.8 y en caso de ser femenino debe ser 0
    """
    IMC = calcular_IMC(peso, altura)
    grasa_corporal = 1.2 * IMC + 0.23*edad-5.4-valor_genero
    return grasa_corporal

#--------------------------------------------------------------------------------
"""
logica calculo calorias que se gastan en reposo
"""
def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int)->float:
    """
    Calcula la cantidad de calorías que una persona quema estando en reposo
    (esto es, su tasa metabólica basal)
     Parametros:
        peso en kg
        altura en centimetros
        edad en años
        valor genero es un valor que varía según el género de la persona
    """
    TMB = 10*peso + 6.25*altura - 5*edad + valor_genero
    return TMB

#--------------------------------------------------------------------------------
"""
logica calculo calorias que se gastan con actividad fisica
"""

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float)->float:
    """
    Calcula la cantidad de calorías que una persona quema al realizar algún tipo 
    de actividad física (esto es, su tasa metabólica basal según actividad física)
    Parametros:
        peso en kg
        altura en centimetros
        edad en años
        valor genero es un valor que varía según el género de la persona
    """
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    TMB_ACTIVIDAD = TMB * valor_actividad
    return TMB_ACTIVIDAD
#--------------------------------------------------------------------------------
"""
logica calculo consumo de calorias recomendado para adelgazar
"""  
def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: float)->str:
    """
    Calcula el rango de calorías recomendado, que debe consumir una persona 
    diariamente en caso de que desee adelgazar
    Parametros:
        peso en kg
        altura en metros
        edad en años
        valor genero es un valor que varía según el género de la persona
    """ 
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    minimo_calorias,maximo_calorias=(0.8*TMB,0.85*TMB)  
    mensaje = 'Para adelgazar es recomendado que consumas entre: '+ str(round(minimo_calorias, 2)) + ' y ' + str(round(maximo_calorias, 2)) + ' calorías al día.' 
    return mensaje