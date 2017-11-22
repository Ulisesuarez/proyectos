def ultimas_tiradas(frames):
	score=0
	turno=frames
	print ("len",len(turno))
	for i in range(0,len(turno)):
		if len(turno[i])==3:
			if  turno[i].find("/")==1:
				turno[i]=turno[i][2]
				print (i,turno[i])
				score=score+10
				print (score)
			elif turno[i].find("/")==2:
				turno[i]=turno[i][0]
				score=score+10
			for el in turno[i]:
				if el=='X':
					score=score+10
				else:
					print(el)
					score=score+int(el)
					print(score)
		if len(turno[i])==2 and i==len(turno)-1:
				print("hola3",turno[i][0],turno[i][1],"i",i)
				score=score+int(turno[i][0])+int(turno[i][1])
    			
	return score

def bowling_score(frames):
    dict={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"X":10,"/":10}
    score=0
    turno=frames.split()
    stringframes="".join(turno)
    print(stringframes, len(stringframes))
    for j in range(0,len(stringframes)):
        if stringframes[j]=='X' and j<len(stringframes)-2 and len(turno[-1])==2:
            score=score+dict[stringframes[j]]+dict[stringframes[j+1]]+dict[stringframes[j+2]]
            if stringframes[j+2]=='/':
              score=score-dict[stringframes[j+1]]
            print("strike",score)
        elif stringframes[j]=='X' and j<len(stringframes)-3 and len(turno[-1])==3:
            score=score+dict[stringframes[j]]+dict[stringframes[j+1]]+dict[stringframes[j+2]]
            if stringframes[j+2]=='/':
              score=score-dict[stringframes[j+1]]
            print("strike2",score)
        elif stringframes[j]=='/' and j<len(stringframes)-2 and len(turno[-1])==2:
            score=score+dict[stringframes[j]]-dict[stringframes[j-1]]+dict[stringframes[j+1]]
            print("spare",score)
        elif stringframes[j]=='/' and j<len(stringframes)-3 and len(turno[-1])==3:
            score=score+dict[stringframes[j]]+dict[stringframes[j+1]]-dict[stringframes[j-1]]
            print("spare2",score)
        elif  j<len(stringframes)-2 and len(turno[-1])==2:
            score=score+dict[stringframes[j]]
            print("hola",j, dict[stringframes[j]], score)
        elif j<len(stringframes)-3 and len(turno[-1])==3:
            score=score+dict[stringframes[j]]
            print("hola2",j, dict[stringframes[j]], score)
            
    
    
    score=score+ultimas_tiradas(turno)
    return score

print(bowling_score("5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 8/8"))