class Solution:
    def addBinary(self, a: str, b: str) -> str:
        op = ""
        car = 0
        a = a[::-1]
        b = b[::-1]
        i = 0
        
        while i < len(a) or i < len(b):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0
            
            s = digit_a + digit_b + car
            
            op += str(s % 2)
            car = s // 2
            
            i += 1
        
        if car:
            op += "1"
        
        return op[::-1]
