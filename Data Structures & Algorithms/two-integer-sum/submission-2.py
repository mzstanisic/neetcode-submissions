class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0;
        r = 1;
        while l < len(nums) - 1:
            # if nums[l] <= target and nums[r] <= target:
            if (nums[l] + nums[r]) == target:
                return [l, r];
            r += 1;
            if r == len(nums):
                l += 1;
                r = l + 1;

            
            
