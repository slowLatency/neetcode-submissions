class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            l,r = 0, 0
            res = []
            
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            if l >= len(left):
                res += right[r:]
            elif r >= len(right):
                res += left[l:]
            
            return res
                
        def merge_sort(nums):
            if len(nums) == 1:
                return nums

            m = len(nums) // 2
            sorted_left = merge_sort(nums[:m])
            sorted_right = merge_sort(nums[m:])
            res = merge(sorted_left, sorted_right)

            return res
        
        return merge_sort(nums)