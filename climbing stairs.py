climbing stairs
you are climbing a staircase it takes n steps to reach the top.
'''
n=2
ouput=2
n=3
output=3

def climbStairs(n):
    one, two = 1,1
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one
climbStairs(2)
climbStairs(3)
