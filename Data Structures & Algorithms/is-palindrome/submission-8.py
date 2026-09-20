class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # We need to create two pointers
        # One keeping track from left to right and one from right to left
        
        left = 0
        right = len(s) - 1

        while(left < right):
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if not s[left].lower() == s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True


        # Time complexity: O(n)
        # Space complexity: O(1)