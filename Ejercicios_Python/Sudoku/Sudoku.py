# encoding: utf-8

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.
irregular = [[1,2,3],
             [2,3,1]] 
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def esCuadrada(Sudoku):
    assert isinstance(Sudoku,list), "El parametro dado a esCuadrada no es una lista"
    for row in Sudoku:
        		
        if len(row)!=len(Sudoku):
            print("No es cuadrada",len(row),"   ",len(Sudoku))

            return False
    return True

def sonEnteros(Sudoku):
    
    assert isinstance(Sudoku,list), "El parametro dado a sonEnteros no es una lista"
    try:
        for row in Sudoku:
            for i in row:
                if i != int(i):
                    print ("Hay numeros no enteros u otro tipo de dato como ",i)
                    return False
    except ValueError:
        print(i, "no es un numero")
        return False
        
    return True
                


def check_fila(Sudoku):
    assert isinstance(Sudoku,list), "El parametro pasado a check_fila no es una lista"
    for row in Sudoku:
        sortedRow=sorted(row)
        testList=list(range(1,len(row)+1))
        for i in range(0,len(row)):
            if sortedRow[i]!=testList[i]:
                print ("no van del 1 al 9 o se repiten, revisa ", i,"por ejemplo",sortedRow)
                return False
    
    return True

def Check_columna(Sudoku):
    assert isinstance(Sudoku,list), "El parametro dado a check_columna no es una lista"
    
    for row in Sudoku:
        for i in range(0,len(row)):
            for j in range(0,len(Sudoku)):
               
                if j!=Sudoku.index(row) and row[i]==Sudoku[j][i]:
                     print ("el numero ",i,"está repetido en la columna ",j)
                      
                     return False
    print("Buen sudoku máquina!")                
    return True

def check_sudoku(sudoku):
    assert isinstance(sudoku,list), "El parametro dado a check_sudoku no es una lista"
	
    
    		
     
    return esCuadrada(sudoku) and sonEnteros(sudoku) and check_fila(sudoku) and Check_columna(sudoku)

			
			





# Casos test:   
print(check_sudoku(irregular))
    
print (check_sudoku(incorrect))
#>>> False

print (check_sudoku(correct))
#>>> True

print (check_sudoku(incorrect2))
#>>> False

print (check_sudoku(incorrect3))
#>>> False

print (check_sudoku(incorrect4))
#>>> False

print (check_sudoku(incorrect5))
#>>> False

