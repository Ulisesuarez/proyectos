a=int(input())
b=int(input())
c=int(input())

def maxim(f_a,f_b,f_c):
  
  if f_a>f_b and f_a>f_c:
    return "a es mayor "+str(f_a)
  elif f_b>f_a and f_b>f_c :
    return "b es mayor "+str(f_b)
  elif f_c>f_a and f_c>f_b:
    return "c es mayor" +str(f_c)
  else:
      if f_a==f_b and f_b==f_c:
        return "Son los tres iguales"
      if f_a==f_b: 
        if f_a>f_c:
          return "a y b "+str(f_a)+" y "+str(f_b)+" son iguales y mayores que c "+str(f_c)
        elif f_a<f_c:
          return "a y b "+str(f_a)+" y "+str(f_b)+" son iguales y menores que c "+str(f_c)
      if f_a==f_c:
        if f_a>f_b:
          return "a y c "+str(f_a)+" y "+str(f_c)+" son iguales y mayores que b "+str(f_b)
        elif f_a<f_b:
          return "a y c "+str(f_a)+" y "+str(f_c)+" son iguales y menores que b "+str(f_b)
      if f_b==f_c:
        if f_b>f_a:
          return "b y c "+str(f_b)+" y "+str(f_c)+" son iguales y mayores que a "+str(f_a)
        elif f_b<f_a:
          return "b y c "+str(f_b)+" y "+str(f_c)+" son iguales y menores que a "+str(f_a)