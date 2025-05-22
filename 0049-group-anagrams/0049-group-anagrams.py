class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            st = defaultdict(int)
            for ch in i:
                st[ch]+=1 
            k =[]
            for key,val in st.items():
                k.append(str(key) + str(val))
            k.sort()
            ans[tuple(k)].append(i)
        print(ans)
        return list(ans.values())
        # st = defaultdict(list)
        # for i in strs:
        #     st[tuple(sorted(i))].append(i)
        # return [i for i in st.values()]