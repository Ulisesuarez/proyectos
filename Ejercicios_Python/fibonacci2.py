
fibList = [0,1,1]
def fibonacci(n):
    global fibList
    for i in range(len(fibList),n+1):
            
            fibList.append(fibList[i-1]+fibList[i-2])
    return fibList


print(fibonacci(50))
print(fibonacci(0))
print(fibonacci(322))
print(fibList[-1]==8801063578447437644962364569698707634360652047981718378070013667111 )
            
"""
#fibonacci(322221)

m = {0: 1, 1: 1}
def fib(n):
    #assert n >= 0
    if n not in m:
        m[n] = fib(n-1) + fib(n-2)
    print(m[n])
    return m[n]
    
fib(25)

"""
"""
0 0
1 0 1 
2 0 1 1
3 0 1 1 2
4 0 1 1 2 3
5 0 1 1 2 3 5

n = 10 -> 55
n = 25 -> 75025
n = 322 -> 8801063578447437644962364569698707634360652047981718378070013667111 

"""
