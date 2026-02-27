class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 
        for _ in range(32):
            res = (res << 1) | ( n & 1) # basically get the last digit of n and add it to res and then when u left keep left shifting it goes to the left side of the end result
            n >>= 1
        
        return res

