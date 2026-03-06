#### Funciones y métodos sus sintaxis

# def auth(email, password):
#   if email == "catary@gmail.com" and password == 12563:
#     print("Autorizado")
#   else:
#     print("No autorizado")

# auth("catary@gmail.coms",12563)


#### Funciones anidadas

# def greeting(first, last):
#   def full_name():
#     return f'{first} {last}'

#   print(f'Hi {full_name()}!')


# greeting('Kristine', 'Hudgens')


#### Argumnetos por defecto 
# def greeting(name = 'Guest'):
#   print(f'Hi {name}!')

# greeting()
# greeting('Kristine')

# # Nope
# def some_function(collection = []): # No se deberia dar como un argumento por defecto una lista vacia porque simpre retornará uno nuevo, se considera mala practica en python.
#   collection.append(1)
#   print(id(collection))
#   return collection


# print(some_function())
# print(some_function())

#### Argumentos con nombre, no tiene que estar en el orden del argumneto de la function

# # def full_name(first, last):
# #   print(f'{first} {last}')


# # full_name('Kristine', 'Hudgens')
# # full_name(first = 'Kristine', last = 'Hudgens')
# # full_name(last = 'Hudgens', first = 'Kristine')


# #### Sacando los argumnetos de la funcion en JS es como el parametro rest

# def greeting(*args):
#   print('Hi ' + ' '.join(args))


# greeting('Kristine', 'M', 'Hudgens')
# greeting('Tiffany', 'Hudgens')


# def greeting(*names):
#   print('Hi ' + ' '.join(names))


# greeting('Kristine', 'M', 'Hudgens')
# greeting('Tiffany', 'Hudgens')


# def greeting(time_of_day, *args):
#   print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


# greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
# greeting('Morning', 'Tiffany', 'Hudgens')


####  Argumentos nombrados unidos con el rest operator (JS)

# def greeting(**kwargs): # Este nombre del argumneto suele usarse entre los progranadores de Python
#   print(kwargs)


# greeting()
# greeting(first = 'Kristine', last = 'Hudgens')

# def greeting(**kwargs):
#   if kwargs:
#     print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
#   else:
#     print('Hi Guest!')


# greeting()
# greeting(first = 'Kristine', last = 'Hudgens')

# Combinar todos los tipos de argumentos en una funcion 

# def greeting(time_of_day, *args, **kwargs):
#   print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

#   if kwargs:
#     print('Your tasks for the day are:')
#     for key, val in kwargs.items():
#       print(f'{key} -> {val}')


# greeting('Morning',
#          'Kristine', 'Hudgens',
#          first = 'Empty dishwasher',
#          second = 'Take pupper out',
#          third = 'math homework')

#### Funciones Lambda (son funciones inline anonmas parecidas a las Arrow => de JS)
# full_name = lambda first, last: f'{first} {last}'
# # print(full_name("Caty", "Sasa"))

# def greeting(name):
#   print(f'Hi there {name}')


# greeting(full_name('Kristine', 'Hudgens'))

#### In the code below, create a variable called "greeting" and assign it a lambda function that accepts a name as an argument, and return the string "Hi, name".

# def lambda_practice():
#   greeting = lambda name: f"Hi, {name}"
#   return greeting

# print(lambda_practice()("Caty")) # lamda_practice retorna greeting sin ejecutar la misma . Luego, inmediamnete la ejecuta anidandole un argumento.

#### Print del 1 al 100 y si es divisible por 3 print "fizz" y si es divisble por 5 print "buzz", y si es divisible por el 3 y 5 print "fizzbuzz"

def mi_fizz_buzz(min_num, max_num):
  for num in range(min_num, max_num + 1):
   if num % 3 == 0 and num % 5 == 0:
     print("fizzbuzz")
   elif num % 3 == 0:
     print("fizz")
   elif num % 5 == 0:
     print("buzz")
   else:
     print(num) 

mi_fizz_buzz(1,100)