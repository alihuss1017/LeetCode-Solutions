class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for num in digits:
            string += str(num)
        
        ans = list(str(int(string) + 1))
        return [int(i) for i in ans]