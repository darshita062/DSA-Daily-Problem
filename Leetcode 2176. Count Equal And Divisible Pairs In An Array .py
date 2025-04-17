def countPairs(nums, k):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if 0 <= i < j < n and nums[i] == nums[j] and (i*j)%k == 0:
                    count += 1
        return count