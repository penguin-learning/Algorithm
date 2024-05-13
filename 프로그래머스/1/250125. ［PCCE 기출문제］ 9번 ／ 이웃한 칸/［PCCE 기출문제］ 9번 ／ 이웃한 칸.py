def solution(board, h, w):
    count = 0
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        
        w_check = w + dw[i]
        h_check = h + dh[i]
        
        if w_check < 0 or h_check < 0 or w_check >= len(board) or h_check >= len(board):
            continue
            
        if board[h_check][w_check] == board[h][w]:
            count += 1
    
    return count