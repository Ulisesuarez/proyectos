def esCuadrado(sudoku):
    
    numeroFilas = len(sudoku)

    for fila in sudoku:

        if len(fila) != numeroFilas:
            return False

    return True