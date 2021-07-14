'''

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

'''


class Solution:

    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    def solution(self,board,word,x,y,cur): #x, y is the current position we are on the board, cur is the current string
        if(x<0 or x>len(board) or y<0 or y>=len(board[x]) or board[x][y]==' '): #check if x,y is within the board boundry or if the current element is visited. If it's visited, we lableled as empty
            return False
        
        
        cur +=board[x][y] # if x,y are within the boundry, add it to the current string
        if(len(cur)>len(word)): # check if cur string longer than the target word, then it's not what we are looking
            return False
        if(cur[len(cur)-1]!=word[len(cur)-1]): # check if the last character of the current string and the target word are the same
            return False
        if(cur==word):
            return True
        
        temp=board[x][y]
        board[x][y]=' ' #mark it as visited
        
        for i in range(4): #check the adjanet cells: up, down, left, right
            if(self.solution(board,word,x+self.dx[i],y+self.dy[i],cur)):
                return True
        
        board[x][y]=temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool: #check if the first character of input word is matched with the character on the current location of the board. If not, don't even bother to start the recursion function
        if(len(word)==0):
            return True #if the input is empty, we return true because there's no word to search for
        
        n=len(board)
        for i in range(n):
            m=len(board[i]) 
            for j in range(m):
                if(word[0]==board[i][j] and self.solution(board,word,i,j,"")): # if the first character of input word is matched with the character on the current location of the board and soltion function return true
                    return True
        return False