# Curso profesional de python

## Practica de tipado estatico

Para utilizar mypy vamos a ejecutar el archivo así:

```mypy palindrome.py``` --check-untyped-defs

este flag nos perdimete ver cuando se esta ejecuntando algo con un tipo de parámetro que no corresponde

## Scope
El scope es el alcance que tienen las variables. Depende de donde declares o inicialices una variable para saber si tienes acceso. Regla de oro:

**una variable solo esta disponible dentro de la region donde fue creada**

Local Scope
---
Es la región que corresponde el ámbito de una función, donde podremos tener una o mas variables, las variables van a ser accesibles únicamente en esta region y no serán visibles para otras regiones

Global Scope
---
Al escribir una o mas variables en esta region, estas podrán ser accesibles desde cualquier parte del código.

## Clousures
### Nested functinos
Son funciones dentro de otra función.

```
def main():
		a = 1

		def nested():
				print(a)

		nested()
main()

// 1
```

```
def main():
		a = 1

		def nested():
				print(a)

		return nested

my_func =  main()
my_func()

// 1
```

### Clousure

Se da cuando una variable que está en un scope superior es recordada por una función que está en un scope inferior, aunque el scope superior sea eliminado.

```
def main():
		a = 1

		def nested():
				print(a)

		return nested

my_func =  main()
my_func()

del(main)

my_func()

// 1
// 1
```

Reglas para encontrar un clousure
---
* Debemos tener una nested function.
* La nested function debe referenciar un valor de un scope superior.
* La función que envuelve a la nested function debe retornarla también.

```
def make_multiplier(x):
		
		def multiplier(n):
				return x * n

		return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))

// 30
// 20
// 80
```
Donde aparecen los closures?
---
En clases cortas y cuando trabajamos con decoradores.

## Decoradores 
Un decorador es una función que recibe como parámetro otra función, le añade cosas y retorna una función diferente. Tienen la misma estructura que los Closures pero en vez de variables lo que se envía es una función. Ejemplo:
```
def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original.")
        func()
    return envoltura

def saludo():
    print("¡Hola!")

saludo()
# Salida:
# ¡Hola!

saludo = decorador(saludo) # Se guarda la función decorada en la variable saludo
saludo()                   # La función saludo está ahora decorada
# Salida:
# Esto se añade a mi función original.
# ¡Hola!
```
Se puede hacer de manera mas sencilla, con azúcar sintáctica (sugar syntax): Cuando tenemos un código que está embellecido para que nosotros lo veamos de una manera más estática, ayudando a entender de manera mas sencilla el código. De esta manera, tenemos el código anterior:
```
def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original.")
        func()
    return envoltura

def saludo():
    print("¡Hola!")
saludo = decorador(saludo) # Se guarda la función decorada en la variable saludo (se decora)

saludo()                   # La función saludo está ahora decorada 
```
```
def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original.")
        func()
    return envoltura

# De esta manera se decora la función saludo (equivale a saludo = decorador(saludo) de la última línea, quedando ahora en la línea inmediata superior ):
@decorador                
def saludo():
    print("¡Hola!")

saludo()                   # La función saludo está ahora decorada 
```
Esto permite ahorrar código al implementar características (decoradores) comunes a diferentes funciones:
```
def decorator_upper(func):                  # Función decoradora
    def wrapper(text):                      # Función anidada
        return func(text).upper()           # Operación que realiza el decorado a la función (func), inserta el texto a la función original. Convierte todo a mayúsculas.
    return wrapper                          # Devuelve wapper como indica la regla de los Clousures

@decorator_upper                            # Decora la función message
def message(name):
    return f'{name}, recibiste un mensaje'  # Esto es lo que realiza la función message, previo a ser decorada.

@decorator_upper                            # Decora la función warning
def warning(name):
    return f'Usa solo mayúsculas {name}'  # Esto es lo que realiza la función warning, previo a ser decorada.

print(message("Cesar")) # Output: CESAR, RECIBISTE UN MENSAJE
print(warning("Cesar")) # Output: USA SOLO MAYÚSCULAS CESAR
```

## Iteradores
Son una estructura de datos para guardar datos infinitos.

Los iterables son los objetos que podemos recorrer a través de un ciclo dicho de otra manera, son estructuras de datos divisibles en elementos que puedo recorrer en un ciclo.

Todos los iterables pueden convertirse en iteradores. De esta manera es que internamente Python los puede recorrer realmente, esto mediante parsing usando el comando iter.
```
# Creando un iterador
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# Iterando un iterador
print(next(my_iter)) # Next nos permite acceder al siguiente elemento del iterador por cada llamada 

# Cuando no quedan datos, la excepción StopIteration es elevada
```

Si queremos crear un código que nos permita recorrer todos los elementos de nuestra lista usando la función next para como aparece en el ejemplo anterior, tendríamos que realizar un bloque try-except:
```
# Creando un iterador
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# Iterando un iterador
while True:
	try:
		element = next(my_iter)
		print(next(my_iter)) # Next nos permite acceder al siguiente elemento del iterador por cada llamada 
	except StopIteration:
		break                # Salimos del ciclo una vez que obtenemos el último valor iterable
```
Lo anterior es posible hacerlo de una manera mucho más sencilla, mediante el ciclo for el cual es azúcar sintáctica pues facilita y realiza de una manera mas estética y sencilla una operación:
```
my_list = [1, 2, 3, 4, 5]

for element in my_list
	print ("element")
```
Es posible crear un iterador personalizado (directamente, sin castear/casting) el cual nos permita recorrer un infinito número de elementos de acuerdo a una función dada, utiliza dos métodos internos importantes: “iter” y “next”.

El uso de una función que determina los valores a iterar nos permite ahorrar memoria y trabajar más rápido, pues no tenemos que almacenar cada uno de los valores, sino solo una función para extraer cada uno de los elementos.

El siguiente ejemplo crea un iterador que recorre todos los números pares:

```
class EvenNumbers:
  """Clase que implementa un iterador de todos los números pares,
  o los números pares hasta un máximo que definimos
  """

  # Constructor
  def __init__(self, max = None): # self = objeto futuro creado con esta clase
    self.max = max

  # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
  def __iter__(self):
    self.num = 0            # Primer número par
    return self             

  # Método para tener la función "next" del ciclo for, es decir, recorrer cada valor.
  def __next__(self):
    if not self.max isNone or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration
```

## Generadores
Sugar syntax de los iteradores. Los generadores son funciones que guardan un estado. Es un iterador escrito de forma más simple.
```
def my_gen():

  """un ejemplo de generadores"""

  print('Hello world!')
  n = 0
  yield n # es exactamente lo mismo que return pero detiene la función, cuando se vuelva a llamar a la función, seguirá desde donde se quedó

  print('Hello heaven!')
  n = 1
  yield n

  print('Hello hell!')
  n = 2
  yield n


a = my_gen()
print(next(a)) # Hello world!
print(next(a)) # Hello heaven!
print(next(a)) # Hello hell!
print(next(a)) StopIteration
```
yield es una palabra reservada similar a return, pero en lugar de terminar la función, yield la pausa, es decir que si la función se vuelve a llamar, esta comienza desde donde se llamó al ultimo yield.

Ahora veremos un generator expression (es como list comprehension pero mucho mejor, porque podemos manejar mucha cantidad
de información sin tener problemas de rendimiento):
```
#Generator expression

my_list = [0,1,4,7,9,10]

my_second_list = [x**2 for x in my_list] #List comprehension
my_second_gen = (x**2 for x in my_list) #Generator expression
```
Como se puede ver en el ejemplo, la diferencia en la sintaxis únicamente es en el uso de paréntesis en lugar del uso de corchetes.

Ventajas de los Generadores:

* Es mas fácil de escribir que un iterador
* Ahorra Tiempo y Memoria
* Permite guardar secuencias infinitas

## Sets
Conjuntos: Una colección desordenada de elementos únicos e inmutables.

Características:
Un set al ser impreso puede presentar diferente orden al definido pues Python los ordena a modo de optimizar/ahorrar memoria: un set es una colección desordenada.
En caso de existir elementos repetidos, los elimina, pues: un set es una lista de elementos únicos.
En caso de indicar una lista, por ejemplo, en un set este nos arroja un error, dado que: un set es inmutable.
Al set no se puede acceder con un índice.

Para declarar un set, el grupo de elementos debe ir entre llaves. Se diferencia de los diccionarios ya que no contienen el símbolo “:”, por lo que automáticamente Python lo entiende como un set de datos.

```
# set de enteros
my_set = {1, 3, 5}
print(my_set)

# set de diferentes tipos de datos
my_set = {1.0, "Hi", (1, 4, 7)}
print(my_set)
```

En caso de desear declarar un set vacío no es posible usar llaves ya que al no contener datos entre las llaves las interpreta como un diccionario. En este caso la declaración de un set debe ser explicita mediante el comando set()

Casting con Sets
Para convertir una estructura de datos a un set se utiliza el comando set()

Si se castea una lista a un set como resultado tenemos un set de elementos únicos ya que elimina los elementos repetidos. Los elementos mutables, en caso de existir, este comando los eliminará.

Agregando elementos a un Set
Para agregar un solo elemento se utiliza el método .add de los sets, en cambio, para agregar múltiples elementos se utiliza el método .update. En ambos se eliminan todos los elementos que fuesen repetido en el set o mutables.

Eliminando elementos de un Set
Existen 4 métodos:

* `.discard()` = Se indica como parámetro el elemento a eliminar, en caso de no exisitir el elemento no realiza ninguna operación y continúa con la ejecución.
* `.remove()` = También se indica como parámetro el elemento a eliminar, pero en este caso si no exististe el elemento arroja un error (KeyError) y detiene la ejecución.
* `.pop()` = Elimina un elemento del set de manera aleatoria.
* `.clear()` = Limpia el set completo.

```
#ejemplo de operaciones sobre sets 
my_set = {1, 2, 3} 
print(my_set) #Output {1, 2, 3} 

#añadiendo un elemento al set 
my_set.add(4) 
print(my_set) #Output {1, 2, 3, 4}

#añadiendo varios elementos al set, python ignorará elementos repetidos 
my_set.update([1, 5, 6]) 
print(my_set) #Output {1, 2, 3, 4, 5, 6}

# eliminado elementos del set 
my_set.discard(1) 
print(my_set) #Output {2, 3, 4, 5, 6}

# borrando un elemento aleatorio 
my_set.pop()
print(my_set) #Output el set menos un elemento aleatorio 

#limpiar el set 
my_set.clear()
print(my_set) # Output set() 
```

Podemos utilizar estructuras de datos existentes para transformarlas a sets utilizando el método set:
```
#usando listas para crear sets
my_list = [1, 2, 3, 3, 4, 5]
my_set = set(my_list)
print(my_set)  #output {1, 2, 3, 4, 5}

#usando tuplas para crear sets 
my_tuple: ('hola', 'hola', 1, 2)
my_set2: set(my_tuple)
print(my_set2) #Output {'hola', 1}
```

### Operaciones con Sets
#### Unión
Resultado de juntar todos los elementos que tienen ambos, combinar ambos sets
```
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 | set_2 #  -> {1, 2, 3, 4, 5}

# O de forma mas explicita
set_1.union(set_2) #  -> {1, 2, 3, 4, 5}
```
#### Intersección
Los que se repiten en ambos sets
```
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 & set_2 #  -> {3}

# O de forma mas explicita
set_1.intersection(set_2) #  -> {3}
```
#### Diferencia
Tomar dos sets y de uno quitarle todos los elementos que tiene el otro
```
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 - set_2 #  -> {1, 2}

# O de forma mas explicita
set_1.difference(set_2) #  -> {1, 2}
```
#### Diferencia Simétrica
Tomar todos los elementos exceptos los que se repiten
```
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 ^ set_2 #  -> {1, 2, 4, 5}

# O de forma mas explicita
set_1.symmetric_difference(set_2) #  -> {1, 2, 4, 5}
```

## Manejo de fechas
datetime es un módulo de manejo de fechas.
```
import datetime

my_time = datetime.datetime.now() # hora local de mi PC u hora universal
my_date = datetime.date.today() # fecha actual

my_day = datetime.date.today()

print(my_time)
print(my_date)

print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')
```

Tabla de códigos de formato para fechas y horas(los más importantes):

| Formato  | Código |
| -------- | ------ |
| Año      | %Y     |
| Mes      | %m     |
| Día      | %d     |
| Hora     | %H     |
| Minutos  | %M     |
| Segundos | %S     |

```
from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

latam = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {latam}')

usa = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {usa}')

random_format = my_datetime.strftime('año %Y mes %m día %d')
print(f'Formato random: {random_format}')

formato_utc = datetime.utcnow()
print(f'Formato UTC: {formato_utc}')
```
Más comandos [aquí](https://docs.python.org/es/3/library/datetime.html#strftime-and-strptime-format-codes)