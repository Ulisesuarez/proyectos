def custom_sort(lst):
    dic={}
    nuevaLista=sorted(lst,key=len)[::-1]
    charnow=nuevaLista[0][0]
    result=[]
    elementIndex=0
    while elementIndex<len(nuevaLista):
        if ord(charnow) not in dic.keys():
            dic[ord(charnow)]=[]
        if nuevaLista[elementIndex][0]==charnow:
            dic[ord(charnow)].append(nuevaLista[elementIndex])
            elementIndex=elementIndex+1
        else:
            charnow=nuevaLista[elementIndex][0]
    print(dic)
    dic2={}
    dic3={}
    for char, lis in dic.items(): #recorre el diccionario, lis es cada lista de elementos que empiezan por char, char= A lis[A1,A2,A]
        for item in lis: #item es cada uno de los elementos de lis ej. A1
            valorList=[]
            for letra in item: #letra es cada uno d elos caracteres de A1 ej. A y 1
                valor=ord(letra)
                valorList.append(valor)
            dic2[item]=valorList
            print(char,item,dic[char])
            print(dic[char].index(item),dic[char][dic[char].index(item)])
            print(int("".join(str(x) for x in dic2[item])))
            #dic[char][dic[char].index(item)]=[dic[char][dic[char].index(item)],dic2[item]]
            dic[char][dic[char].index(item)]=[dic[char][dic[char].index(item)],int("".join(str(x) for x in dic2[item]))]#join(str(x) for x in list_of_ints
    print (dic)
    
    primerOrden=sorted(dic.keys())
    print(primerOrden)
   
        
    #while len(result)==len(lst):
    for firstchar, listelements in dic.items():
           dic[firstchar]=sorted(listelements, key=lambda x: x[1])
           for el in listelements:
               dic[firstchar][listelements.index(el)]=dic[firstchar][listelements.index(el)][0]
    
    print("hola",dic)
    for index in primerOrden:
            result=result+dic[index]
    print(result)
    return result    
    print(dic)
    lengthnow=len(nuevaLista[0])
    for element in nuevaLista:
        
        for char in element:
            
            pass
    print(ord("~"))
    print(nuevaLista)
    return nuevaLista





assert custom_sort(['A', 'A2']) == ['A2', 'A'],"no pasa el primer caso test"
assert custom_sort(['B3', 'A2', 'B2', 'B', 'A1', 'A']) == ['A1', 'A2', 'A', 'B2', 'B3', 'B']
tests = [
[['A', 'A2'], ['A2', 'A']],
[['B3', 'A2', 'B2', 'B', 'A1', 'A'],['A1', 'A2', 'A', 'B2', 'B3', 'B']],
[['3', '@', '@2', 'a', 'aa'], ['3', '@2', '@', 'aa', 'a']],
[['~', '~~~', '~~', 'Z', 'ZZ','z'], ['ZZ', 'Z', 'z', '~~~', '~~', '~']]]

