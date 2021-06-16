def insertion_sort(elements):
    for i in range(1,len(elements)):
        anchor=elements[i] 
        j=i-1 
        while j>=0 and anchor<elements[j]:
            elements[j+1]=elements[j] 
            j=j-1 
        elements[j+1]=anchor


if __name__=='__main__':
    tests=[
    [21,38,29,17,4,25,11,32,9],
    [3,7,9,11],
    [25,22,21,10],
    [29,15,28],
    [],
    [6]
    ]
    print("Elements before sort",tests)
    print("================================")
    for el in tests:
        insertion_sort(el)
        print("Elements after sort: ",el)