
'''
Consider an array of non-negative integers. 
A second array is formed by shuffling the elements of the first array and 
deleting a random element. Given these two arrays, 
find which element is missing in the second array.
'''
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,5,2,1,4,7]

def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1,arr2): #takes iterable, aggregates them in a tuple and return it. 
        print(num1,num2)
        if num1 != num2:
            return num1
        
    return 


finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

