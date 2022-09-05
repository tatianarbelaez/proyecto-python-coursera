# -*- coding: utf-8 -*-
import calculadora_indices_mejorado as calc2

peso = float(input('Inserte su peso en kilogramos: '))
altura = float(input('Inserte su altura en metros: '))
edad = int(input('Inserte su edad en años: '))
genero = input('Inserte su genero (hombre - mujer): ')
actividad= int(input('Inserte: \n1. Si hace poco o ningun ejercicio\n2. Si hace ejercicio ligero (1, 2, maximo 3 dias a la semana)\n3. Si hace ejercicio moderado (de 3 a 5 dias a la semana)\n4. Si es deportista (entrena de 6 a 7 dias a la semana)\n5. Si es atleta (entrena dos veces al dia)\n'))


CALCULAR_IMC = calc2.calcular_IMC(peso, altura)
CATEGORIA = calc2.categorizacion_segun_IMC(CALCULAR_IMC)
print('Su Indice de masa corporal es: ' + str(round(CALCULAR_IMC,2)))
print('Segun su IMC se encuentra en: ' + CATEGORIA + '\n')

CALCULAR_PORCENTAJE_GRASA = calc2.calcular_porcentaje_grasa(peso, altura, edad, genero)
CALCULAR_PORCENTAJE_GRASA_RECOMENDADO = calc2.rango_normal_grasa_corporal(CALCULAR_PORCENTAJE_GRASA, edad, genero)
print('Su porcentaje de grasa corporal es: ' + str(round(CALCULAR_PORCENTAJE_GRASA, 2)) + ' %')
print('El rango de grasa corporal recomendado es de ' + CALCULAR_PORCENTAJE_GRASA_RECOMENDADO)

CALCULAR_TMB = calc2.calcular_calorias_en_reposo(peso, altura, edad, genero)
print('Su tasa metabolica basal o gasto de calorias en reposo es: ' + str(round(CALCULAR_TMB, 2)) + ' cal\n')

CALCULAR_CALORIAS_CON_ACTIVIDAD = calc2.calcular_calorias_en_actividad(peso, altura, edad, genero, actividad)
print('Las calorias que gasta segun la actividad fisica que realiza es alrededor de: ' + str(round(CALCULAR_CALORIAS_CON_ACTIVIDAD, 2)) + ' cal\n')

CALCULO_CALORIAS_PARA_ADELGAZAR = calc2.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, genero)
print('Entonces, si desea bajar de peso ' + CALCULO_CALORIAS_PARA_ADELGAZAR)

