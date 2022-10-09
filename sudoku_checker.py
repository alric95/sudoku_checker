import numpy as np

# sudoku_file_to_array reads the file and returns a 9x9 numpy array
def sudoku_file_to_array(file):
    int_list = [] 
    with open(file) as f:
        for line in f: 
            # for each line: split by comma, remove non-numerical char and add numbers to int_list
            int_list.extend([int(x) for x in 
                             [char.strip('[ ]') for char in line.split(',') if char.strip('[ ]').isdigit()]])
    grid = np.reshape(int_list, (9, 9)) 
    return grid
    

# sudoku_checker returns True if sudoku is valid. False if sudoku not valid. 
def sudoku_checker(file):
    grid = sudoku_file_to_array(file)
    for i in range(9):
        # j, k index top left corner of each 3x3 tile
        j, k = (i // 3) * 3, (i % 3) * 3
        # For valid sudoku we need three conditions:
        # 1. all the rows have unique values from 1 to 9
        # 2. all the columns have unique values from 1 to 9
        # 3. all the 3x3 tiles have unique values from 1 to 9
        if (set(grid[i,:]) != set(range(1,10)) 
                or set(grid[:,i]) != set(range(1,10))
                or set(grid[j:j+3, k:k+3].ravel()) != set(range(1,10))):
            return False
    return True

                   
sudoku_checker('Correct_Sudoku.txt')
