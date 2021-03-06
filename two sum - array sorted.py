'''
Given an array of integers that is already sorted in ascending order. Find
two numbers such that they add up to a specific target number. 
The function twoSum should return indices of the two numbers such that they add up to that target,
where index1 must be less than index2

Time Complexity: O(N).
Space Complexity: O(1).
'''
numbers = [2,7,11,15]
target = 9

def twoSum(numbers, target):
    l,r = 0, len(numbers)-1
    while l<r:
        curSum = numbers[l] + numbers[r]
        
        if curSum > target:
            r-=1
        elif curSum < target:
            l+=1
        else:
           # return [l+1, r+1]
            return [l, r]
    return -1


twoSum(numbers, target)






def twosum(nums, target):
    d={}
    for i, v in enumerate(nums):
        if target-v not in d:
            d[v] = i
        else: 
            return d[target-v],i
nums = [2,8,11,15]
target = 10   
twosum(nums, target)        
