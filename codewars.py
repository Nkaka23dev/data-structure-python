# def likes(names):
#     if len(names)==0:
#         return "no one likes this"
#     elif len(names)==1:
#         return f"{names[0]} likes this"
#     elif len(names)==2:
#         return f"{names[0].title()} and {names[1].title()} like this"
#     elif len(names)==3:
#         return f"{names[0].title()},{names[1].title()} and {names[2].title()} like this"
#     else:
#         return f"{names[0].title()},{names[1].title()} and {len(names)-2} others like this"
    
# arr=["kettia","kwitonda","munyarukundo"]
# print(likes(arr))








































# def count_bit(num):
#     if num<=0:
#         return "Invalid"
#     if num==1:
#         return 1
    
#     count_bit(num//2)
#     return (num%2)

# my_func=count_bit(10)

# for i in list(my_func):
#     print(i)

# #a  function to return number of 1 present in an binary 
# def bin_conv(n):
#     if n<=0:
#         return "Invalid"
#     num=list(bin(n).replace("0b",""))
#     count=0
#     for i in num:
#         if i=="1":
#             count+=1
#     return count
# print(bin_conv(10))


#a  function to return number of 1 present in an binary 
def bin_conv(n):
    if n<=0:
        return "Invalid"
    num=list(bin(n).replace("0b",""))
    # new_num=num[-4]
    return num

print(bin_conv(10))

