class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        for key, value in d.items():
            if value > len(nums)/2:
                return key
