def alphabet_position(text):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    number=[]
    result=""
    for i in range(1,27):
        number.append(str(i))
    number=number+number
    right=""
    dic=dict(zip(list(alphabet),list(number)))
    for letter in text:
      if letter in alphabet:
        right=right+letter
    print(right)
    for i in range(0,len(right)):
      if i<len(right)-1:
            print (right[i],dic[right[i]])
            result=result+dic[right[i]]+" "
      else:
        result=result+dic[right[i]]
    return result
        
print(alphabet_position("The sunset sets at twelve o' clock."))
      