import numpy as np

def solution(key, lock):
    K = len(key[0])
    L = len(lock[0])
    T = L + 2*(K-1)
    lock = np.asarray(lock)

    def rotate(key):
        key = np.array(key)
        return np.rot90(key)

    key1 = np.array(key)
    key2 = rotate(key1)
    key3 = rotate(key2)
    key4 = rotate(key3)

    variant_board = []
    
    for key in [key1,key2,key3,key4]:
        for i in range(K+L-1):
            for j in range(K+L-1):
                board = np.zeros((T,T))
                board[i:i+K,j:j+K] = key
                variant_board.append(board)
    
    def fit(map_, lock):
        board = np.zeros((T,T))
        board[K-1:K+L-1, K-1:K+L-1] = lock

        for i in range(K-1, K+L-1):
            for j in range(K-1, K+L-1):
                if board[i][j] == 0 and map_[i][j] == 1:
                    board[i][j] = 1
                elif board[i][j] == 1 and map_[i][j] == 1:
                    return False
        if 0 not in board[K-1:K+L-1, K-1:K+L-1]:
            return True
        else:
            return False

    for i,map_ in enumerate(variant_board):
        
        if fit(map_,lock):
            return True
    # print(len(variant_board))
    return False


if __name__ == '__main__':
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock =[[1, 1, 1], [1, 0, 0], [1, 0, 1]]
    print(solution(key,lock))