#### Caracteristica de un Set es que no permite duplicado:

# mi_set = {1, 4, 6, 7, 8, 4, 40}
# print(mi_set)

# query_one = 4 in mi_set
# print(query_one) # True

#### Varios metodos para unir dos Set juntos

# # Unir dos set en uno nuevo
# mi_set_uno = {"CGR", "SSP", "CPG", "SSP"}
# mi_set_dos =  {"LLM", "SSP", "CPG", "RTI"}

# set_juntos = mi_set_uno | mi_set_dos
# # print(set_juntos)

# # Solo los elementos que no esta en la segunda

# solo_primera = mi_set_uno - mi_set_dos
# solo_segunda = mi_set_dos - mi_set_uno
# # print(solo_segunda)

# # Solo los eleemntos que se encuentran en varios Set
# en_ambos = mi_set_uno & mi_set_dos
# print(en_ambos)

