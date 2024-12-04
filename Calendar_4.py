def diagonal_to_string(matrix):
    max_y = len(matrix)     # Alto de la matriz (filas)
    max_x = len(matrix[0])  # Ancho de la matriz (columnas)
    diagonals = []

    # Diagonales hacia abajo y derecha
    # Desde la primera fila
    for start_x in range(max_x):  # Comenzamos desde cada columna de la primera fila
        texto = ''
        x = start_x
        y = 0
        while x < max_x and y < max_y:
            texto += str(matrix[y][x])
            x += 1
            y += 1
        diagonals.append(texto)

    # Desde la primera columna (excepto el primer elemento, que ya está cubierto)
    for start_y in range(1, max_y):  # Comenzamos desde cada fila de la primera columna
        texto = ''
        x = 0
        y = start_y
        while x < max_x and y < max_y:
            texto += str(matrix[y][x])
            x += 1
            y += 1
        diagonals.append(texto)

    # Diagonales hacia abajo y izquierda 
    # Desde la última fila
    for start_x in range(max_x - 1, -1, -1):  #los dos primeros -1 ajustan del valor de columnas al indice, con el tercer -1 indico que quiero decrecer 
        texto = ''
        x = start_x
        y = 0
        while x >= 0 and y < max_y:
            texto += str(matrix[y][x])
            x -= 1
            y += 1
        diagonals.append(texto)

    # Desde la última columna (excepto el primer elemento que ya está cubierto)
    for start_y in range(1, max_y):  # Comenzamos desde cada fila de la última columna
        texto = ''
        x = max_x - 1
        y = start_y
        while x >= 0 and y < max_y:
            texto += str(matrix[y][x])
            x -= 1
            y += 1
        diagonals.append(texto)

    return diagonals

def columnas_to_string(matrix):
    # Obtener el número de filas y columnas
    max_y = len(matrix)     # Alto de la matriz (filas)
    max_x = len(matrix[0])  # Ancho de la matriz (columnas)
    
    # Lista para almacenar las columnas como cadenas
    columnas = []
    
    # Recorrer cada columna y generar la cadena correspondiente
    for col in range(max_x):
        columna = ''
        for row in range(max_y):
            columna += str(matrix[row][col])  # Concatenar el elemento de la fila actual
        columnas.append(columna)
    
    return columnas

def oh_wow_its_afucking_x_mas(matrix):
    max_y = len(matrix) - 1    # Alto de la matriz (filas)
    max_x = len(matrix[0]) - 1 # Ancho de la matriz (columnas)
    oh_wow_a_fucking_xmas_lol = 0

    for y in range(max_y):
        for x in range(max_x):
           if (x+2) <= max_x and (y+2) <= max_y:
                if matrix[y][x] == 'M'  and matrix[y][x+2] == 'S' and matrix[y+1][x+1] == 'A' and matrix[y+2][x] == 'M' and matrix[y+2][x+2] == 'S':
                    oh_wow_a_fucking_xmas_lol += 1
                elif matrix[y][x] == 'S'  and matrix[y][x+2] == 'S' and matrix[y+1][x+1] == 'A' and matrix[y+2][x] == 'M' and matrix[y+2][x+2] == 'M':
                    oh_wow_a_fucking_xmas_lol += 1
                elif matrix[y][x] == 'M'  and matrix[y][x+2] == 'M' and matrix[y+1][x+1] == 'A' and matrix[y+2][x] == 'S' and matrix[y+2][x+2] == 'S':
                    oh_wow_a_fucking_xmas_lol += 1
                elif matrix[y][x] == 'S'  and matrix[y][x+2] == 'M' and matrix[y+1][x+1] == 'A' and matrix[y+2][x] == 'S' and matrix[y+2][x+2] == 'M':
                    oh_wow_a_fucking_xmas_lol += 1
    
    return(oh_wow_a_fucking_xmas_lol)
        


matches = 0
fucking_xmas_matches = 0
with open("data/dia4_lista2.txt", "r") as fichero:
    matrix = []
    for linea in fichero:
        matches += linea.count("XMAS")
        matches += linea.count("SAMX")
        matrix_line = list(linea.replace("\n",""))
        matrix.append(matrix_line) 
    
    diagonals = diagonal_to_string(matrix)
    for line in diagonals: 
        matches += line.count("XMAS")
        matches += line.count("SAMX")
        
    columnas = columnas_to_string(matrix)
    for col in columnas: 
        matches += col.count("XMAS")
        matches += col.count("SAMX")
    
    print("encuentros", matches)
    
    fucking_xmas_matches = oh_wow_its_afucking_x_mas(matrix)
    print("fucking_xmas", fucking_xmas_matches)

       
    