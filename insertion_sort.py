def insertion_sort(arr):
    for i in range(1,len(arr)):
        anchor=arr[i] 
        j=i-1 
        while j>=0 and anchor<arr[j]:
            arr[j+1]=arr[j] 
            j=j-1 
        arr[j+1]=anchor

if __name__=='__main__':
    tests=[
    [21,38,29,17,4,25,11,32,9],
    [3,7,9,11],
    [25,22,21,10],
    [29,15,28],
    [],
    [6]
    ]
    for element in tests:
        insertion_sort(element)
        print("Elements after sorting",element) 

    
    