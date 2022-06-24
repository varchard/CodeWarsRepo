def valid_solution(board):
    solution = [1,2,3,4,5,6,7,8,9]
    #board sectors
    square1 = [board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]]
    square2 = [board[0][3],board[0][4],board[0][5],board[1][3],board[1][4],board[1][5],board[2][3],board[2][4],board[2][5]]
    square3 = [board[0][6],board[0][7],board[0][8],board[1][6],board[1][7],board[1][8],board[2][6],board[2][7],board[2][8]]
    square4 = [board[3][0],board[3][1],board[3][2],board[4][0],board[4][1],board[4][2],board[5][0],board[5][1],board[5][2]]
    square5 = [board[3][3],board[3][4],board[3][5],board[4][3],board[4][4],board[4][5],board[5][3],board[5][4],board[5][5]]
    square6 = [board[3][6],board[3][7],board[3][8],board[4][6],board[4][7],board[4][8],board[5][6],board[5][7],board[5][8]]
    square7 = [board[6][0],board[6][1],board[6][2],board[7][0],board[7][1],board[7][2],board[8][0],board[8][1],board[8][2]]
    square8 = [board[6][3],board[6][4],board[6][5],board[7][3],board[7][4],board[7][5],board[8][3],board[8][4],board[8][5]]
    square9 = [board[6][6],board[6][7],board[6][8],board[7][6],board[7][7],board[7][8],board[8][6],board[8][7],board[8][8]]
    #columns
    down1 = [board[0][0],board[1][0],board[2][0],board[3][0],board[4][0],board[5][0],board[6][0],board[7][0],board[8][0]]
    down2 = [board[0][1],board[1][1],board[2][1],board[3][1],board[4][1],board[5][1],board[6][1],board[7][1],board[8][1]]
    down3 = [board[0][2],board[1][2],board[2][2],board[3][2],board[4][2],board[5][2],board[6][2],board[7][2],board[8][2]]
    down4 = [board[0][3],board[1][3],board[2][3],board[3][3],board[4][3],board[5][3],board[6][3],board[7][3],board[8][3]]
    down5 = [board[0][4],board[1][4],board[2][4],board[3][4],board[4][4],board[5][4],board[6][4],board[7][4],board[8][4]]
    down6 = [board[0][5],board[1][5],board[2][5],board[3][5],board[4][5],board[5][5],board[6][5],board[7][5],board[8][5]]
    down7 = [board[0][6],board[1][6],board[2][6],board[3][6],board[4][6],board[5][6],board[6][6],board[7][6],board[8][6]]
    down8 = [board[0][7],board[1][7],board[2][7],board[3][7],board[4][7],board[5][7],board[6][7],board[7][7],board[8][7]]
    down9 = [board[0][8],board[1][8],board[2][8],board[3][8],board[4][8],board[5][8],board[6][8],board[7][8],board[8][8]]
    if not all(elem in square1 for elem in solution):
        return False
    elif not all(elem in square2 for elem in solution):
        return False
    elif not all(elem in square3 for elem in solution):
        return False
    elif not all(elem in square4 for elem in solution):
        return False
    elif not all(elem in square5 for elem in solution):
        return False
    elif not all(elem in square6 for elem in solution):
        return False
    elif not all(elem in square7 for elem in solution):
        return False
    elif not all(elem in square8 for elem in solution):
        return False
    elif not all(elem in square9 for elem in solution):
        return False
    # #should always use loops to check 9 conditions
    # squares = [square1,square2,square3,square4,square5,square6,square7,square8,square9]
    # for square in squares:
    #     if sorted(square) != solution:
    #         return False
    elif not all(elem in down1 for elem in solution):
        return False
    elif not all(elem in down2 for elem in solution):
        return False
    elif not all(elem in down3 for elem in solution):
        return False
    elif not all(elem in down4 for elem in solution):
        return False
    elif not all(elem in down5 for elem in solution):
        return False
    elif not all(elem in down6 for elem in solution):
        return False
    elif not all(elem in down7 for elem in solution):
        return False
    elif not all(elem in down8 for elem in solution):
        return False
    elif not all(elem in down9 for elem in solution):
        return False
    # #should have used a loop to check all the conditions instead of copy/pasting
    # down = [down1,down2,down3,down4,down5,down6,down7,down8,down9]
    # for col in down:
    #     if sorted(col) != solution:
    #         return False
    # #even better, should have used zip to create my columns
    # for col in zip(*board):
    #     if sorted(col) != solution:
    #         return False
    # #so much better but had to consult expert, would be to generate the squares programatically
    # for j in range(3):
    #     for i in range(3):
    #         to_check = []
    #         for line in board[i*3:(i+1)*3]:
    #             to_check.extend(line[j*3:(j+1)*3])
    #         if sorted(to_check) != solution:
    #             return False
    elif not all(elem in list(board[0]) for elem in solution):
        return False
    elif not all(elem in list(board[1]) for elem in solution):
        return False
    elif not all(elem in list(board[2]) for elem in solution):
        return False
    elif not all(elem in list(board[3]) for elem in solution):
        return False
    elif not all(elem in list(board[4]) for elem in solution):
        return False
    elif not all(elem in list(board[5]) for elem in solution):
        return False
    elif not all(elem in list(board[6]) for elem in solution):
        return False
    elif not all(elem in list(board[7]) for elem in solution):
        return False
    elif not all(elem in list(board[8]) for elem in solution):
        return False
    # #should have used loop to check rows
    # for row in board:
    #     if sorted(row) != solution:
    #         return False    
    else:
        return True


test = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]

test2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
        [6, 7, 2, 1, 9, 0, 3, 4, 8],
        [1, 0, 0, 3, 4, 2, 5, 6, 0],
        [8, 5, 9, 7, 6, 1, 0, 2, 0],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 0, 1, 5, 3, 7, 2, 1, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 0, 0, 4, 8, 1, 1, 7, 9]]

print(valid_solution(test))
print(valid_solution(test2))