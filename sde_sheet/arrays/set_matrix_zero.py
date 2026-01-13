# matrix = i*j , rox*col.. 
# m = [[1,1,1],[0,0,0]]

# First : Use 2 lists as position markers for the rows and cols we need to make zeros. Time : O(m*n) and Space: O(m+n) -> 2 lists created, assuming all zero matrix
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i in row) or (j in col):
                    matrix[i][j] = 0
        

# Optimal : Use 1st row and col as lists, also use 2 flags for determining if 1st row or col itself needs to be turned to zero (Did they have zeros). 
# Time : O(m*n) -> and Space : O(1) -> means constant space as few fixed variables are needed.

class OptimalSolution:
    # Function to set entire row and column to 0 if an element in the matrix 
    def setZeroes(self, matrix):
        # Get dimensions of matrix
        m = len(matrix)
        n = len(matrix[0])

        # Flag to track if first row should be zeroed
        first_row_zero = False
        # Flag to track if first column should be zeroed
        first_col_zero = False

        # Check if first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row/column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
