
'''
first-depth tree problem
Given a binary tree, get the average value at each level of the trees. 
Input: 
    4
7     9

10 2        6
      6
   2
   
output: [4,8,6,6,2]
'''
#input can be none empty node or always tree input?
#it looks like all interget, can I assume all integer?
#vefore you begin coding, explain out loud how you would like to solve the problem and get feedback from your interviwer
#Depth First Serach using stack - LastIn First Out
class node(object):
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None
    #hash table, my key is depth of the tress and then value can be in the all list of the associated key value
    #can I start the coding?
    #instead of creating dic, I want recurtion, everytime I call
def _collect(node, dict_data,depth = 0):
    if not node: #empty case
        return None
    if depth not in dict_data:
        dict_data[depth] = []
        
    dict_data[depth].append(node.val)
    
    _collect(node.left, dict_data, depth+1)
    _collect(node.right, dict_data, depth+1)
    
def avg_by_depth(node):
    dict_data = {}
    _collect(node, dict_data) #after run left, data = {0:[4],1:[7,9],2:[10,2,6],3:[6],4:[2]}
    
    result = []
    
    i = 0
    while i in dict_data:
        nums = dict_data[i]
        avg = sum(nums) / len(nums)
        result.append(avg)
        i+=1
    
    return result

root = None
root = node(4)
root.left = node(7)
root.right = node(9)
root.left.left = node(10)
root.left.right = node(2)
root.right.right = node(6)
root.left.right.right = node(6)
root.left.right.right.left = node(2)
avg_by_depth(root)

[4,8,6,6,2]
# I wawnt to go through the code by using some example if every case run throgh smoothly         
#data2: {0:(4,1), 1: (16,2)......}
    
class node(object):
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None
        
def _collect(node, dict_data,depth = 0):
    if not node: #empty case
        return None
    if depth not in dict_data:
        dict_data[depth] = (node.val,1)
    else: 
        val, count = dict_data[depth]
        val+=node.val
        count+=1
        dict_data[depth] = (val,count)
        
    
    _collect(node.left, dict_data, depth+1)
    _collect(node.right, dict_data, depth+1)
    
def avg_by_depth(node):
    dict_data = {}
    _collect(node, dict_data) #after run left, data = {0:[4],1:[7,9],2:[10,2,6],3:[6],4:[2]}
    
    result = []
    
    i = 0
    while i in dict_data:
        val,count = dict_data[i]
        avg = val / count
        result.append(avg)
        i+=1
    
    return result
root = None
root = node(4)
root.left = node(7)
root.right = node(9)
root.left.left = node(10)
root.left.right = node(2)
root.right.right = node(6)
root.left.right.right = node(6)
root.left.right.right.left = node(2)
avg_by_depth(root)

dict_data = {0:[4],1:[7,9],2:[10,2,6],3:[6],4:[2]}

node = [[4],[7,9],[10,2,6],[6],[2]]

avg_by_depth(node)
output = [4.0, 8.0, 6.0, 6.0, 2.0]
