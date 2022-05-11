"""El proceso de convertir un dato a otro es casting"""
"""Conversion implicita lo realiza python"""
""" Python necesita que el usuario haga algo para convertir un tipo de dato en otro """

"""Implicita"""
num1 = 20
num2 = 30.5
print(type(num1))
print(type(num2))
num1= num1 + num2
print(type(num1))
print(type(num2))

"""Explicita"""
num3 = 5.8
print(num3)
print(type(num3))
num4 = int(num3)
print(num4)
print(type(num4))

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
nueva_edad = 1 + edad
print(nueva_edad)
print(type(nueva_edad))
