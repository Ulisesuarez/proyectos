import checkColumnas
import checkFilas
import checkNumerosValidos
import casosTest
import esCuadrado


def check_sudoku(sudoku):
    
    return esCuadrado.esCuadrado(sudoku) and checkNumerosValidos.checkNumerosValidos(sudoku) \
            and checkFilas.checkFilas(sudoku) and checkColumnas.checkColumnas(sudoku)


casosTest.tester(True,check_sudoku,"correcto")