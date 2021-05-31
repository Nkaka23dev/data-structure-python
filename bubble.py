# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         swapped=False
#         for j in range(len(arr)-1-i):
#             if arr[j]>arr[j+1]:
#                 tmp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=tmp 
#                 swapped=True 
#         if not swapped:
#             break
#     return arr
   

# if __name__=='__main__':
#     arr=[1,2,3,4,5,6,7,8,9,10]
#     arr2=['Nkaka','Kwitonda','Abayisenga','Johnson','Kanyange']
#     print("The original list was: ",arr2)
#     print(bubble_sort(arr2))


def bubble_sort(arr,key):
    for i in range(len(arr)-1):
        swapped=False
        for j in range(len(arr)-1-i):
            if arr[j][key]>arr[j+1][key]:
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp 
                swapped=True 
        if not swapped:
            break
    return arr
   

if __name__=='__main__':
    elements=[
    {'name':'kathy','transaction_amount':200,'device':'vivo'},
    {'name':'dhaval','transaction_amount':400,'device':'google pixel'},
    {'name':'aamir','transaction_amount':800,'device':'iphone-8'},
    {'name':'mona','transaction_amount':1000,'device':'iphone-10'}]
 
    # print("The original list was: ",elements)
    print(bubble_sort(elements,key='transaction_amount'))

    
