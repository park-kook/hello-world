
'''
Equilibirum index: An index of an array such that the sum of elements at lower indexes is equal to
the sum of elements at higher indexes
# 3 is an equilibrium index, because:
# A[0] + A[1] + A[2]  =  A[4] + A[5] + A[6]
time complexity O(n)
space complexity O(n)
'''
nums = [-7,1,5,2,-4,3,0] 
sum - i1-i2-i3
output = 3
nums = [0,1,5,2,-4,-3,-1]


def equilibrium(nums):
    l_sum, r_sum = 0,0
#    length = len(nums)

    for i in range(len(nums)):
        l_sum = 0
        r_sum = 0
        
        for l in range(i): #left sum

            l_sum+= nums[l]
        for r in range(i+1, len(nums)): #right sum

            r_sum+= nums[r]
            
        if l_sum == r_sum:
            return i
    return -1

equilibrium(nums)





nums = [0,1,5,2,-4,-3,-1] #sum = 0
nums = [-7,1,5,2,-4,3,0] #sum = 0
def equilibrium3(nums):
    l_sum = 0
#    length = len(nums)
    total_sum = sum(nums)
    for i in range(len(nums)):

        total_sum-=nums[i]

        if total_sum == l_sum:
            return i
        l_sum+= nums[i] #left sum
    return -1
 
equilibrium3(nums)
