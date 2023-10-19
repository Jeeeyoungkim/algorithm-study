def solution(board):
    len_board = len(board)
    answer = 0
        
    for y in range(len_board):
        for x in range(len_board):
            if board[y][x] == 1: # 지뢰가 있는 곳 찾기
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        myY = y + dy
                        myX = x + dx

                        if 0 <= myX < len_board and 0 <= myY < len_board:
                            if board[myY][myX] != 1:
                                board[myY][myX] = "X"
                                
    for y in range(len_board):
        for x in range(len_board):
            if board[y][x] == 0: # 지뢰가 없는 곳 찾기
                answer += 1

    return answer