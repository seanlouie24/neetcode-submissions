class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) solution
        # Since num1 + num2 + num3 = 0
        # num1 + num2 = -(num3)

        # Use the same method as two pointer two sum
        # Thus we need to first sort the array

        nums_sorted = sorted(nums)

        # Loop through each num which is nums[i]
        # Then have two pointers one at j(left) which starts at i+1
        # And then k(right) which starts at the end
        
        length = len(nums)
        ans = []

        for i in range(length):
            # skip duplicates of base number
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            target = -1*nums_sorted[i]
            j = i + 1
            k = length - 1

            while(j < k):
                temp = nums_sorted[j] + nums_sorted[k]
                if temp == target:
                    c_ans = [nums_sorted[i], nums_sorted[j], nums_sorted[k]]
                    ans.append(c_ans)
                    j += 1
                    k -= 1
                    # skip duplicate values for j
                    while j < k and nums_sorted[j] == nums_sorted[j - 1]:
                        j += 1
                    # skip duplicate values for k
                    while j < k and nums_sorted[k] == nums_sorted[k + 1]:
                        k -= 1
                elif temp < target:
                    j += 1
                else:
                    k -= 1
        
        return ans

        # O(n^2)
        # O(n)
                    






