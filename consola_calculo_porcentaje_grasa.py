# -*- coding: utf-8 -*-
import calculadora_indices as calc

peso = float(input('Inserte su peso en kilogramos: '))
altura = float(input('Inserte su altura en metros: '))
edad = int(input('Inserte su edad en años: '))
valor_genero = float(input('Inserte 10.8 si es hombre y 0 si es mujer: '))

CALCULAR_PORCENTAJE_GRASA = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print(str(round(CALCULAR_PORCENTAJE_GRASA, 2)) + ' %')

#Listo