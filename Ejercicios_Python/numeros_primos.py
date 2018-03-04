def Numeros_primos_hasta(n):
    primos=[]
    
    for numero in range(2,n):
        esPrimo=True
        for primo in primos:
            
            if numero%primo==0:
                esPrimo=False
            
        if esPrimo:
            primos.append(numero)         
    return primos

numerosPrimosMenoresCien = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(Numeros_primos_hasta(9000))
print (numerosPrimosMenoresCien==Numeros_primos_hasta(100))
numerosLimite = [20, 50, 100]