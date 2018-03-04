print('Introduce un numero decimal')

Done=False
while not Done:
    dato=(input())
    numero=str(dato)

    print(numero)
    punto="."
    fristdecimal=numero.find(punto,0)+1
    print(fristdecimal)
    if fristdecimal==0:
        Done=False
        print ("introduce un numero decimal porfavor, utilizando el punto")
    else:
        Done=True
parteentera=numero[:fristdecimal-1]

print(parteentera)

print(fristdecimal)
if int(numero[fristdecimal]) >= 5:
  print(int(parteentera)+1)

elif int(numero[fristdecimal]) < 5:
  print (int(parteentera))