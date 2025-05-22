class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        st = defaultdict(list)
        for i in strs:
            st[tuple(sorted(i))].append(i)
        return [i for i in st.values()]