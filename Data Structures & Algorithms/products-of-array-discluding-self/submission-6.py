class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)
        prefix = [None] * len_nums
        suffix = [None] * len_nums

        # Pass from left to right
        prefix_num = 1
        for i in range(len_nums):
            prefix[i] = prefix_num
            prefix_num = prefix_num * nums[i]
        
        # Pass from right to left
        suffix_num = 1
        for i in range(len_nums-1, -1, -1):
            suffix[i] = suffix_num
            suffix_num = suffix_num * nums[i]

        ans = []
        for i in range(len_nums):
            ans.append(prefix[i] * suffix[i])
        
        return ans

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
