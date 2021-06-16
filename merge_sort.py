def merge_sort(arr):
    if len(arr)<=1:
        return arr 
    mid=len(arr)//2 

    left=arr[:mid] 
    right=arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right) 

    return merge_sort_two_arr(left,right)

def merge_sort_two_arr(a,b):
    new_list=[]
    len_a=len(a) 
    len_b=len(b) 
    i=j=0 
    while i<len_a and j<len_b:
        if a[i]<b[j]:
            new_list.append(a[i])
            i+=1 
        else:
            new_list.append(b[j])
            j+=1 

    while i<len_a:
        new_list.append(a[i])
        i+=1 

    while j<len_b:
        new_list.append(b[j])
        j+=1 
    return new_list


if __name__=="__main__":
    arr=[21,38,29,17,4,25,11,32,9]
    print(merge_sort(arr)) 

