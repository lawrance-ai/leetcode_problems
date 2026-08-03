class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Create tower up to query_row (no need for full 100 rows)
        tower = [[0.0] * (r + 1) for r in range(query_row + 1)]
        
        # Pour champagne into the top glass
        tower[0][0] = poured
        
        # Simulate overflow
        for r in range(query_row):
            for c in range(len(tower[r])):
                if tower[r][c] > 1.0:
                    overflow = tower[r][c] - 1.0
                    tower[r][c] = 1.0
                    tower[r + 1][c] += overflow / 2.0
                    tower[r + 1][c + 1] += overflow / 2.0
        
        # Return the amount in the requested glass (max 1.0)
        return min(1.0, tower[query_row][query_glass])
