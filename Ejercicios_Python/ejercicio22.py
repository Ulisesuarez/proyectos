print("Introduzca cuántos números tienen que leerse por teclado:")
Positivo=False
while not Positivo:
    veces=int(input())

    if veces<=0:
     print("este no es un numero valido de numeros")
     Positivo=False
    
    else:Positivo=True
    
print("Introduce "+str(veces)+ " numeros enteros positivos")
Done=False
Error=False
while not Done:
        if Error:print ("los numeros tienen que ser positivos")
        lista=[]
        for i in range(0,veces):
            numero =  int(input())
            lista.append(numero)

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
print("El mayor es "+str(listaOrdenada[-1])+" y el menor es "+str(listaOrdenada[0]))