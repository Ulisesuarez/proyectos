fiboMemoDict={'actual':1,'n1':1,'n2':0}
def fibonacci(n):
    fibList = []
    
    if n == 0:
        fibList.append(n)
        return fibList
    
    else:
        index = int(n)
        while index != 1:
            fiboMemoDict['actual'] = fiboMemoDict['n1'] + fiboMemoDict['n2']
            fiboMemoDict['n2'] = fiboMemoDict['n1']
            fiboMemoDict['n1'] = fiboMemoDict['actual']
            index -= 1
        print (fiboMemoDict['actual'])
    return fiboMemoDict['actual']

#fibonacci(322221)

m = {0: 1, 1: 1}
def fib(n):
    #assert n >= 0
    if n not in m:
        m[n] = fib(n-1) + fib(n-2)
    print(m[n-2])
    return m[n]
    
fib(25)

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