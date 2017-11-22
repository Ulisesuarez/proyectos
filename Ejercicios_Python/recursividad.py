
sumPowerlist=[]
pattern_arr=[]
h=0
last_term=0
patt_len=0
First=True
ciclos=0
Finished=False

def sum_pow_dig_seq(start, n, k):

  global patt_len,last_term,h,sumPowerlist,pattern_arr,First,ciclos,Finished
 
  if First:
       ciclos=k
       First=False
  numberString=str(start)
  sumPower=0
  testigo=True
  cyc_patt_arr=pattern_arr
  
  
  for digit in numberString:
      sumPower=sumPower+int(digit)**n
  sumPowerlist.append(sumPower)
  #print(sumPowerlist)
  for number in sumPowerlist:
      #print(pattern_arr,k)
      if sumPowerlist.count(number)>1 and testigo:
          testigo=False
          h=sumPowerlist.index(number)
      if number in pattern_arr :
          pattern_arr=sumPowerlist[h:-1]
          #print("hola",number,pattern_arr)
          k=1
      if sumPowerlist.count(number)>1 and number not in pattern_arr:
              pattern_arr.append(number)
      

  if k==1:
      cyc_patt_arr=list(pattern_arr)
      patt_len=len(cyc_patt_arr) 
      index=ciclos-h-1
      #print(index)
      while index>0:
          print(index-patt_len)
          index=index-patt_len
      
      
      print(ciclos,h,len(cyc_patt_arr))
      print(index,cyc_patt_arr)
      last_term=cyc_patt_arr[index]
      
      
      
      h=h+1
      Finished=True
      return [h, cyc_patt_arr, patt_len, last_term] 
  else:
      
      sum_pow_dig_seq(sumPower,n,k-1)
  #print(k,"reciclo",cyc_patt_arr,pattern_arr)
  cyc_patt_arr=list(pattern_arr)
  if k==ciclos:
    print(Finished)  
    sumPowerlist=[]
    pattern_arr=[]
    First=True
    Finished=False
  return [h, cyc_patt_arr, patt_len, last_term]


print(sum_pow_dig_seq(420, 4, 30)==
[12, [13139, 6725, 4338, 4514, 1138, 4179, 9219], 7, 1138])

print(sum_pow_dig_seq(420, 5, 100)==
[23, [9045, 63198, 99837, 167916, 91410, 60075, 27708, 66414, 
17601, 24585, 40074, 18855, 71787, 83190, 92061, 66858, 84213, 
34068, 41811, 33795, 79467, 101463], 22, 18855])