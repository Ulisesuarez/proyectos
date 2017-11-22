def buscandoNemo(matrix,neo):
      
   cicles=0
   while matrix and  cicles<10:
        if len(matrix)%2==0:
           mitad=int(len(matrix)/2)
        else:
            mitad=int(len(matrix)/2)
        
        cicles=cicles+1  
        print("Mitad",mitad)
        print("matrix",matrix)
       
       
        if matrix[mitad][mitad]==neo:
            return[mitad,mitad]

        elif matrix[mitad][mitad]>neo:
            print("nooo",matrix[mitad][mitad])
            matrix=[matrix[i][0:mitad] for i in range(0,mitad)]
        elif matrix[mitad][mitad]<neo:
            print("hola neo")
            matrix=[matrix[i][mitad:] for i in range(mitad,len(matrix))]
   return[mitad,mitad]



""" dic=dict()
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
             
            dic[matrix[i][j]]=[j,i]
    
    return dic[neo]"""





casotest1=[[1,4,7],
            [3,6,9],
            [11,15,17]]
neo1=9

ini=0
fin=100
pas=100
max=10000
c2=[[]]*fin


index=0
while fin<=max:
    row=[]
    
    for i in range(ini,fin):
        row.append(i)
        
    
    
    c2[index]=row
    index=index+1
    ini,fin=fin+1,fin+pas


    
    
    
        
        

print (buscandoNemo(casotest1,neo1))
#print (buscandoNemo(c2,9876))