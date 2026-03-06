##### Dictonaries que son los objectos en JS

# jugadores = {
#   "esqui": "Sasa",
#   "bici": "Cathy",
#   "patineta": "Cathy",
#   "baile": "Zorka"

# }

# print(jugadores["baile"])

##### Dictonaries Nidados

# equipos = {
#   "personas": ["Sasa","Cathy","Cathy","Zorka" ],
#   "coches": {
#     "rapido": "Ficho"
#   }
# }

# print(equipos["personas"][1])
# print(equipos["coches"]["rapido"]

#### Añadir una Key?value par a un dictonaries

# equipos = {
#   "personas": ["Sasa","Cathy","Cathy","Zorka"],
#   "coches": ["rapido", "Ficho"]
# }

# equipos["bicis"] = ["speecializes", "Orbea"]
# equipos["coches"][0] = "Lento"
# print(equipos)

#### Function Get 


# equipos = {
#    "personas": ["Sasa","Cathy","Cathy","Zorka"],
#    "coches": ["rapido", "Ficho"]
# }

# futuros_equipos = equipos.get("personas", "No existe este elemento") # Se usa el metodo get para obtener valores, si existen y si no existe retornara algo

# print(futuros_equipos)

#### Uso de .keys() .value() & .items() es similar a como se usa en JS los Object.value, keys e entreis



# # print(equipos.keys())
# # # print(equipos.values())
# # # print(equipos.items()) # Esto devuelve en forma de tuplas

# print(list(equipos.keys())[1]) # Es la maera de convertir un dictonary view a una lista/array es asi [1] como si fuera con .slice

# Para evitar lo de la actualiacion dinamica de una dictonary view debemos hacer la copia local y asi desconcetar del diccionario original. Usamos .copy()

# copias_equipos = list(equipos.copy().keys())
# print(copias_equipos)

# items_personas = list(equipos.items())
# print(items_personas[1][1][1])

#### Diferentes metodos para borrar elementos para un dictonaries

usuario = {
  "name": "Cathy",
  "edad": 55,
  "hobby": "Esquiar",
  "coches": ["ficho", "peygi"]
}

# del usuario["edad"] # del funciona si sabemos que el elemento existe si no daria error, la solucion seria usar pop que retorna el segundo argumneto si no existe lo que buscamos
# solucion_pop = usuario.pop("edades", "Fallo de cojones")
# print(solucion_pop)

#### Como trabajar con lista /array con varios dictonaies dentro

equipos = [{
  "LPA": {
    "primero": "Sasha",
    "segundo": "Cathy",
    "tercero": "Clau"
  }
},{
  "BIO": {
    "primero": "Almudena",
    "segundo": "Juan Carlos",
    "tercero": "JUanma"
  }
}]

# print(equipos[0])
# bilbao = equipos[1].get("BIO", "Equipo no encontrado")

# print(list(bilbao.values())[0])

#### Ejercici: Crear un Hitogramo con Python

ventas = {
  "google": 12,
  "apple": 20,
  "TIKTOK": 16,
}



print("A: ", ventas.get("apple", "está") * "$") 
print("B :", ventas.get("google", " no está") * "$") 
print("C :", ventas.get("TIKTOK", "está") * "$") 
