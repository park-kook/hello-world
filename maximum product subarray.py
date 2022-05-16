
"""
Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (continaing at least one number) 
which has the largest product
"""
nums = [2,3,-2,4]
output = 6

def maxProduct(nums):
    res = max(nums)
    curMin, curMax = 1,1
    for n in nums:
        if n ==0:
            curMin, curMax = 1,1
            continue
        tmp = curMax * n
        curMax = max(n*curMax, n*curMin, n)
        curMin = min(tmp, n*curMin, n)
        res = max(res, curMax)
    return res
maxProduct(nums)

