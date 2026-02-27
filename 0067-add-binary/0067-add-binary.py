class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = min(len(a), len(b))
        c = 0
        res = []
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            total = digitA + digitB + c
            res.append(str(total % 2))
            c = total//2
        
        if c:
            res.append('1')
        print(res)
        return "".join(res)[::-1]

    



        