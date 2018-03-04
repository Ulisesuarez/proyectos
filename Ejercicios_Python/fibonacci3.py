def fib(n):
    #fiboDics = {0: 0, 1: 1}
    fiboDics=[0,1,1]
    def fiboMemoization(n):
        nonlocal fiboDics
        #print(n,fiboDics)
        #if n in fiboDics:
        if n<len(fiboDics):
            
            return fiboDics[n]
        else:
            #fiboDics[n] = fiboMemoization(n - 1) + fiboMemoization(n - 2)
            fiboDics.append((fiboMemoization(n - 1) + fiboMemoization(n - 2)))
            
            return fiboDics[n]

    return fiboMemoization(n)

fiboNumbers = [0, 1, 1, 2, 3,5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

for num in range(0, len(fiboNumbers)):
    
    print(fib(num) == fiboNumbers[num])

print(fib(100) == 354224848179261915075)
print(fib(251) == 12776523572924732586037033894655031898659556447352249)

print(fib(900))