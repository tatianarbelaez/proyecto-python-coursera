# -*- coding: utf-8 -*-
import calculadora_indices as calc

peso = float(input('Inserte su peso en kilogramos: '))
altura = float(input('Inserte su altura en  centimetros: '))
edad = int(input('Inserte su edad en años: '))
valor_genero = int(input('Inserte 5 si es hombre y -161 si es mujer: '))

CALCULAR_TMB = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print(str(round(CALCULAR_TMB, 2)) + ' cal')

#Listo
