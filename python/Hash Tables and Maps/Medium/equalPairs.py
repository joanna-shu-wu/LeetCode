"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Store the first row of the grid
        column_starts_with = grid[0]

        # Initialize a list to store the columns of the grid
        columns = [[] for _ in column_starts_with]
        
        # Iterate through each row of the grid
        for row in grid:
            # Iterate through each element in the row and append it to the corresponding column
            for j, element in enumerate(row):
                columns[j].append(element)
        
        # Initialize a variable to count the equal pairs
        equal_pairs = 0

        # Iterate through each row of the grid
        for row in grid:
            # Iterate through each element in the first row
            for j, element in enumerate(column_starts_with):
                # Check if the first element of the row is equal to the element in the corresponding column
                if row[0] == element:
                    # Check if the entire row is equal to the column
                    if row == columns[j]:
                        equal_pairs += 1
    
        return equal_pairs


sol=Solution()
print(sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))