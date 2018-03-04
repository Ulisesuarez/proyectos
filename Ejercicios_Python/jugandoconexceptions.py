sep = '-' * 45 + '\n'

print(sep+'EXCEPTION RAISED AND CAUGHT')
try:
    print("soy antes de fallo")
    x='spam'[1]
    print (x)
    print(x[2])
except IndexError:
    print ("except run")
    
    
finally:
    print ("finally run")
print("after run")

print(sep+'NO EXCEPTION RAISED')
try:
    x="spam"[3]
except IndexError:
    print("except run")
finally:
    print("finally run")
print("after run")

print(sep+'NO EXCEPTION RAISED, WITH ELSE')
try:
    x=1/0
    print("run try")
except (IndexError, ZeroDivisionError):
    
    
    print("except run")
else:
    print("else run")
finally:
    print("finally run")
print("after run")