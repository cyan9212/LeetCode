from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      
        for col in board:
            dic = defaultdict(int)
            for num in col:
                if num == '.':
                    continue
                if dic[num] == 1:
                    return False
                else:
                    dic[num]+=1
                    
        for i in range(9):
            dic = defaultdict(int)
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if dic[board[j][i]] == 1:
                    return False
                else:
                    dic[board[j][i]]+=1
                    
        direc = [[0,0],[0,1],[0,2],[1,0],[2,0],[1,1],[1,2],[2,1],[2,2]]
        for i in range(0,9,3):
            for j in range(0,9,3):
                dic = defaultdict(int)
                for d in direc:
                    if board[i+d[0]][j+d[1]] == '.':
                        continue
                    if dic[board[i+d[0]][j+d[1]]] == 1:
                        return False
                    else:
                        dic[board[i+d[0]][j+d[1]]]+=1
        return True
