def sortedSquares(self, nums):
        l , r = 0 , len(nums)-1
        res = [0]*len(nums)
        for k in reversed(range(len(nums))):
            if nums[l]**2 > nums[r]**2:
                res[k] = nums[l]**2
                l += 1
            else:
                res[k] = nums[r]**2
                r-=1
        return res