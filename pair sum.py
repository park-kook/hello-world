'''
Given an interger array, output all the unique paris that sum up to a specific value K. 
pair_sum([1,3,2,2],4) would return 2 paris: (1,3), (2,2)
'''
arr=[1,3,2,2]
k=4

def pair_sum(nums,target):
    if len(nums)<=1:
        return False#means does not return anything.  
    #set for tracking
    seen = set()
#    output = set()
    output = []
    #keep this in mind it;s a really great strategy at converting things that might seem like take order. 
    #and squared and reducing it down to a linear order. 
    for num in nums:
        n = target -num
        if n not in seen:
            seen.add(num)
        else:
#          output.add((min(num,n), max(num,n))) # make tuple 
#          output.add((n,num)) # make tuple  
          output.append((n,num)) # make tuple            
    #return len(output)
   # print('\n'.join(map(str,list(output))))
    print('\n'.join(str(x) for x in output))
#    print(','.join(str(x) for x in output))
#    print('\n'.join(x for x in output))
    #is just taking the output converting into a list,
    #making sure all those tuples are stings by mapping the str function which 
    #converts to a string to every element in that list 
    #and then joining them with new lines in between


nums=[1,3,2,2]
target=4
