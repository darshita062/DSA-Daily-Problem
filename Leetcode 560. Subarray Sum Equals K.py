def subarraySum(nums, k):
        # brute force method
        """
        count = 0
        for i in range(len(nums)):
            add = 0
            for j in range(i,len(nums)):
                add += nums[j]
                if add == k:
                    count += 1
        return count
        """
        #optimized method
        hashset = {0:1}
        count = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in hashset:
                count += hashset[prefix_sum-k]
            if prefix_sum in hashset:
                hashset[prefix_sum] += 1
            else:
                hashset[prefix_sum] = 1
        return count