def numerosEnRango(sudoku):
    
    numerosValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:

        for numero in fila:

            if numero not in numerosValidos:
                return False

    return True