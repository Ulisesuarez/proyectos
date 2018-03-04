
""" Kata nivel 8 , utilizado para practicar los estandares de escritura de Python3,
    calcula los múltiplos de un número en un rango dado y los devuelve como una lista.
"""
def count_by(multiplo=0, rango=1):
    """ Calcula los múltiplos del número (multiplo->int o float) en el rango (1,rango->int),
     devuelve una lista. Si no hay rango devuelve una lista con el valor del múltiplo como
     único elemento.
      """
    try:
        if (not isinstance(multiplo, int) and not isinstance(multiplo, float)) or \
        not isinstance(rango, int):
            raise TypeError
        lista_de_multiplos = []
        if rango > 0:    #si el rango es positivo devolvemos los múltiples del 1 hasta el numero indicado
            for numero in range(1, rango+1):
                lista_de_multiplos.append(numero*multiplo)
        else: #si el rango es positivo devolvemos los múltiples del numero indicado hasta 1
            for numero in range(rango, 0):
                lista_de_multiplos.append(numero*multiplo)
        return lista_de_multiplos
    except TypeError:
        print("TypeError")
        if not isinstance(multiplo, int) and not isinstance(multiplo, float):
            print("El tipo del primer argumento, 'multiplo', con valor '" +str(multiplo)\
                  +"' y tipo"+str(type(multiplo))[6:-1]+", debe ser int o float.")
        if not isinstance(rango, int):
            print("El tipo del segundo argumento, 'rango', con valor '"+str(rango)\
                  +"' y tipo"+str(type(rango))[6:-1]+", debe ser int")

#Casos Test

assert count_by() == [0], "count_by() "+str(count_by())
assert count_by(1) == [1], "count_by() "+str(count_by(1))
assert count_by(0, 5) == [0, 0, 0, 0, 0], "count_by(0,5) "+str(count_by(0, 5))
assert count_by(2, -4) == [-8, -6, -4, -2], "count_by(2, -4) "+str(count_by(2, -4))
assert count_by(1.5, 5) == [1.5, 3, 4.5, 6, 7.5], "count_by('a', 5) "+str(count_by("a", 5))
assert count_by(2, 5) == [2, 4, 6, 8, 10], "count_by(2, 5) "+str(count_by(2, 5))
assert count_by(3, 5) == [3, 6, 9, 12, 15], "count_by(3, 5) "+str(count_by(3, 5))
assert count_by(50, 5) == [50, 100, 150, 200, 250], "count_by(50, 5) "+str(count_by(50, 5))
assert count_by(100, 5) == [100, 200, 300, 400, 500], "count_by(100, 5) "+str(count_by(100, 5))
assert count_by(1.5, "a") is None, "count_by('a', 5) "+str(count_by(1.5, "a"))
assert count_by("a", 5) is None, "count_by('a', 5) "+str(count_by("a", 5))
assert count_by(None, [1, 2, 3, 4, 5]) is None, "count_by('a', 5) "+str(count_by(None, [1, 2, 3, 4, 5]))
