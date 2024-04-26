class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^a-zA-Z\s]', ' ', paragraph.lower()).split()
        paragraph = list(filter(lambda x: x not in banned + [''], paragraph))
        count = Counter(paragraph)
        return max(count, key = count.get)
