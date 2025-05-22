class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = "a b c e d e f g h i j k l m n o p q r s t u v w x y z"
        d = set(l.strip(" "))
        st=""
        
        for i in s:
            if i.isalpha() and i.lower() in d:
                st+=i.lower()
            if i.isnumeric():
                st+=i
        print(st)
 

        l,r=0,len(st)-1
        while l<=r:
            if st[l]!=st[r]:
                return False
            # print(st[l], st[r])
            l+=1
            r-=1
        return True
        