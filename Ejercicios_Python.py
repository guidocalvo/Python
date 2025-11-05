# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencias_letras(cadena):

    frecuencias = {}

    for caracter in cadena:
        if caracter != " ":
            caracter = caracter.lower()
            if caracter in frecuencias:
                frecuencias[caracter] +=1
            else:
                frecuencias[caracter] = 1

    return frecuencias

texto = "hola mundo"
print (frecuencias_letras(texto))


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def duplicador(numero):
    
    numero *= 2
    
    return numero

lista_numeros = [1,2,3,4,5]

lista_resultado_map = list(map(duplicador,lista_numeros))

print(f"El resultado de la función map es: {lista_resultado_map}")


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def funcion_palabra_objetivo(lista_palabras, palabra_objetivo):
    palabra_objetivo = palabra_objetivo.lower()
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra.lower()]


palabras = ["Camion","Camino","Cama","Leon","Coche","Camello"]

palabra_clave = "cam"

lista_prueba = funcion_palabra_objetivo(palabras,palabra_clave)

print(lista_prueba)


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencias(lista1, lista2):

    return list(map(lambda x, y: x - y, lista1, lista2))

lista_numeros = [1,2,3,4,5]

lista_numeros2 = [0,1,2,3,4]

resultado = diferencias(lista_numeros, lista_numeros2)
print("Diferencias:", resultado)


# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def evaluar_lista(numeros, nota_aprobado=5):
    
    media = sum(numeros) / len(numeros)  # Calcular la media
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# Ejemplo de uso:
notas = [6, 7, 5, 4, 8]
resultado = evaluar_lista(notas)
print(resultado)  # Salida: (6.0, 'aprobado')


# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Salida: 120


# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tupla_a_strings(tuplas):
    lista = []
    for tupla in tuplas:
        for item in tupla:
            lista.append(str(item))

    return lista

lista_tuplas_fecha = [("Enero","Febrero","Marzo"),("Lunes","Martes","Miercoles","Jueves"),(2020,2021,2022)]

#lista_final = list(map(tupla_a_strings,lista_tuplas_fecha))

lista_final = tupla_a_strings(lista_tuplas_fecha)

print(lista_final)


# 8 Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

while True:
    try:
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese otro número: "))
        print(f"El resultado de la división es: {numero1/numero2:.2f}")
    except ValueError:
        print("Error -> Debe ingresar un número.")
        print("La división no fue exitosa.")
    except ZeroDivisionError:
        print("Error -> Un número no se puede dividir entre 0.")
        print("La división no fue exitosa.")
    else:
        print("La división fue exitosa.")
        break


# 9 Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()

def mascotas_permitidas(mascota):
    mascotas_prohibidas = ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]

    return mascota not in mascotas_prohibidas

test_de_mascotas = ["Perro","Gato","Oso","Tortuga","Loro","Tigre"]

print(list(filter(mascotas_permitidas, test_de_mascotas)))


# 10 Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

def comprobar_lista(lista_numeros):
    try:        
        if lista_numeros == []:
            raise ValueError ("La lista no puede estar vacía.")
        else:
            print(sum(lista_numeros) / len(lista_numeros))            
    except ValueError as error:
        print(f"Error: {error}\n")


lista1 = [10,20,30,40,50]

lista2 = []

comprobar_lista(lista2)


# 11 Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            
            if edad < 0 or edad > 120:
                raise TypeError("La edad debe estar entre 0 y 120.")
            
            print(f"Tienes {edad} años.")
            break

        except ValueError:
            print("Error: Debe ingresar un número.\n")

        except TypeError as error:
            print(f"Error: {error}\n")

pedir_edad()


# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    lista = []
    for palabra in frase.split():
        contador = 0
        for letra in palabra:
            contador += 1
        lista.append(contador)

    print(lista)

frase1 = "Esta es la primer frase"

frase2= "Otra frase para confirmar que el programa funciona correctamente."

longitud_palabras(frase1)


def longitud_palabras(lista):
    lista = []
    for frase in frases:
        for palabra in frase.split():
            contador = 0
            for letra in palabra:
                contador += 1
            lista.append(contador)

    return lista

frases = ["Esta es la primer frase","Otra frase para confirmar que el programa funciona correctamente","Y una mas para probar"]

hola = list(map(longitud_palabras,frases))

print(hola)


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

def mayus_minus(conjunto):    
    unicos = sorted(set(conjunto))    
    return list(map(lambda c: (c.upper(), c.lower()), unicos))

print(mayus_minus(['a', 'b', 'A', 'c', 'C', 'b']))


# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()

letra_inicial2 = lambda palabra: palabra[0]=="A"

lista = ["Alemania","Argentina","Bolivia","Bulgaria","Croacia","Dinamarca"]

print(list(filter(letra_inicial2,lista)))


# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

lista = range(1,11)

lista_final = list(map(lambda numero: numero + 3, lista))

print(lista_final)


# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()

def tamaño_palabra(cadena, caracteres):

    lista_palabras = cadena.split()

    lista_filtrada = list(filter(lambda palabra: len(palabra)>caracteres, lista_palabras))

    return lista_filtrada


numero = 5
frase1 = "Esta es la frase de ejemplo para comprobar que funcione."

print(tamaño_palabra(frase1,numero))
      

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

# Ejemplo de uso
print(lista_a_numero([5, 7, 2]))  # Salida: 572


# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter()

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 88},
    {"nombre": "María", "edad": 19, "calificacion": 91},
    {"nombre": "Carlos", "edad": 21, "calificacion": 76},
    {"nombre": "Sofía", "edad": 20, "calificacion": 90}
]

# Usamos filter() para obtener los estudiantes con calificación >= 90
estudiantes_destacados = list(filter(lambda est: est["calificacion"] >= 90, estudiantes))

# Mostramos los resultados
print("Estudiantes con calificación mayor o igual a 90:")
for est in estudiantes_destacados:
    print(f"Nombre: {est['nombre']}, Edad: {est['edad']}, Calificación: {est['calificacion']}")


# 19. Crea una función lambda que filtre los números impares de una lista dada.

lista_numeros = range(1,11)

impares = lambda x: x%2 != 0

print(list(filter(impares,lista_numeros)))


# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

lista = [1,"Hola",4,7,9,"Mundo",6,"Python"]

solo_integer = lambda x: isinstance(x,int)

print(list(filter(solo_integer,lista)))


# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

numero = 8

cubo = lambda x: x**3

print(cubo(numero))


# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce()

from functools import reduce

lista = range(1,11)

producto_total = lambda x,y: x*y

print(reduce(producto_total,lista))


# 23. Concatena una lista de palabras. Usa la función reduce()

from functools import reduce

lista_palabras = ["Esta","es","una","lista","de","palabras"]

palabras_unidas = lambda x,y: x+" "+y

print(reduce(palabras_unidas,lista_palabras))


#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()

from functools import reduce

lista_numeros = [10,5,-8,2,-3,10,4,5,-7]

diferencia_total = lambda x,y: x-y

print(reduce(diferencia_total,lista_numeros))


# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

cadena = "Esta es una cadena de texto de ejemplo."

suma_caracteres = lambda x: len(x)

print(suma_caracteres(cadena))


# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

x = 31
y = 4

resto_divison = lambda x,y: x%y

print(resto_divison(x,y))


# 27. Crea una función que calcule el promedio de una lista de números.

lista_numeros = [5,3,2,8,11]

promedio = lambda x: sum(x)/len(x)

print(promedio(lista_numeros))


# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def duplicado(lista):
    lista_temporal = []
    for elemento in lista:
        if elemento in lista_temporal:
            return elemento
        else: 
            lista_temporal.append(elemento)
    
    
lista1 = ["Hola",1,2,3,4,"Mundo",1,"Mundo",2]

lista2 = ["Libro","Boligrafo","Carpeta","Mochila","Carpeta","Cuaderno","Lapiz"]

print(duplicado(lista1))


# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

def enmascarar(variable):

    texto = str(variable)
    
    if len(texto) <= 4:
        return texto

    return '#' * (len(texto) - 4) + texto[-4:]

frase = "Holamundo1234"

print(enmascarar(frase))


# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

def anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
        
print(anagramas("roma","amor"))
print(anagramas("Programacion","Python"))


# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

def nombre_lista():

    print("Ingrese 5 nombres")

    lista_nombres = []

    for i in range(1,6):
        nombre = input("Ingrese un nombre: ")
        lista_nombres.append(nombre)


    while True:
        try:
            nombre_buscado = input("Ingrese un nombre para buscar en la lista: ")
            if nombre_buscado in lista_nombres:
                print(f"{nombre_buscado} se encuentra en la lista.")
                break
            else:
                raise ValueError()
            
        except ValueError:
            print("El nombre no se encuentra en la lista, intentelo de nuevo.")        

nombre_lista()


# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

def buscador_empleado(lista, nombre_buscado):

    for empleado in lista:
        if empleado["nombre"].lower() == nombre_buscado.lower():
            return f"{empleado["nombre"]} trabaja aquí como {empleado["puesto"]}."
            
    return f"{nombre_buscado} no trabaja aquí."

lista_prueba= [{"nombre":"Juan Rodriguez Perez","puesto":"product manager"},
         {"nombre":"Lucia Fernandez Rey","puesto":"jefe de marketing"},
         {"nombre":"Martina Perez Gomez","puesto":"becario en control de gestión"},
         {"nombre":"Larry Johnson Cole","puesto":"formador en control de calidad"},
         {"nombre":"Oscar Paulista Del Rio","puesto":"comercial"},
         {"nombre":"Laura Carreras Flores","puesto":"diseñador"}]


nombre_prueba1 = "Oscar Paulista Del Rio"
nombre_prueba2 = "Jose Felix Fernandez"

print(buscador_empleado(lista_prueba, nombre_prueba1))


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

suma_de_listas = lambda x,y: sum(x) + sum(y)

lista1 = [1,2,3,4,5]
lista2 = [10,20,20,40,50]

print(suma_de_listas(lista1,lista2))


"""
# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol.
Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y 
las longitudes de las mismas.
Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol.
"""
class Arbol():

    def __init__(self):
        self.longitud_tronco = 1
        self.ramas = []
    
    def crecer_tronco(self):
        self.longitud_tronco += 1
    
    def nueva_rama(self):
        self.ramas.append(1)
    
    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1
    
    def quitar_rama(self,numero):
        self.ramas.pop(numero)  
    
    def info_arbol(self):
        print(f"Longitud del tronco: {self.longitud_tronco}")
        for posicion,longitud in enumerate(self.ramas):
            print(f"Longitud de rama {posicion}: {longitud}")
        

arbol_ejemplo = Arbol()

arbol_ejemplo.crecer_tronco()  # tronco -> 2

arbol_ejemplo.nueva_rama()     # ramas -> [1]

arbol_ejemplo.crecer_ramas()   # ramas -> [1]

arbol_ejemplo.nueva_rama()     # ramas -> [2, 1]

arbol_ejemplo.nueva_rama()     # ramas -> [2, 1, 1]

arbol_ejemplo.quitar_rama(2)   # ramas -> [2,1]

arbol_ejemplo.info_arbol()  

"""
36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo.
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".
"""

class UsuarioBanco():
    
    def __init__(self,nombre,saldo,cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self,dinero):
        if dinero > self.saldo:
            raise IndexError(f"No puede retirar ese dinero, su saldo es: {self.saldo}.")    
        else:
            self.saldo -= dinero
    
    def transferird_dinero(self, otro_usuario,cantidad):
        if not isinstance(otro_usuario, UsuarioBanco):
            raise TypeError("Debe transferirse desde otro usuario del banco.")
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.")

        otro_usuario.saldo -= cantidad

        self.saldo += cantidad

        print(f"Transferencia realizada: {otro_usuario.nombre} → {self.nombre} ({cantidad} unidades).")

    def agregar_dinero(self,dinero):
        self.saldo += dinero


#1 Crear usuarios
usuario1 = UsuarioBanco("Alicia", 100, True)
usuario2 = UsuarioBanco("Bob", 50, True)

# 2. Bob agrega 20
usuario2.agregar_dinero(20)   # saldo Bob = 70

# 3. Transferencia de 80 desde Bob a Alicia
usuario1.transferir_dinero(usuario2, 80)
# saldo Bob = -10? no, salta error porque no tiene suficiente

# Corregimos: Bob transfiere 60, por ejemplo
usuario1.transferir_dinero(usuario2, 60)

# 4. Alicia retira 50
usuario1.retirar_dinero(50)

print(usuario1)
print(usuario2)

"""
37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto.
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
número de argumentos variable según la opción indicada.
Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto
"""

def contar_palabras(texto):
    # {Palabra1: 8, Palabra2: 3, ...}
    palabras_repetidas = {}
    palabras = texto.split()
    for palabra in palabras:
        contador = palabras.count(palabra)
        palabras_repetidas[palabra] = contador
    return palabras_repetidas


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    texto_nuevo = texto.replace(palabra_original, palabra_nueva)
    return texto_nuevo


def eliminar_palabra(texto, palabra_eliminar):
    texto_nuevo = texto.replace(palabra_eliminar, "")
    return texto_nuevo


def procesar_texto():
    while True:
        print("Inicio de programa")
        texto = input("Ingrese un texto: ")

        print("""
Menú para procesar texto:
1. Contar las palabras del texto.
2. Reemplazar palabras del texto.
3. Eliminar palabras del texto.
""")

        opcion = int(input("Ingrese una opción de menú: "))

        if opcion == 1:
            print(contar_palabras(texto))
            break

        elif opcion == 2:
            palabra_texto = input("Ingrese la palabra del texto que desea reemplazar: ")
            palabra_nueva = input("Ingrese la palabra nueva: ")
            print(reemplazar_palabras(texto, palabra_texto, palabra_nueva))
            break

        elif opcion == 3:
            palabra_borrar = input("Ingrese la palabra del texto que desea borrar: ")
            print(eliminar_palabra(texto, palabra_borrar))
            break


procesar_texto()

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

hora = int(input("Introduce una hora (0-23):  "))

if hora < 0 or hora > 23:
    print("La hora introducida no es válida. Debe estar entre 0 y 23.")
else:
    if 6 <= hora < 12:
        print("Es de día (mañana).")
    elif 12 <= hora < 20:
        print("Es de tarde.")
    else:
        print("Es de noche.")


"""
39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente
"""

calificacion = int(input("Ingrese la calificación del alumno (0-100): "))

if 0 <= calificacion <= 69:
    print("Insuficiente")
elif 70 <= calificacion <= 79:
    print("Bien")
elif 80 <= calificacion <= 89:
    print("Muy bien")
elif 90 <= calificacion <= 100:
    print("Excelente")
else:
    print("Calificación no válida. Debe estar entre 0 y 100.")


# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area(figura, datos):

    figura = figura.lower()

    if figura == "rectangulo":
        base, altura = datos
        area = base * altura

    elif figura == "circulo":
        (radio,) = datos
        pi = 3.1416
        area = pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        area = (base * altura) / 2

    else:
        raise ValueError("Figura no válida. Usa 'rectangulo', 'circulo' o 'triangulo'.")

    return area


# Ejemplos de uso:
print(calcular_area("rectangulo", (4, 5)))  # ➜ 20
print(calcular_area("circulo", (3,)))       # ➜ 28.2744
print(calcular_area("triangulo", (6, 4)))   # ➜ 12


"""
41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python.
"""

# 1. Solicitar el precio original
precio = float(input("Ingrese el precio original del artículo (€): "))

# 2. Preguntar si tiene cupón
tiene_cupon = input("¿Tiene un cupón de descuento? (si/no): ").lower()

# 3. Si tiene cupón, pedir el valor y aplicarlo
if tiene_cupon == "si":
    descuento = float(input("Ingrese el valor del cupón de descuento (€): "))
    
    # 4. Verificar si el cupón es válido
    if descuento > 0:
        precio_final = precio - descuento
        print(f"Descuento aplicado de {descuento:.2f}€.")
    else:
        print("El valor del cupón no es válido. No se aplicará descuento.")
        precio_final = precio

# 5. Si no tiene cupón
elif tiene_cupon == "no":
    precio_final = precio

# 6. Si responde algo distinto
else:
    print("Respuesta no válida. No se aplicará descuento.")
    precio_final = precio

# Mostrar el precio final
print(f"El precio final de la compra es: {precio_final:.2f}€")