def missingInteger(nums):
        pre_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                break
            pre_sum += nums[i]
        if pre_sum not in nums:
            return pre_sum
        else:
            while pre_sum in nums:
                pre_sum += 1
            return pre_sum
            