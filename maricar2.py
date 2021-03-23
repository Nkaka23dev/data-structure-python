
# # returning  a friend when characters are equals to 4
# def friend(arr):
#     return [char for char in arr if len(list(char))==4]
   
# arr=["Ryan", "Kieran", "Jason", "Yous"]
# print(friend(arr))

# # python programm to make a phone number from a list of numbers
# arr=[1,2,3,4,5,6,7,8,9,0]
# str_=[str(n) for n in arr]
# new_arr="".join(str_)
# print(f"({new_arr[0:3]}) {new_arr[3:6]}-{new_arr[6:10]}")


# def fizzBuzz(n):
#     if n<0 and n>(2*10**5):
#         raise ValueError("Not valid")
#     else:
#         for i in range(1,n+1):
#             if i%3==0 and i%5==0:
#                 print("FizzBuzz")
#             elif i%3==0:
#                 print("Fizz")
#             elif i%5==0:
#                 print("Buzz")
#             else:
#                 print(f"{i}")
        
# fizzBuzz(-25)

# def arrSum(number):
#     i
#     sum=0
#     for i in number:
#         sum+=i
#     return sum
     

# arr=[3,4,5]
# print(arrSum(arr))

def dnaComplement(s):
    word=s.casefold()
    new_word=list(reversed(word))
    for i in new_word:
        if i=="a":
            x="t"
            i="t"
        if i=="t":
            temp=i
            i=temp
    return new_word

print(dnaComplement('ACCGGGTTTT'))



    

