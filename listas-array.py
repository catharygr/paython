import math
import random

### Listas

#Crear, agregar y cambiar
# users = ["Caty", "Sasa", "Clau"]
# users.insert(0, "Luis")
# users.append("Edu")
# print(users)
# # Para acceder
# print(users[0])
# print([users[0]])
# print({"nombre": users[2]})

# Remover 

# users = ["Caty", "Sasa", "Clau", "Zorka"]

# users.remove("Caty")
# users[1:-1]Remueve el primero y ultimo de una lista y retorna uno nuevo.
# pooper_user = users.pop() # pop quita el ultimo y si pongo .pop(0) quita el primero o cualquier indices

# # print(users, pooper_user)

# # Eliminar
# del users[0]
# print(users)


# # Consultar lista 
# etiquetas = ["python", "JS", "react", "HTML"]
# print(len(etiquetas))
# print(etiquetas[-1])
# print(etiquetas.index("JS"))

#### Ordenar listas

# etiquetas = ["senderos", "bici", "esquiar", "correr"]
# # numbers = [1,2,5,8.10,22,45]

# etiquetas.sort() # ordena albateticamente y los numeros de menos a mayor.
# print(etiquetas)
# sorted(numbers) # Ordenar por alfabeto, no modifica la lista original y retorna una nueva lista
# number.sort(reverse=True) # Ordenar al reves del albabeto
# print(numbers)

#### join()function para construir URL 

#https://www.startpage.com/do/search?q=paython+development+tutorial

# uri = "https://www.startpage.com/do/search?q="
# etiquetas = ["paython", "development", "tutorial"]
# formatear_etiquetas = "+".join(etiquetas) # Unir elementos tipo string con " "
# url_consulta = f"""{uri}{formatear_etiquetas}""" # he puesto """"""" pero si es es en una sola fila se puede usar solo una ""
# print(url_consulta)

### Rangos en listas
# etiquetas = ["paython","JS", "CSS", "HTML"]
# etiquetas_rango = etiquetas[:-1] # Retorna un array con elemento/s ejemplos: [:2][1:][3:1], si queiro eliminar uno se hace de esta manera [:-1]
# print(etiquetas_rango)

### Tecnicas mas avanzadas de rango y slice sobre una lista

# etiquetas = ["paython", "development", "tutorial","programing", "computer science", "code","pinga","coño"]

# etiquetas_rango = etiquetas[:-1:3]#Empieza en cero hasta el penultimo y ese argumneto es para sacar cada segundo o tercero....
# etiquetas_rango = etiquetas[::-1]# De esta manera se invierte el orden de los elementos, se crea una nueva lista
# print(etiquetas_rango)

#### Mediana estadistica de una lista 

# rebaja_precio = [100, 83, 220, 40, 100, 400, 10, 1, 3]

# def encontrar_mediana(arr): 
#   # Ordenar arr y guardar en una nueva variable
#   arr_ordenado = sorted(arr)
#   # Encontrar indice de mediano buscando la longitud de arr y dividiendola a la mitad y rendondeanla hacia abajo.
#   index_mediano = math.floor(len(arr) / 2)
#   # Retornar el string de valor mediano utilizando slice y indice de mediano
#   return arr_ordenado[index_mediano : index_mediano + 1][0]

# print(encontrar_mediana(rebaja_precio))

#### Usar varios class para guardar varios slice values

# etiquetas = ["paython", "development", "tutorial","programing", "computer science", "code"]
# slice_obj = slice(1, 4, 1)
# print(slice_obj.start)
# print(slice_obj.stop)
# print(slice_obj.step)

#### añadir a una lista con dos procesos: Place and Copy

# etiquetas = ["paython", "development", "tutorial", "computer science", "code"]


# #  # Si es una Lista: 
# # etiquetas.extend(["programming", "Codificador"]) # Extiende la lista parecido a la funcionalidad de push de JS pero si es otra lista, solo extiende con los valores de su propia lista.



# # # Y si es un string. Debo meterlo en corchete
# # # etiquetas.extend(["programming"])

# new_etiqueta = etiquetas = ["coñazo"] # Asi se crea una nueva lista sin modificar la original
# # print(etiquetas)

otros_pesado = {
      "ganador": 1, 
      "igual": 2,
      "perdedor": 3
    }

def loteria_pesada(pesada):
  listado_contenido = []

  for (name, peso) in pesada.items(): 
    for _ in range(peso):
      listado_contenido.append(name)

  return random.choice(listado_contenido)

print(loteria_pesada(otros_pesado))

#### Remover el primer y ultimo elemento usando destructuracion 
# mi_lista = [1, 2, 3, 4, 5]
# def rem_primer_y_ultimo(arr):
#    primero, *el_resto, ultimo = arr # *el_resto es equivalente en JS a: ...el_resto
#    return el_resto
# print(rem_primer_y_ultimo(mi_lista))