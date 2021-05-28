'''We are discussing about binary search and linear search to see 
which is more convinient to use.'''

#its time complexity is O(n)
def linear_search(arr,numb_to_find):
    for idx,element in enumerate(arr):
        if numb_to_find==element:
            return "Number exist it is on index:{}".format(idx)
    return "Wrong!" 


def binary_search(arr,numb_to_find):
    left_index=0
    mid_index=0 
    right_index=len(arr)-1 

    while left_index<=right_index:
        mid_index=(left_index+right_index)//2 
        mid_element=arr[mid_index]

        if numb_to_find==mid_element:
            return mid_index

        if numb_to_find>mid_element:
            left_index=mid_index+1
        else:
            right_index=mid_index-1 

    return -1
        
    
# def binary_search_recursion(arr,numb_to_find,left_index,right_index):
#     if left_index>right_index:
#         return -1 

#     mid_index=(left_index+right_index)//2
#     mid_element=arr[mid_index] 
    
#     if mid_element==numb_to_find:
#        return mide_index

#     if mid_element<numb_to_find:
#         left_index=mid_index+1 
#     else:
#         right_index=mid_index-1 
#     return  binary_search_recursion(arr,numb_to_find,left_index,right_index)

if __name__=='__main__':
    arr= [1,4,6,9,11,15,15,15,17,21,34,34,56]
    # print(linear_search(arr,67))
    numb_to_find=56
    print(binary_search(arr,numb_to_find))
    # print(binary_search_recursion(arr,numb_to_find,0,len(arr)-1))