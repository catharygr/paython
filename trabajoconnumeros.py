from decimal import Decimal
from functools import reduce
import math


"""
Orden de calculos
Parentisis => ()
Exponentes => **
Multiplicar => *
División => /
Suma => +
Resta => -
"""

# total = 100

# # total = total + 10
# total += 10

# print(total)

# Decimal y float



# precio = Decimal(88.40)
# comision = Decimal(0.08)
# unidades = 44

# precio += (precio * comision)
# precio *= unidades

# print(precio)

# Convertir entre integrales, Float, Decimal  y numeros complejos


# precio = 88.40
# comision = 0.08
# unidades = 44

# print(int(precio))
# print(float(unidades))
# print(Decimal(precio))
# print(complex(comision))

##### Funciones mas populares

perdida = -20.25
precio_producto = 89.49

# print(abs(perdida)) # Quita lo negativo
# print(math.floor(precio_producto)) # Lo deja en muero entero hacia abajo
# print(math.ceil(precio_producto)) # Lo deja en muero entero hacia abajo
# print(math.ceil(abs(perdida))) 
# print(round(precio_producto)) 
# print(math.sqrt(precio_producto))
# print(math.pow(5, 3)) # Potencial

#### Funcion (Ejercicio de retornar la exponecial de un numero)

# def power_function(num, exp):
  ##  Version Manual 
    # contador = exp - 1
    # resultado_final = num

    # while contador > 0:
    #     resultado_final *=  num 
    #     contador -= 1

    # return resultado_final

#### Version Reducer
  # computed_list = [num] * exp # [10, 10, 10] - En el caso de que num es 10 y exp es 2
  # return (reduce(lambda resultado_final, element: resultado_final * element, computed_list))


# print(power_function(2, 3))


