'''
Given an array of integers (positive and negative) find the largest continuous sum, that should be continuous.
it should be adjacent
'''
def large_cont_sum(arr):
    if len(arr)==0:
        return 0
    
    max_sum = current_sum = 0
    
    for num in arr:
        current_sum = max(current_sum+num,num)
#        current_sum+=num
        max_sum = max(current_sum,max_sum)
    return max_sum


arr=[1,2,-1,3,4,10,10,-10,-1]
large_cont_sum([1,2,-1,3 ,4,10,10,-10,-1])


large_cont_sum([1,2,-8,-1,10])


nums = [-2,1,-3,4,-1,2,1,-5,4]
output = 6

def maxsubarray(nums):
    cum_sum = 0
    max_sum = max(nums)
    
    for i in range(len(nums)):
        if cum_sum < 0 :
            cum_sum = 0
        cum_sum+=nums[i]
        max_sum  = max(max_sum, cum_sum)
        
    return max_sum
maxsubarray(nums)
