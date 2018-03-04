def factorial(numer):
    fact=1
    while numer >0:
        
      fact=numer*fact

      numer=numer-1
    
    return fact
print (factorial(int(input())))
