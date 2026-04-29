class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return len(nums)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        print(freq)
        i = 0
        for key, value in freq.items():

            if key != val:
                while value:
                    nums[i] = key
                    i += 1
                    value -= 1
        
        return len(nums) - freq[val]

        