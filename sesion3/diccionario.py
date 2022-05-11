diccionario = {'c1':'valor1', 'c2':'valor2'}
print(diccionario)
result = diccionario ['c1']
print(result)

cliente = {'nombre': 'juan', 'apellido':'fuentes', 'peso': 55, 'talla': 1.76}
consulta = cliente ['apellido']
print(consulta)

dic = {'c1':55, 'c2': [10,20,30], 'c3': {'s1':100, 's2': 200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

dic2 = {'c1': ['a', 'b', 'c'], 'c2':['d','e', 'f']}
print(dic2['c2'][1].upper())

dic3 = {'c1': 'A', 'c2':'B'}
print(dic3)
dic3['c3'] = 'C'
print(dic3)
dic3['c1'] = 'Z'
print(dic3)