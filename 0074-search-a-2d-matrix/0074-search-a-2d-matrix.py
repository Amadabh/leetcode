class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        target_row = -1
        for i in range(n):
            if matrix[i][0]<=target<=matrix[i][m-1]:
                target_row= i
                break
        if target_row==-1:
            return False
        
        l,r =0,m-1
        while l<r:
            mid = (l+r)//2
            if matrix[target_row][mid]==target:
                return True
            elif matrix[target_row][mid]<target:
                l +=1
            else:
                r-=1

        # will fail this test case [[1]] without the below check 
        if matrix[target_row][l]==target:
            return True
        return False
        