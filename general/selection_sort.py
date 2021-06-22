# def find_min_number(arr):
#     min=200000000 
#     for i in range(len(arr)):
#         if min>arr[i]:
#             min=arr[i]
#     return min

def selection_sort(arr,sort_by_list):
    size=len(arr)
    for key in sort_by_list[-1::-1]:
        for i in range(size):
            min_index=i
            for j in range(min_index+1,size):
                if arr[j][key]<arr[min_index][key]:
                    min_index=j 
            if i!=min_index:
                arr[i],arr[min_index]=arr[min_index],arr[i]
    
if __name__=='__main__':
    elements=[78,12,15,8,61,53,23,27]
    # print(find_min_number(elements)) 
    arr=[
        {"First Name":"Raj","Last Name":"Nayyar"},
        {"First Name":"Suraj","Last Name":"Sharma"},
        {"First Name":"Karan","Last Name":"Kumar"},
        {"First Name":"Jade","Last Name":"Canary"},
        {"First Name":"Raj","Last Name":"Thakur"},
        {"First Name":"Raj","Last Name":"Sharma"},
        {"First Name":"Kiran","Last Name":"Kamla"},
        {"First Name":"Armaan","Last Name":"Kumar"},
        {"First Name":"Jay","Last Name":"Sharma"},
        {"First Name":"Ingrid","Last Name":"Galore"},
        {"First Name":"Jay","Last Name":"Seth"},
        {"First Name":"Armaan","Last Name":"Dadra"},
        {"First Name":"Ingrid","Last Name":"Maverick"},
        {"First Name":"Aahana","Last Name":"Arora"}
    ]

    # selection_sort(arr,["First Name","Last Name"])
    # for i in arr:
    #     print(i)
    tests=[
    [21,38,29,17,4,25,11,32,9],
    [3,7,9,11],
    [25,22,21,10],
    [29,15,28],
    [],
    [6]
    ]

    for test in tests:
        selection_sort(test,["First Name","Last Name"]) 
        print(test)
   

