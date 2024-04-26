class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        a = list(words[0])
        for word in words[1:]:
            b = []
            for c in word:
                if c in a:
                    b.append(c)
                    a.remove(c)
            a = b   
        return a    

