import numpy as np
import itertools

def letter_finder(board,word,i1,i2):
   npboard=np.array(board)
   #print("Holaa letter",npboard)
   search=board[i1][i2]
   instances=[]
   for row in range(0,len(board)):
      #print ("board row search",board[row],search)
      ij=np.where(npboard[row] == search)[0]
      #print("row,ij!!!!",row,ij)
      if list(ij)!=list([]):
        #print("quee")
        for p in ij:
            instances.append([row,p])
   return instances

def instances_of_all_letters(board,word):
    dic={}
    #print("instances")
    for row in range(0,len(board)):
        for letter in range(0,len(board[row])):
            dic[board[row][letter]]=letter_finder(board,word,row,letter)
    return dic
#crear indice de por donde vamos de word y un metodo iguala  first pero para cualquier letra

def all_letters_in(board, word,dic):
    
    for letter in word:
        if letter not in dic:
            return False
        
    return True

def posible_positions_letter(board,word,dic):
    positions=[]
    for letter in word:
        positions.append(dic[letter])
    return positions

def posible_ways(positions):
    ways=[]
    #positions=posible_positions_letter(board,word,dic)
    for x in itertools.product(*positions):
        
        ways.append(x)
    return ways
            

        
def find_word(board, word):
    dic=instances_of_all_letters(board,word)
    #print("dic",dic)
    #index=0

    if all_letters_in(board,word,dic):
        if len(word)==1:
            return True
        positions=posible_positions_letter(board,word,dic)
        #print ("positions",positions)
        ways=posible_ways(positions)
        #print("HOLAAAA WAYS",ways)
        for index in range(0,len(positions[0])):
            
            first=positions[0][index]
            
            for way in ways:
                forbidden=[]
                forbidden.append(first)
                for w in range(1,len(way)):
                    if (way[w][0]==way[w-1][0] or way[w][0]==way[w-1][0]+1 or way[w][0]==way[w-1][0]-1) and  (way[w][1]==way[w-1][1] or way[w][1]==way[w-1][1]+1 or way[w][1]==way[w-1][1]-1) and way[w] not in forbidden:
                        forbidden.append(way[w])
                    if len(forbidden)==len(word):
                        return True

        
    return False
                 

testBoard = [
  ["E","A","R","A"],
  ["N","L","E","C"],
  ["I","A","I","S"],
  ["B","Y","O","R"]
]

print(find_word( testBoard, "C" ) == True )
print(find_word( testBoard, "EAR" ) == True )
print(find_word( testBoard, "EARS" ) == False )
print(find_word( testBoard, "BAILER" ) == True )
print(find_word( testBoard, "RSCAREIOYBAILNEA" ) == True)
print(find_word( testBoard, "CEREAL" ) == False)
print(find_word( testBoard, "ROBES" ) == False)
""""bol=np.array([ ["I","L","A","W"],
               ["B","N","G","E"],
               ["I","U","A","O"],
               ["A","S","R","L"] ])
wor="NARUBI"

print(find_word(bol,wor))
 """


"""for index in range(0,len(positions[0])):
            forbidden=[]
            first=positions[0][index]
            forbidden.append(first)
            #while len(forbidden)!=len(word):
            #print("reiniciando forbidden",forbidden)
            for iletter in range(1,len(positions)):
                posibles=[]
               
                for pos in range(0,len(positions[iletter])):
                    #print("se compara pos ",positions[iletter][pos],"iletter vale ",iletter,"con forbiden ",forbidden[-1])
                    if ((forbidden[-1][0]== positions[iletter][pos][0]) or (positions[iletter][pos][0]== forbidden[-1][0]+1) or (positions[iletter][pos][0]== forbidden[-1][0]-1)) and ((positions[iletter][pos][1]==forbidden[-1][1]) or (positions[iletter][pos][1]== forbidden[-1][1]+1) or (positions[iletter][pos][1]== forbidden[-1][1]-1)) and (positions[iletter][pos] not in forbidden):
                        posibles.append(positions[iletter][pos])
                        #print ("posibles",posibles)
                        #print("posicion que cumple",positions[iletter][pos])
                if  len(posibles)==1:   
                        forbidden.append(positions[iletter][pos])
                        #print("como va el forbiden",forbidden)
                else:
                    if len(posibles)==0:
                        pass
                    else:
                        
                            if iletter<(len(positions)-1):
                                postpos=len(positions[iletter+1])
                                for ps in range(0,postpos):
                                    #print("hola",positions[iletter+1][ps])
                                    for tr in posibles:
                                        #print (tr[0],tr[1],iletter)
                                        if (((forbidden[-1][0] == tr[0] or (tr[0]== forbidden[-1][0]+1) or (tr[0]== forbidden[-1][0]-1)) and (tr[1]==forbidden[-1][1]) or (tr[1]== forbidden[-1][1]+1) or (tr[1]== forbidden[-1][1]-1)) and tr not in forbidden) and (((positions[iletter+1][ps][0] == tr[0] or (tr[0]== positions[iletter+1][ps][0]+1) or (tr[0]== positions[iletter+1][ps][0]-1)) and (tr[1]==positions[iletter+1][ps][1]) or (tr[1]== positions[iletter+1][ps][1]+1) or (tr[1]== positions[iletter+1][ps][1]-1)))  :
                                             forbidden.append(tr)
                            
                if len(forbidden)==len(word):
                        return True"""