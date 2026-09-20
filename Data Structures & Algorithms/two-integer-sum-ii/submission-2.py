class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Cannot use a hashmap since our solution must use O(1) additional space
        # Use two pointers one starting at the left and one at the right
        # Add the two together if the number is too small increment the left pointer
        # If the number is too large decrement the right number

        left = 0
        right = len(numbers) - 1

        while(left < right):
            temp = numbers[left] + numbers[right]
            if temp < target:
                left += 1
                continue
            elif temp > target:
                right -= 1
                continue
            
            return [left+1, right+1]


        # Time: O(n)
        # Space: O(1)