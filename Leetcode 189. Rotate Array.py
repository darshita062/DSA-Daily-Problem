def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    def reverse(arr,start,end):
        while (start<end):
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
        return arr
    length = len(nums)
    k = k % length
    reverse(nums,0,length-1)
    reverse(nums,0,k-1)
    reverse(nums,k,length-1)
    return nums