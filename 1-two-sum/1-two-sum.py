class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, value in enumerate(nums):
            if target - value in seen:
                return [i, seen[target - value]]
            
            seen[value] = i

        return seen