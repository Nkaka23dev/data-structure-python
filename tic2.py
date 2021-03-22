
# # returning  a friend when characters are equals to 4
# def friend(arr):
#     return [char for char in arr if len(list(char))==4]
   
# arr=["Ryan", "Kieran", "Jason", "Yous"]
# print(friend(arr))

arr=[1,2,3,4,5,6,7,8,9,0]
str_=[str(n) for n in arr]
new_arr="".join(str_)
print(f"({new_arr[0:3]}) {new_arr[3:6]}-{new_arr[6:10]}")



    

