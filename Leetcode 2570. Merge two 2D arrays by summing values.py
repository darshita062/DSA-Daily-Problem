def mergeArrays(nums1,nums2):
        ht = {}  # Dictionary to store merged values
        
        # Process nums1
        for key, value in nums1:
            ht[key] = ht.get(key, 0) + value  # Sum values for same key
        
        # Process nums2
        for key, value in nums2:
            ht[key] = ht.get(key, 0) + value  # Sum values for same key
        
        # Convert dictionary to sorted list
        return sorted([[key, value] for key, value in ht.items()])