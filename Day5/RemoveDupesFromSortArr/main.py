class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        idx = 0
        while idx < len(nums):
            if nums[idx] in unique:
                nums.remove(nums[idx])
            else:
                unique.append(nums[idx])
                idx += 1