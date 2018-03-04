def move_zeros(array):
     

  zeros=[]
  result=[]
  print("queesesto",array)
  
  
  
  for el in range(0,len(array)):
      if array[el] is 0:
            print (array[el],"este es 0")
            zeros.append(array[el])
                    
      else:
        if   isinstance(array[el],float) and int(array[el])==0:
              print(array[el])
              zeros.append(0)
        else:
                           
            print (array[el],"esto no es 0")
            result.append(array[el])
            print (result)
        
        
      
       
       

  return result+zeros

    

print(move_zeros(['a',0,False,0.0, 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

#'a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] should equal 
# ['a', 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
