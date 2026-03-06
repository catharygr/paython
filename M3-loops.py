#### Generando un header en HTML con una función 

# def generando_header(contenido, nivel):
#   return f"<h{nivel}>{contenido}</h{nivel}>"

# headerUno = generando_header("Hola jili", 4)
# print(headerUno)

#### Loops en Python
## Lista
# personas = ["Caty", "Sasa", "Clau", "Zorka"]
# for persona in personas:
#   print(persona)

##Tuple
# personas = ("Caty", "Sasa", "Clau", "Zorka")
# for persona in personas:
#   print(persona)

## Dictonary
# personas = {
#   "primera": "Caty",
#   "segunda": "Sasa",
#   "tercera": "Clau",
#   "cuarta": "Zorka"
# }

# for key, valor in personas.items():
#   print(f"La {key} persona es: {valor}")
  

#### Loops con Strings
# alfabetos = "abcdfghi"
# for alfabeto in alfabetos:
#   print(alfabeto)


#### Loops for in => en funcion range() Igual foor loop n JS

# for num in range(2, 20, 2): # Incluye el primero pero no el ultimp
#   print(num)

#### Uso de Continue y Break en loop en Python
# personas = ["Caty", "Sasa", "Clau", "Zorka"]
# for persona in personas:
#   if persona == "Caty":
#     print(f"persona {persona}, No eres bienvenida")
#     continue # continue salta el resto de codigo y sigue iterando con el siguiente elemento 
#   if persona == "Clau":
#     print(f"persona {persona}, Eres bienvenida y lo encontramos en el index: {personas.index(persona)}")
#     break # Salta del resto de codigo y para el look
#   else: 
#      print(f"persona {persona}, La que sea")

#### For loop While

# nums = list(range(2, 20, 2))
# while len(nums) > 0:
#   print(nums.pop())

# def game(): # True y False debe estar combinado
#   while True: # mira donde esta false
#     print("Adivina el numero")
#     guees = input()

#     if guees == "48":
#       print("bingo")
#       return False # Retornando false se sale por completo de la iteración
#     else: 
#       print("No")

    
# game()

#### Combinar y aplanar(flatten) List con for/in loop

# primeras_personas = ["Caty", "sasa"]
# segundas_personas = ["Clau", "Zorka"]

# # for persona in primeras_personas:
# #   segundas_personas.append(persona)

# segundas_personas.extend(primeras_personas)

# print(segundas_personas)

#### Usando el listado de comprencion en Python

# numeros = [x for x in range(2, 20) if x % 2 == 1 ]
# print(numeros)

