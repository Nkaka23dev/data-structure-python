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

def bin_conv(n):
    if n<=0:
        return "Invalid"
    num=list(bin(n).replace("0b",""))
    count=0
    for i in num:
        if i=="1":
            count+=1
    return count


print(bin_conv(10))