# -*- coding: utf-8 -*-
import calculadora_indices as calc

peso = float(input('Inserte su peso en kilogramos: '))
altura = float(input('Inserte su altura en  centimetros: '))
edad = int(input('Inserte su edad en años: '))
valor_genero = float(input('Inserte 5 si es hombre y -161 si es mujer: '))
valor_actividad = float(input('Inserte:' 
                        '1.2 si hace poco o nada de ejercicio'
                        '1.375 si hace ejercicio de 1 a 2 veces a la semana'
                        '1.55 si hace ejercicio de 3 a 5 dias a la semana'
                        '1.725 si hace ejercicio de 6 a 7 dias a la semana'
                        '1.9 si entrena todos los dias por la mañana y por la tarde'
                        ': '))

CALCULAR_CALORIAS_CON_ACTIVIDAD = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
print(str(round(CALCULAR_CALORIAS_CON_ACTIVIDAD, 2)) + ' cal')

#Listo