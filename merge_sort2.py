def merge_sort(elements,key) -> object:
    if len(elements)<=1:
        return 
    mid=len(elements)//2 

    left=elements[:mid]
    right=elements[mid:] 

    merge_sort(left,key)
    merge_sort(right,key)
    return merge_two_arr(left,right,elements,key)


def merge_two_arr(arr1,arr2,arr,key):
    len_a=len(arr1) 
    len_b=len(arr2) 
    i=j=k=0 
    while i<len_a and j<len_b:
        if arr1[i][key]<arr2[j][key]:
            arr[k]=arr1[i]
            i+=1 
        else:
           arr[k]=arr2[j]
           j+=1 
        k+=1
    while i<len_a:
        arr[k]=arr1[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k]=arr2[j] 
        j+=1 
        k+=1


if __name__=="__main__":
    #  arr1=[17,21,29,38]
    #  arr2=[4,9,32,45,98] 
    # elements=[21,38,29,17,4,25,11,32,9]
    #  print(merge_two_arr(arr1,arr2))
    # print("before sort",elements)
    # merge_sort(elements)
    # print("After sort",elements)
    elements=[
    {'name':'kathy','age':17,'time_hours':1},
    {'name':'dhaval','age':12,'time_hours':3},
    {'name':'aamir','age':21,'time_hours':2.5},
    {'name':'mona','age':24,'time_hours':1.5}
    ]
    print("before sort",elements)
    print("==========================================")
    print("===========================================")
    print("============================================")
    merge_sort(elements,key="time_hours")
    print(elements)

