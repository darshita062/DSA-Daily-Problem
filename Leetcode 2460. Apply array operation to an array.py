def applyOperations(nums):
        # function to move all the zeros to the end
        def move_zeros(arr):
            ans = []
            for num in arr:
                if num != 0:
                    ans.append(num)
            if len(ans)!=len(arr):
                return ans + [0]*(len(arr)-len(ans))
            else:
                return ans

        result = [0]*len(nums)

        # using two pointer's 
        l , r = 0 , 1

        if len(nums) < 2:
            return nums
        
        if len(nums) == 2:
            if nums[0] == nums[1]:
                nums[0] = nums[0]*2
                nums[1] = 0
            return move_zeros(nums)

        while r < len(nums):
            if nums[l] == nums[r]:
                result[l] = nums[l]*2
                result[r] = 0
                l += 2
                r += 2
            else:
                result[l] = nums[l]
                l += 1
                r += 1

        # to include the last element
        if nums[len(nums)-2] != nums[len(nums)-1]:
            result[len(nums)-1] = nums[len(nums)-1]
        return move_zeros(result)