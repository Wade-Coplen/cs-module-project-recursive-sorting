# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # Base Case (where we will stop)
    if start >= end:
        mid = (start + end) // 2
        # if the element is the middle
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            # if the element is < mid it will be on the left side array
            return binary_search(arr, target, end, mid - 1)
        else:
            # else the elemnt is in >, will be on the right side
            return binary_search(arr, target, start, mid + 1)
    else:
        return -1

           
            

    
  

        

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#def agnostic_binary_search(arr, target):
    # Your code here

