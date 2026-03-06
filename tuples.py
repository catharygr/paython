#### TUPLES, es una coleccion de elementos ordenados e inmutable no se puede añadir, modificar o borrar un elemento dentro de tupla. 
mi_tuple = ("Caty",[1,2,3], {"name": "Sasha"})
# # print(mi_tuple[1][1])

# nombre, arr, obj = mi_tuple # Se puede destructurar de esta manera.
# # print(obj)


# #### Como agregar elementos a una tupla seagsinado elemntos.
# mi_tuple = mi_tuple + ("Hola",)
# mi_tuple += (" que tal?",)
# print(id(mi_tuple))
# mi_tuple += ("Publicidad",)
# print(id(mi_tuple))
# print(mi_tuple)

#### Listas  nidadas en Tuples


# mi_tuple += ([2,4,6,10],)
# print(mi_tuple[2]) # Slice funciona tambien en tuple

#### Tres manera qe eleminar un elemento de un tuple al final

# mi_tuple = mi_tuple[:-2] # es la manera mas comun para remover usando -
# print(mi_tuple)

#### Tres manera qe eleminar un elemento de un tuple al inicio
# mi_tuple = mi_tuple[1:] 
# print(mi_tuple)

# Eliminando un elemento especifico messy no recomendado
# arr_tuple = list(mi_tuple)
# arr_tuple.remove("Caty")
# mi_tuple = tuple(arr_tuple)
# print(mi_tuple)

#### Uso de tuple como llave(Key) de dictonary

# index_proritario = {
#   (1, "primero"): [1, 2, 3 ],
#   (1, "segundo"): [14, 12, 13 ],
#   (1, "tercero"): [11, 42, 33 ]
# }
# print(list(index_proritario.keys()))

#### Uso de la funcion ZIP para unir listas en una tuple

personas = ["CG", "SS", "CG"]
dinero = [1000, 2000, 1045]

millonario = zip(personas, dinero)
print(list(millonario))

# Cuando usas zip, crea un iterador—un objeto especial que genera sus valores uno por uno a medida que lo usas. Una vez que recorres todos sus valores (por ejemplo, convirtiéndolo en una lista o iterando sobre él), queda vacío y no se puede usar de nuevo.