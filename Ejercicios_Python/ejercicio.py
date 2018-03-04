print("introduce dos numeros y te daré la suma de los numeros \
        pares y la de los impares comprendidos entre esos dos numeros")
print("intoduce un valor del rango")
num1=int(input())
print("Ahora el otro")
maximo= int(input())


rango=range(minimo,maximo+1)
print(rango)
pares=0
impares=0
for i in rango:
    
    if i%2==0:
        pares=i+pares
    if i%2!=0:
        impares=i+impares

print("la suma de los pares es "+str(pares)+"y la de los impares "+str(impares))