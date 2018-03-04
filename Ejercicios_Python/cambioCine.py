def tickets(people):
    change={"100":0,"50":0,"25":0}
    price=25
    if people==[]:
        return "YES"
    if people[0]!=price:
        return "NO"
    else: 
        if len(people)==1:
            return "YES"
        else:
            change["25"]=1
    for i in range(1,len(people)):
                  
        if people[i]!=price:
            
            if people[i]==100:
                if change["25"]>=1 and change["50"]>=1:
                    change["100"]=change["100"]+1
                    change["50"]=change["50"]-1
                    change["25"]=change["25"]-1
                        
                elif change["25"]>3:
                    change["100"]=change["100"]+1
                    change["25"]=change["25"]-3
                else:
                    return "NO"
                
            elif people[i]==50:
                if change["25"]<1:
                    return "NO"
                else:
                    change["50"]=change["50"]+1
                    change["25"]=change["25"]-1
        else:
            change["25"]=change["25"]+1 
    return "YES"
                