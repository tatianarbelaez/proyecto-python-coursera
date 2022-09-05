# -*- coding: utf-8 -*-
import calculadora_indices as calc

peso = float(input('Inserte su peso en kilogramos: '))
altura = float(input('Inserte su altura en  centimetros: '))
edad = int(input('Inserte su edad en años: '))
valor_genero = float(input('Inserte 5 si es hombre y -161 si es mujer: '))

CALCULO_CALORIAS_PARA_ADELGAZAR = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
print(CALCULO_CALORIAS_PARA_ADELGAZAR)

#Listo

