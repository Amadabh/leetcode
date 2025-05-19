class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Brute force
        ans =0
        n = len(s)
        for i in range(n):
            st = set()
            for j in range(i,n):
                if s[j] in st:
                    break
                st.add(s[j])
            ans = max(len(st),ans)
        return ans


        #OPtimal
        # n = len(s)
        # l=0
        # if s=="":
        #     return 0
        # st = set()
        # st.add(s[l])
        # ans =0
        # for r in range(1,n):
        #     if s[r] not in st:
        #         st.add(s[r])
        #     else:
        #         ans = max(len(st),ans)
        #         while s[r] in st:
        #             st.remove(s[l])
        #             l+=1
        #         st.add(s[r])
        # ans = max(len(st),ans)
        # return ans



