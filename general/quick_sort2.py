
def swap(a,b,arr):
    if a!=b:
        tmp=arr[a]
        arr[a]=arr[b] 
        arr[b]=tmp 

def partition(arr):
    pivot_index=0 
    pivot=arr[pivot_index] 

    start=pivot_index+1 
    end=len(arr)-1 

    while start<end:
        while arr[start]<=pivot:
            start+=1 
        while arr[end]>pivot:
            end-=1 
        if start<end:
            swap(start,end,arr) 

    swap(pivot_index,end,arr) 

    return end  


def quick_sort(arr):
    pi=partition(arr) 
    

if __name__=='__main__':
    arr=[11,9,29,7,2,15,28] 
    print(arr) 
    print("===============")
    print(quick_sort(arr)) 
    print(arr)