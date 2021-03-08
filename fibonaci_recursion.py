from functools import lru_cache

@lru_cache
def fibo(num):
    if type(num)!=int:
        raise TypeError("n must be integer")
    if num<1:
        raise ValueError("n Must be positive.")
    if num==1:
        return 1
    elif num==2:
        return 1
    elif num>2:
        return fibo(num-1)+fibo(num-2)

number=int(input("Enter a number: "))

for n in range(1,number+1):
    print(n,':',fibo(n))


# def fibo(num):
#     if num<=1:
#         return 1
#     if num==2:
#         return 1
#     return fibo(num-1)+fibo(num-2)

# number=int(input("Enter a number to find fibonacci: "))

# for n in range(1,number):
#     print(n,":",fibo(n))

# fibonacci_cache={}






# def fibbo(num):
#     # checking if value exist in cache memory
#     if num in fibonacci_cache:
#         return fibonacci_cache[num]
#     # calculating fibonnaci 
#     if num==1:
#         value=1
#     elif num==2:
#         value=1
#     elif num>2:
#         value=fibbo(num-1)+fibbo(num-2)
#     fibonacci_cache[num]=value
#     return value

# number=int(input("Enter a number to find fibonacci: "))

# for n in range(1,number):
#     print(n,":",fibbo(n))