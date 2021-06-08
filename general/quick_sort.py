# def swap(a,b,arr):
#     # arr[a],arr[b]=arr[b],arr[a] 
#     tmp=arr[a]
#     arr[a]=arr[b]
#     arr[b]=tmp

# def partition(elements,start,end):
#     start_index=start
#     pivot=elements[start_index] 

#     start=start_index+1 
#     while start<end:
#         while start<len(elements) and elements[start]<=pivot:
#             start+=1 

#         while elements[end]>pivot:
#             end-=1  

#         if start<end:
#             swap(start,end,elements)
#     swap(start_index,end,elements)

#     return end 


# def quick_sort(arr,start,end): 
#     if start<end:
#         pi=partition(arr,start,end) 
#         quick_sort(arr,start,pi-1) 
#         quick_sort(arr,pi+1,end)

# if __name__=='__main__':
#    c
#     quick_sort(arr,0,len(arr)-1) 
#     print(arr)


