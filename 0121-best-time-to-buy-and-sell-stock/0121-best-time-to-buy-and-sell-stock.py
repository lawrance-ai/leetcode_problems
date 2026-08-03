import math
class Solution:        
    def maxProfit(self, prices: list[int]) -> int:
        max = -math.inf
        n_max = 0
        min = math.inf
        n_min = 0
        op = 0
        n = len(prices)-1  
        def pos(n):
            for i in range(len(prices)-1,-1,-1):
                if prices[i] == n:
                    return i
        while n >= 0:
            a = prices[n]
            if a > max:
                max = a 
                n_max = n               
            if a < min:
                min = a
                n_min = n
                print("min:",min)
            if n_min>n_max:
                min = max
                n_min = n_max                
            if op < max - min:
                op = max - min
            n -= 1
        return op
