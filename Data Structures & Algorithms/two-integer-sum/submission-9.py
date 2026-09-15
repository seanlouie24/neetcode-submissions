class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Find the diff between the current nums and target
        # Check if that diff is in the dict
        # If not add the current num and continue

        num_dict = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_dict:
                return [num_dict[diff], i]
            num_dict[nums[i]] = i

        # Time: O(n)
        # Space: O(n)
        

