class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l=0
        if s=="":
            return 0
        st = set()
        st.add(s[l])
        ans =0
        for r in range(1,n):
            if s[r] not in st:
                st.add(s[r])
            else:
                ans = max(len(st),ans)
                while s[r] in st:
                    st.remove(s[l])
                    l+=1
                st.add(s[r])
        ans = max(len(st),ans)
        return ans




        # def rec(i,path):
           
        #     if i == len(s) or s[i] in path:
        #         return len(path)

        #     path.add(s[i])
        #     result = rec(i + 1, path)
        #     path.remove(s[i])
        #     return result

        # return rec(0,set())

            

        # m = 0
        # st= set()
        # for i in s:
        #     if i not in st:
        #         st.add(i)
        #     else:
        #         m = max(len(st),m)
        #         st.remove(i)
        #         st.add(i)
        # m = max(len(st),m)
        # return m
        