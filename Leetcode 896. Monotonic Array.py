def isMonotonic(nums):
        n = len(nums)
        first = nums[0]
        second = nums[n-1]
        if first < second:
            for i in range(n-1):
                if (nums[i] > nums[i+1]):
                    return False
        elif first == second:
            for i in range(n-1):
                if (nums[i] != nums[i+1]):
                    return False
        else:
            for i in range(n-1):
                if (nums[i] < nums[i+1]):
                    return False
        return True