# Python3 implementation of Linked Lists
# Modified from https://www.geeksforgeeks.org/create-linked-list-from-a-given-array/
#%%
# Representation of a node 
class Node:  
    def __init__(self, data = 0, next = None):  
        self.data = data  
        self.next = next
#%% 
# Function to insert node 
def insert(linkedList, data): 
    insertNode = Node(data) 
      
    if (linkedList == None): 
        linkedList = insertNode 
    elif type(linkedList) == type(Node()): 
        ptr = linkedList 
        while (ptr.next != None): 
            ptr = ptr.next
        ptr.next = insertNode
    else:
        raise TypeError('input is not a node in linked list')
      
    return linkedList 
#%%
# init linkedlist from arr
def arrayToList(arr): 
    linkedList = None
    for i in range(len(arr)): 
        linkedList = insert(linkedList, arr[i])
      
    return linkedList 
#%%
# Simple print display
def display(linkedList): 
    while (linkedList != None) : 
        print(linkedList.data, end = " ") 
        linkedList = linkedList.next
#%%
# Driver code 
if __name__=='__main__':  
    arr = [1, 2, 3, 4, 5] 
    linkedList = arrayToList(arr)
    display(linkedList) 
#%%
def test_insert_type_error(self):
    with self.assertRaises(TypeError):
        insert(0,0)