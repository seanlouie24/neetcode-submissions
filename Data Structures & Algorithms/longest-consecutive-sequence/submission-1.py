class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest = 0
        
        for num in nums:
            if not num - 1 in nums_set:
                temp = num
                counter = 1
                while True:
                    temp += 1
                    if not temp in nums_set:
                        break
                    counter += 1

                if counter > longest:
                    longest = counter
        
        return longest

        # Time complexity: O(n)
        # Space complexity: O(n)