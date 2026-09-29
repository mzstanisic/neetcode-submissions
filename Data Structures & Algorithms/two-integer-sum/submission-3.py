class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0;
        bucket = {}
        bucket[nums[l]] = 0;

        while l < len(nums):
            diff = target - nums[l];
            # don't check the first since it would be a duplicate if it matches
            if l > 0:
                if diff in bucket:
                    return [bucket[diff], l];

                bucket[nums[l]] = l;
            l += 1;
        
        
        ''' O(n^2) time, O(1) space
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
        '''
            
            
