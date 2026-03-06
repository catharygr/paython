#### Las clases en paython tienen las mismas funcionalidades que las clases JS> Genrador de objectos con metodos y funciones y todo lo demas parecido. Las clases se componen de datos y comportamiento.

# class Invoice:

#   def greeting(self):
#     return 'Hi there'


# inv_one = Invoice()
# print(inv_one.greeting())


# Para añadir datas usamos constructor
# class Factura:
#   def __init__(self, cliente, total):
#     self.cliente = cliente
#     self.total = total

#   def imprimir(self):
#     return f"El cliente {self.cliente} nos debe {self.total}€"
  
# factura0024 = Factura("Clafer", "200")
# factura0025 = Factura("Blacondent", "800")

# print(factura0024.imprimir())
# print(factura0025.imprimir())

# Using our Garage class from the previous guide, add a constructor method that builds a property named size, which will represent how many cars will fit in the garage as an integer. Instantiate the home object to be a 2 car garage.

# class Garage:
#   def __init__(self,size):
#     self.size = size
    

#   def garage_size(self):
#     return f"This garage accepts {self.size}"
    
# home = Garage(2) 
# print(home.garage_size())

#### Get y Set en las clases 

# Las funciones Setter y getter son necesarias solamente en el caso de necesitar una logica mas compleja.


# We've added an array of cars to our garage. All of the vehicles are out for the day, and we need to update the array. Now that you've seen getters and setters, use a setter to update the cars array to reflect all cars being gone. Then, in the get_cars variable, get the cars data from the home object.

# Starter code
# class Garage:
#   def __init__(self, size):
#     self.size = size
#     self.cars = ["Ram", "Model 3"]

#   def open_door(self):
#     return "The door opens"
    
# home = Garage(2)

# home.cars = []
# get_cars = home.cars

#### Decoradores property (__init__ es Contructor en JS)

# class Invoice:

#     def __init__(self, client, total):
#         self._client = client
#         self._total = total

#     def formatter(self):
#         return f'{self._client} owes: ${self._total}'

#     @property # GETTER
#     def client(self):
#         return self._client

#     @client.setter #SETTER
#     def client(self, client):
#         self._client = client

#     @property # GETTER
#     def total(self):
#         return self._total

# google = Invoice('Google', 100)

# print(google.client)

# google.client = 'Yahoo'

# print(google.client)

# We want to ensure that our size attribute can be retrieved, but not set. Use the appropriate syntax to protect the size attribute. Then, use the 'property' decorator to build a getter to return the protected data. You do not need to instantiate the class.

# class Garage:
#   def __init__(self, size):
#     self._size = size
#     self.cars = []

#   @property
#   def size(self):
#    return self._size 

#   def open_door(self):
#     return "The door opens"


#### Pepaso del metodo DUNDER en __init__ Son metodos especailes que se escriben com __ y permiten definir como los objectos se comportan con las operaciones predefinidas en PYTHON como, imprimir, sumar y comparar.
# __init__(self, ...): Constructor, called when you create a new object.
# __str__(self): Defines the string representation (used by print()).
# __repr__(self): Official string representation, used in debugging.
# __len__(self): Defines behavior for len(obj).
# __eq__(self, other): Defines equality (==) comparison.
# __add__(self, other): Defines addition (+) behavior.


# class Invoice:
#  def __str__(self):
#     return "This is the invoice class!"


# inv = Invoice()
# print(str(inv))

# class Invoice:
#   def __init__(self, client, total):
#     self.client = client
#     self.total = total

#   def __str__(self): #
#     return f"Invoice from {self.client} for {self.total}"

#   def __repr__(self):
#     return f"Invoice({self.client}, {self.total})"


# inv = Invoice('Google', 500)
# print(str(inv))
# print(repr(inv))

#### Custom Iterator Class en PYTHON

# class Lineup:

#     def __init__(self, players):
#         self.players = players
#         self.last_player_index = (len(self.players) - 1)

#     def __iter__(self): # Para iterar en Python
#         self.contador = 0
#         return self

#     def get_player(self, contador):
#         return self.players[contador]

#     def __next__(self):
#         if self.contador < self.last_player_index:
#             player = self.get_player(self.contador)
#             self.contador += 1
#             return player
#         elif self.contador == self.last_player_index:
#             player = self.get_player(self.contador)
#             self.n = 0
#             return player


# astros = [
#   'Springer',
#   'Bregman',
#   'Altuve',
#   'Correa',
#   'Reddick',
#   'Gonzalez',
#   'McCann',
#   'Davis',
#   'Tucker'
# ]

# astros_lineup = Lineup(astros)
# process = iter(astros_lineup)

# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
