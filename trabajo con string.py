# comida_terminada = True
# total = 100
# tip = total * 1/5
# total = total + tip
# recibo = "Tu billete es" + str(total)

# print(total)


# first = "Sasa"
# second = "Caty"
# third = "Clau" # TODO: bla bkab 


string = "Hola como estas"
new_string = "Caty" + string[:4]

# string_mayuscula = string.upper()
# string_mayuscula = string.capitalize()
# string_mayuscula = string.title()
# string_mayuscula = string.lower()

print(new_string)


# print(string_mayuscula)

# content = """
# fdsfgsdf fdgfsgsfh sgfhf thfjdygj jtyfjtr tryueruy eu6et7uie rtywr5y

# fdfghf ghdghjdghjg ghdgjjkf

# fdgdsgds hdrfhdfhd
# """.strip()

# print(repr(content))

# import operator 
# from functools import reduce

# def dinamic_reducer(nums, operandi):
#   ops = {
#     '+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.truediv,
#   }


#   return reduce(ops[operandi], nums)


# print(dinamic_reducer([1, 2, 3], '+'))
# print(dinamic_reducer([1, 2, 3], '-'))
# print(dinamic_reducer([1, 2, 3], '*'))
# print(dinamic_reducer([1, 2, 3], '/'))

# name = "Catary"
# saludos = f""" Hola {name}
# feliz cumple {name}
# """

# print(saludos)


# todo = f"""Hola {nombre}, tienes {edad} anos y has gamado {producto}""" # .format(nombre, edad, producto)
# print(todo)

# frase = "Yo quiero ganar el euromillon"

# respuesta = frase.find("euromillon")
# respuesta_dos = frase.index("euromillon")
# respuesta_tres = "euromillon" in frase

# if ("euromillon" in frase):
  # print(frase)



# print(respuesta_tres)

# frase = frase.replace("euromillon", "primitiva")

# print(guardada)

# index_negativo = frase[-9:]

# print(index_negativo)

# url = "https://bubulazi.com"

# print(url.strip("https://"))

# print(url.lstrip("https://").rstrip(".com").capitalize())

# text = "Titulo: Soy una pendeja"

# titulo, _, subtitulo = text.partition(": ")


# print(subtitulo)

# subtitulo = text.split()
# print(subtitulo)

# numero_cadena = "5"
# cadena = "hola"
# numeros = 1254

# print(numero.isalpha())
# print(cadena.isalpha())

# print(numero_cadena.isnumeric())
# print(cadena.isnumeric())
# print(numeros.is_integer())

# print(6+5)
# print(6-5)
# print(6/5)
# print(6//5) # floor divicion redondear hacia abajo
# print(6%5)
# print(6*5)
# print(6**5) # exponente