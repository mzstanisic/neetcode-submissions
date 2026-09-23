class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {};
        for num in nums:
            if num in count:
                return True;
            else:
                count[num] = 1;
        return False
        # i = 0;
        # while i < len(nums)-1:
        #     if nums[i] == nums[i+1]:
        #         return True;
        #     i += 1;
        
        # return False;

        # li = 0
        # lr = 1
        # # l = nums[li];
        # # r = nums[lr];
        # while li < len(nums)-1:
        #     if nums[li] == nums[lr]:
        #         return True;
        #     if lr < len(nums)-1:
        #         lr += 1;
        #     else:
        #         li += 1;
        #         lr = li + 1;

        # return False;




        # for i, num in enumerate(nums):
        #     while (num != nums[i+1]):
        #         print(i);
        #         print(len(nums));
        #         if i < len(nums):
        #             i += 1;

        #     if num == nums[i+1]:
        #         return True
            
        # return False;