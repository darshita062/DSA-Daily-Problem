class Solution:
    def triangleType(nums):
        nums.sort()
        a,b,c = nums
        if a == b == c:
            return "equilateral"
        elif a + b <= c:
            return "none"
        elif a != b != c:
            return "scalene"
        else:
            return "isosceles"