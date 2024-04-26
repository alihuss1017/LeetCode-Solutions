class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thresh = len(nums) // 2
        count = Counter(nums)
        for key, val in count.items():
            if val > thresh:
                return key