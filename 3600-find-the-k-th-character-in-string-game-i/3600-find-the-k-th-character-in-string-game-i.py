class Solution:
    def kthCharacter(self, k: int) -> str:
        nextChar = {}
        # print(chr(97))
        for i in range(ord('a'),ord('z')+1):
            nextChar[chr(i)] = chr(i+1)
        nextChar['z'] ='a'
        # print(nextChar)

        word = 'a'
        while len(word)<k:
            add =""
            for ch in word:
                add+=nextChar[ch]
            word += add
        return word[k-1]


        