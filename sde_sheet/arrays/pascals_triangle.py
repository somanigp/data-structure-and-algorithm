class Solution: # O(N*2) -> Both time and space. As we make additional space to store pascals triangle.
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1) # n1 is 1st row with 1 element, and so on. row should be equal to no of elements in the row.

            for j in range(1, i): # first and last element of each row should be zero 
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j] # r is row, j is col

            triangle.append(row)
        
        return triangle

# For understanding
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         triangle = []
#         for i in range(1, numRows+1):
#             row = [1]*i

#             for j in range(1,i-1):  # in case of n5 - j should have values 0 to 4 as it represent col thus it should iterate over 1 to 3. Thus n - 1
#             # i-1 -> is the current row and i-2 is the prev row.
#                 row[j] = triangle[i-2][j-1] + triangle[i-2][j]
#             triangle.append(row)
        
#         return triangle



        