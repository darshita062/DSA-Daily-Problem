from collections import defaultdict
def largestInteger(nums, k):
        if len(nums) < k:
            return -1
    
        window_count = defaultdict(int)  # Track frequency inside the window
        global_count = defaultdict(int)  # Track how many windows contain each element
    
        # Initialize the first window
        for i in range(k):
            window_count[nums[i]] += 1
        for num in window_count:
            global_count[num] += 1
    
        # Sliding window
        for i in range(k, len(nums)):
            # Remove the leftmost element
            left = nums[i - k]
            window_count[left] -= 1
            if window_count[left] == 0:
                del window_count[left]
    
            # Add the new element
            right = nums[i]
            window_count[right] += 1
    
            # Update global count
            for num in window_count:
                if num not in global_count:
                    global_count[num] = 1
                else:
                    global_count[num] += 1
    
        # Find the largest number appearing in exactly one window
        candidates = [num for num, count in global_count.items() if count == 1]
        
        return max(candidates) if candidates else -1