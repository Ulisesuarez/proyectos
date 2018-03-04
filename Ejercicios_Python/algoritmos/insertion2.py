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
    print(lista)
    #print (i, j, lista)
    #lista[i], lista[j]=lista[j], lista[i]
    sublist=list(lista[j:])
    if lista[i] in sublist:
            sublist.remove(lista[i])
    #print("lista[:j]"+str(lista[:j]),"Lista[i]"+str(lista[i]),"sublist"+str(sublist),)
   
    lista=list(lista[:j]+[lista[i]]+sublist)
    assert isExchanged(lista, i, j)
    return lista
    # intercambia dos elementos de posicion en la lista
    # recibe la lista, la posicion i y la posicion j
    # devuelve None
    # comprueba que se han intercambiado los elementos


def isExchanged(lista, i, j):
    print (lista)
    #print(lista[i]<lista[j],lista[i],lista[j], j,i)
    return lista[j]<lista[i]
    
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
    print(time.clock())
    swaped=True
    
    while swaped:
        swaped=False
        for indice in range(1,len(lista)):
            j=indice-1
            while less(lista[indice],lista[j]) and j>=0:
                
                
               j-=1 
            if less(lista[indice],lista[j+1]):
                    lista=exchange(lista,indice,j+1)
                    #display(lista)
                    #print(lista)
                    swaped=True
                
        
                
    print(time.clock())
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
    listatest=insertionSort(listatest)
    print(listatest)
    print(isSorted(listatest))
    plt.show(block=True)

    # Listas de strings como casos test #
    # desactivar display() en bubbleSort()

    for test in open("stringTestCases.txt", 'r'):
        testList = list(test.replace(' ', ''))
        testList=insertionSort(testList)
        assert isSorted(testList), "Test %s " % (str(test))

    print("string test cases passed")
