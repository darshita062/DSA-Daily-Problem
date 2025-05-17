def checkSubarraySum(nums, k):
    if len(nums) < 2:
        return False
    addition = 0
    hash_set = {0:-1}
    for i in range(len(nums)):
        addition += nums[i]
        rem = addition % k
        if rem in hash_set:
            if i-hash_set[rem]>=2: 
                return True
        else:
            hash_set[rem] = i
    return False
