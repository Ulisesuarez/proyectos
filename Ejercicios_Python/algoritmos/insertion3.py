import matplotlib.pyplot as plt
import random
import time


def createRandomList(length):
    assert isinstance(length,int)
    listaRandom=list(range(length))
    random.shuffle(listaRandom)
    assert len(listaRandom)==length
    
    return listaRandom
    # recibe como parametro la longitud de la lista
    # crea una lista de numero enteros
    # la "mezcla" = desordena
    # devuelve la lista


def display(lista):
    plt.clf()
    plt.bar(range(len(lista)), lista)
    plt.draw()


def less(a, b):
    #assert isinstance(a,int) and isinstance(b,int) or isinstance(a,str) and isinstance(b,str)
    return a<b
     
    # comprueba si a es menor que b
    # devuelve un boolean
    # recibe dos elementos
    # ojo a si el algoritmo de ordenacion es estable o inestable


def exchange(lista, i, j):
    
    lista[i], lista[j]=lista[j], lista[i]
    
    assert isExchanged(lista, i, j)
    # intercambia dos elementos de posicion en la lista
    # recibe la lista, la posicion i y la posicion j
    # devuelve None
    # comprueba que se han intercambiado los elementos


def isExchanged(lista, i, j):
    
    return lista[i]>lista[j]
    
    # comprueba si el elemento en la posicion i
    # es menor que el elemento en la posicion j
    # devuelve un boolean


def isSorted(lista):
    """ for index in range(len(lista[:-1]):
        if lista[index]<lista[index+1]:
            return False"""
    for(offset,element) in enumerate(lista[:-1]):
        if element >lista[offset+1]:
            print (str(element)+str(lista[offset+1]),element <lista[offset+1] )
            return False
    return True
    # comprueba si la lista esta oredenada
    # devuelve un boolean


def insertionSort(lista):
    
    pos=1
    while pos<len(lista):
        i=pos
        isTheEnd=False

        while i>0 and not isTheEnd:
            if less(lista[i],lista[i-1]):
                exchange(lista, i, i-1)
                i-=1
            else:
                
                isTheEnd=True
        pos+=1         
    print(time.clock())
    assert pos== len(lista)
    assert isSorted(lista)
    return lista
        
                    
                
                
    # ordena la lista segun el algoritmo de ordenacion
    # bubble sort
    # cada vez que se intercambian dos elementos se dibuja la lista:
    # llama a display(lista)
    # devuelve None
    # Comprueba que la lista esta ordenada


if __name__ == "__main__":

    plt.ion()
    listatest = createRandomList(15)
    print(listatest)
    print(insertionSort(listatest))
    print(isSorted(listatest))
    plt.show(block=True)

    # Listas de strings como casos test #
    # desactivar display() en bubbleSort()

    for test in open("stringTestCases.txt", 'r'):
        testList = list(test.replace(' ', ''))
        insertionSort(testList)
        assert isSorted(testList), "Test %s " % (str(test))

    print("string test cases passed")
