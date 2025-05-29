class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans =[]
        str_maxlen = 2*n
        def rec(num, open, st):
            if len(st)==str_maxlen:
                ans.append(st)
                return

            if num==0:
            #wjhile loop close: based on len of the string in between
                while open!=0:
                    st+=")"
                    open-=1
                ans.append(st)
                return

            if num>0:
                #open
                rec(num-1,open+1,st+"(")
            if open>0:
                #close
                rec(num,open-1,st+")")
                
        rec(n,0,"")
        return ans
        