def format_duration(seconds):
    if seconds==0:
        return "now"
    
    timesPrinter=[["year","years"],["day","days"],["hour","hours"],["minute","minutes"],["second","seconds"]] 
        
    secondsInYear=365*24*60*60
    secondsInDay=24*60*60
    secondsInHour=60*60
    secondsInMinute=60
    times=[secondsInYear,secondsInDay,secondsInHour,secondsInMinute,1]
    result=[0,0,0,0,0]
    Text_result=""
    rest=seconds
    for t in range(0,len(times)):
        result[t]=int(rest/times[t])
        rest=seconds%times[t]

    contzero=0
    nonzero=0
    for i in range (0,len(result)):
        
        if result[i]==0:
            contzero=contzero+1
        else:
            nonzero=nonzero+1
    first=True
    for i in range (0,len(result)):        
        if contzero==4 and result[i]>0:
            if result[i]>1:
                Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][1]
            else:
                Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][0]
            
        elif contzero==3 and result[i]>0:
             
             print (first)
             if result[i]>1 and first:
                    Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][1]+ " and "
                    first=False
             elif result[i]>1 and not first :
                Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][1]
             
             elif result[i]==1 and first:
                    Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][0]+ " and "
                    first=False
             elif result[i]==1 and not first :
                Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][0]
        elif contzero<3 and result[i]>0:
             nonzero=nonzero-1
             
             if result[i]>1 and nonzero>1 :
                    Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][1]+ ", "
                    
             elif result[i]>1 and nonzero==1 :
                Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][1]+ " and "
             
             elif result[i]>1 and nonzero==0 :
                    Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][1]
            
             elif result[i]==1 and nonzero>1 :
                    Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][0]+ ", "
                    
             elif result[i]==1 and nonzero==1 :
                Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][0]+ " and "
             
             elif result[i]==1 and nonzero==0 :
                    Text_result=Text_result+ str(result[i])+" "+timesPrinter[i][0]
             
           

            
            
    
    return Text_result 

print(format_duration(62))
                  
    