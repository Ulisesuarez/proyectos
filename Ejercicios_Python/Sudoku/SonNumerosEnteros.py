def sonNumerosEnteros(sudoku):
    
    for fila in sudoku:

        for numero in fila:

            if not isinstance(numero, int):
                return False

    return True