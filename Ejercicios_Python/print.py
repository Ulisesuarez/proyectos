Done=False

while Done==False:
      print("Introduce un numero")
      numero=float(input())
      print("y ahora otro")
      numerodos=float(input())
      if numero>=0 and numerodos>=0:
        print("la suma de los numeros es igual a "+ str(numero+numerodos))
        Done=True
        break
      elif numero>=0 and numerodos<0:
          print ("el segundo numero es negativo, cambialo")
          pass
      elif numero<0 and numerodos>=0:
          print ("el primer numero es negativo, cambialo") 
          pass  
      else:
          print("nooo los dos son negativooos")