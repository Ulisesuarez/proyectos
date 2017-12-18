import matplotlib.pyplot as plt
import random
import time


def createGapList(length):
    gapList=[]
    f,g={},{}
    nlength=int(length/5)
    for i in range(0,nlength):
        f[i]=9*(4**i)-9*(2**i)+1
        g[i]=2**(i+2)*(2**(i+2)-3)+1
    print (f,g) 
    for i in f.keys():
        if f[i]<length:
            gapList.append(f[i])
        if g[i]<length:
            gapList.append(g[i])
    return gapList[::-1]

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
    
    #print ("lista antes del cambio", "i="+str(i), "j="+str(j),"lista[i]="+str(lista[i]),"lista[j]="+str(lista[j]), lista,"\n")
    #print(lista)
    lista[i], lista[j]=lista[j], lista[i]
    #print(lista)
    #print ("lista despues del cambio", "i="+str(i), "j="+str(j),"lista[i]="+str(lista[i]),"lista[j]="+str(lista[j]), lista,"\n")
    assert isExchanged(lista, i, j)
    return lista
    # intercambia dos elementos de posicion en la lista
    # recibe la lista, la posicion i y la posicion j
    # devuelve None
    # comprueba que se han intercambiado los elementos


def isExchanged(lista, i, j):
    #print("i="+str(i),"j="+str(j), "lista[i]="+str(lista[i]),"lista[j]="+str(lista[j])," lista[i]<lista[j]="+str(lista[i]<lista[j]) )
    
    return lista[i]<lista[j]
    
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


def shellSort(lista):
    swaped=True
    gapList=createGapList(len(lista))
    print(gapList)
    while swaped:
        swaped=False
        for gap in gapList:
            #print(gap)
            for indice in range(len(lista)):
                
                if indice+gap<len(lista) and less(lista[indice+gap],lista[indice]):
                    #print(indice,lista[indice],indice+gap,lista[indice+gap])
                    exchange(lista,indice,indice+gap)
                    #display(lista)
                    
                    swaped=True
                    if indice-gap>=0 and less(lista[indice],lista[indice-gap]):
                        #print("-gap",indice,lista[indice],indice-gap,lista[indice-gap])
                        exchange(lista,indice-gap,indice)
                        #display(lista)
                        





       
                
        
                
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
    print(shellSort(listatest))
    print(isSorted(listatest))
    plt.show(block=True)

    # Listas de strings como casos test #
    # desactivar display() en bubbleSort()

    for test in open("stringTestCases.txt", 'r'):
        testList = list(test.replace(' ', ''))
        shellSort(testList)
        assert isSorted(testList), "Test %s " % (str(test))

    print("string test cases passed")
