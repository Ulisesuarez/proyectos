import numerosEnRango
import SonNumerosEnteros
import casosTest

def checkNumerosValidos(sudoku):
    
    # precondiciones

    return SonNumerosEnteros.sonNumerosEnteros(sudoku) and numerosEnRango.numerosEnRango(sudoku)

if __name__ == "__main__":
    casosTest.tester(True,checkNumerosValidos,"correcto")
    casosTest.tester(True,checkNumerosValidos,"incorrecto")
    casosTest.tester(True,checkNumerosValidos,"incorrecto1")
    casosTest.tester(True,checkNumerosValidos,"incorrecto2")

"""correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto = [[1, 2, 3],
              [2, 3, 1],
              [2, 3, 1]]

incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]

incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]

incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]

incorrecto5 = [[1, 1.5],
               [1.5, 1]]

incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]"""