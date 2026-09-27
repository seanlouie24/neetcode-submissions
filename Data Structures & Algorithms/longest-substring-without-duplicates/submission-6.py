class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Keep track of current list using a set
        # If we find a repeated character pop the the element on the left
        # Keep doing so until it doesnt repeat anymore
        # at each index see if the current length is longer than
        # the current longest substring

        c_set = set()
        max_len = 0
        left = 0

        for right in range(len(s)):
            while s[right] in c_set:
                c_set.remove(s[left])
                left += 1
            c_set.add(s[right])
            temp = (right-left + 1)
            if temp > max_len:
                max_len = temp

        return max_len

        # O(n)
        # O(m)
            
            
