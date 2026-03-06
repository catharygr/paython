#### Condiciones en Python

# age = 66

# if age < 25:
#   print("No puedes alquilar")
# elif age < 65:
#   print("Puedes fumarte un porro conduciendo")
# else:
#   print("Si no te da un infarto antes")

# In the below starter code, place 4 dog names (elements) of your choice in the dog_house list. Then write a while loop that iterates through the dog_house list and prints each dogs name. An iterator variable named "counter" must be set, and must have an initial value of 0.

# Hint: An iterator value (also sometimes called a sentinel value) is a value that exists outside of your loop, and that you update or otherwise keep track of each time you loop, so that your while loop knows when to end.

# Example:
# iterator_value = 0
# while iterator_value < 10:
#     print("Keep looping...")
#     iterator_value += 1


#### Operador Ternary

# role = "admins"
# auth = " Puede acceder" if role == "admin" else "No puede acceder"
# print(auth)

#### Todas la lista de los opradores de las condiciones


# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to
# Tambien hay IS que es parecido a ===

#### Como verificar si un valor esta presente en una lista o string

# frase = "Hola estas ahi?"
# palabra = "Holas"
# if palabra in frase:
#   print("esta")
# else: 
#   print("no esta")

# nums = [1, 2, 3, 4]
# if 5 in nums: 
#   print("esta")
# else: 
#   print("No esta")

#### Como unir condicionales en Python es como && || en JS

nombre = "Caty"
email = "catary@gmail.com"
password = "23456AB"

# if nombre == "Caty" and  email == "catary@gmail.com":
#   print("Puedes entrar")
# else: 
#   print("No puedes entrar")

# if nombre == "Catys" or  email == "catary@gmail.coms":
#   print("Puedes entrar")
# else: 
#   print("No puedes entrar")

# if (nombre == "Catys" or  email == "catary@gmail.com") and password == "23456AB":
#   print("Puedes entrar")
# else: 
#   print("No puedes entrar") # Si quiero que evalue primero una parte tengo que meterlo en ()

#Esta condicion es como !var en JS
# logueado = True
# admin = False
# if logueado and not admin:
#   print("YES")
# else: 
#   print("No")


