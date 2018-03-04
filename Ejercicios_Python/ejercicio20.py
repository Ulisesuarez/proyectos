print("introduce 5 numeros enteros positivos")

Done=False
Error=False
while not Done:
        if Error:print ("los numeros tienen que ser positivos")
        
        numero =  int(input())
        numero2 = int(input())
        numero3 = int(input())
        numero4 = int(input())
        numero5 = int(input())


        lista=[numero, numero2,numero3,numero4,numero5]
        Error=False
        for i in lista:
            
            if i>=0 and not Error:
                Done=True
                Error=False
            
            
            else:
                Error=True
                Done=False
                break
                
listaOrdenada=sorted(lista)
print("El mayor es "+str(listaOrdenada[4]))