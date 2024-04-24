class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        copy = list(reversed(sorted(score)))
        ans = [0 for _ in range(len(score))]
        for n in range(len(score)):
            if n == 0:
                ans[score.index(copy[n])] = "Gold Medal"
            elif n == 1:
                ans[score.index(copy[n])] = "Silver Medal"
            elif n == 2:
                ans[score.index(copy[n])] = "Bronze Medal"
            else:
                ans[score.index(copy[n])] = f'{n + 1}'
        return ans