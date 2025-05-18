def numSubarrayProductLessThanK(nums, k):
    #BruteForce Method
    """
    count = 0
    for i in range(len(nums)):
        mul = 1
        for j in range(i,len(nums)):
            mul *= nums[j]
            if mul < k:
                count += 1
            else:
                break
    return count
    """
    #Optimized Method
    if k<=1:
        return 0
    count = 0
    mul = 1
    left = 0
    for right in range(len(nums)):
        mul *= nums[right]
        while mul >= k:
            mul /= nums[left]
            left += 1
        count += right-left+1
    return count
