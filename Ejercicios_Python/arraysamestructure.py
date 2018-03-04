encode=
def same_structure_as(original,other):
    stra1=str(original)
    stra2=str(other)
    
    stra1=stra1.translate(str.maketrans("","","'' ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890"))
    stra2=stra2.translate(str.maketrans("","","'' ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890"))
    if stra1==stra2:
       return True
    else:
        return False

print(same_structure_as([],[]))