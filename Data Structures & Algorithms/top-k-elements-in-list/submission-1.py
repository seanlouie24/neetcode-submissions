class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        
        top_k_frequent = heapq.nlargest(k, nums_dict, key=nums_dict.get)
        return top_k_frequent

        # Time: O(nlogk)
        # Space: O(n)