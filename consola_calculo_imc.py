# -*- coding: utf-8 -*-
import calculadora_indices as calc

peso = float(input('Por favor inserte su peso en kilogramos: '))
altura = float(input('Por favor inserte su altura en metros: '))

CALCULAR_IMC = calc.calcular_IMC(peso, altura)
print(round(CALCULAR_IMC,2))

#listo