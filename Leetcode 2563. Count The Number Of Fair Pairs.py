def countFairPairs(nums, lower, upper):
        nums.sort()
        n = len(nums)
        res = 0

        def count_pairs(max_sum):
            count = 0
            left, right = 0, n - 1
            while left < right:
                if nums[left] + nums[right] <= max_sum:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count

        return count_pairs(upper) - count_pairs(lower - 1)