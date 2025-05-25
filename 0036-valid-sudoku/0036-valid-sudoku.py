class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m,n= len(board),len(board[0])
        grid = board
        # row
        for i in range(9):
            col = []
            for c in range(9):
                if grid[i][c]!=".":
                    if grid[i][c] in col:
                        return False
                    else:
                        col.append(grid[i][c])
        
            row = []
            for r in range(9):
                if grid[r][i]!=".":
                    if grid[r][i] in row:
                        return False
                    else:
                        row.append(grid[r][i])
                
        
        for x in range(0,9,3):
            for y in range(0,9,3):
                mat =[]
                for r in range(x,x+3):
                    for c in range(y,y+3):
                        print(r,c)
                        if grid[r][c]!=".":
                            if grid[r][c] in mat:
                                return False
                            else:
                                mat.append(grid[r][c])  

        # x=3
        # while x<10:
        #     mat =[]
        #     y =3
        #     for r in range(x-3,x):
        #         while y<10:
        #             for c in range(y-3,y):
        #                 print(r,c)
        #                 if grid[r][c]!=".":
        #                     if grid[r][c] in mat:
        #                         return False
        #                     else:
        #                         mat.append(grid[r][c])  
        #             y+=3
        #     x+=3

        return True

        

            

            

        

