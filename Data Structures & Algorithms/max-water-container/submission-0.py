class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
    # Two pointer approach
    # Start with one pointer on the first bar and one on the last
    # move past the smaller bar at each step since it caps our max_amt lower


        left = 0
        right = len(heights) - 1
        max_amt = 0

        while(left < right):
            height = min(heights[left], heights[right])
            width = right - left
            if (height*width) > max_amt:
                max_amt = height*width
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_amt

        # O(n)
        # O(1)


