
# comentarios en PYTHON

'''
    Diferencias basicas con Java
        1) SINTAXIS
        2) NO hay punto y coma al final de cada instruccion
        3) La SANGRIA o INDENT es SUPER IMPORTANTE en PYTHON
        4) NO hay declaracion de tipos de datos en Python
            4a)  TODOS los datos en Python son OBJETOS
            4b) Python es FUERTEMENTE TIPADO y DE TIPADO DINAMICO

        5) En python casi todo son funciones

'''

"""
asdfasdfasd
"""
print("=== CALCULO DE SALARIO ======")

print("Ingresa tu nombre completo: ")
nombre = input()

año_nac = input("Ingresa tu año de nacimiento: ")
edad = 2022 - int(año_nac)

dias_trabajados = int(input("Ingresa dias trabajados: "))
pago_hora = int(input("Ingresa pago por dia: "))
pctj_impuesto = int(input("Ingresa tasa de impuesto (%): "))

salario_bruto = dias_trabajados * pago_hora

tasa = pctj_impuesto / 100
salario_neto = salario_bruto * (1-tasa)

print(type(edad))
print("-------------- RECIBO NOMINA --------------")
print("Tu nombre es: " + nombre)
print("Tu año de nacimiento es: " + año_nac)
print("Tu edad es: " + str(edad))

import math

print(f"Salario  BRUTO: ${salario_bruto:.2f}")
print(f"Salario NETO: ${salario_neto:.2f}")


