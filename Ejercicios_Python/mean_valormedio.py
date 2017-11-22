a=int(input())
b=int(input())
c=int(input())

def mean(f_a,f_b,f_c):
    lista=[f_a,f_b,f_c]
    nummax=max(lista)
    numin=min(lista)

    for i in lista:
      if i==nummax and len(lista)>0:
          lista.remove(i)
      if i==numin and len (lista)>0:
          lista.remove(i)
    return lista


print(mean(a, b, c))
