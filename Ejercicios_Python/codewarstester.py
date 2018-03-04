def queue_time(customers, n):
    till=[]
    copy=list(customers)
    revers=[]
    while copy:
        l=copy.pop()
        revers.append(l)
    Time=0
    print ("como queda revers",revers)
    for tills in range(0,n):
        till.append(0)
    
    i=0
    
    while till[-1]==0 and revers:
        till[i]=revers.pop()
        i=i+1
    print("esto es la primera asignacion de till",till)
    for i in range(0,len(till)):
        if till[i]==[]:
            
            till[i]=[0]
        
        count=0
    while sum(till)!=0 and count<10000:
        print("lo que queda en revers",revers)
        for j in range(0,len(till)):
            print ("siguiendo el rastro de till ",till)
            print("esto es la j de ahora ",till[j])
            
            minnoncero=[]
            for k in till:
                if k!=0:
                    minnoncero.append(k)
            
            if minnoncero!=[]:        
                print("esto es el minimo ",min(minnoncero))
                Time=min(minnoncero)+Time
                print("esto es el total",Time)
                for m in range(0,len(till)):
                    if till[m]!=0:
                        till[m]=till[m]-min(minnoncero)
                print ("despues de la resta",till)
                if  revers:
                    tilempt=0
                    for d in range(0,len(till)):
                        if till[d]==0:
                            tilempt=tilempt+1

                    while revers and tilempt>0:
                        for d in range(0,len(till)):
                          if till[d]==0 and revers:
                            till[d]=revers.pop()
                            tilempt=tilempt-1               
                        
                    
                else:
                    if sum(till)!=0:
                        pass
                    else:
                        count=10000000
                    
    return Time

#print(queue_time([],1))
"""print(queue_time([], 1), 0)
print(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
print(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
print(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
print(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
print(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")


print(queue_time([15,3,5,10],3))"""
print(queue_time([31, 29, 2, 46, 20, 5, 31, 49, 42, 16, 44, 49, 48, 22],3),149)