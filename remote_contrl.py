from functools import lru_cache
# class remote_control:
#     def __init__(self):
#         self.channels=["TV1","RTV","ISIBO","PRIME TV","VICTORY"]
#         self.index=-1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.index+=1
#         if self.index==len(self.channels):
#             raise StopIteration
#         return self.channels[self.index] 

# r=remote_control()
# itr=iter(r) 
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


# def remote_control_next():
#     yield "RTV"
#     yield "Nkaka"

# itr=remote_control_next()
# print(next(itr))
# print(next(itr))
# print(next(itr))


# fibonacci sequence using  recursion
# @lru_cache
# def fibo(n):
#     if n<1:
#        raise ValueError("It should be greater than zero")
#     if n==1:
#         return 1
#     if n==2:
#         return 1
#     return fibo(n-1)+fibo(n-2)
    

# arr=10000000

# for i in range(1,arr+1):
#     print(fibo(i))

# generatin fibonacci sequence using Generators


# def fib():
#     a, b=0, 1
#     while True:
#         yield a
#         a, b=b, a+b 


# for f in fib():
#     # if f>50:
#     #     break
#     print(f)


# numbers=[1,2,3,4,5,6,7,8,9,10,11,12,34]
# s=set([1,2,3,4,5,6,7,8,2,1,5,7,2])
# print([i for i in s if i%2==0])

#turning two list into a dictionary
# cities=["Kigali","kampala","Adi sabeba","Mombai","Dodoma","Kinshasa"]
# countries=["Rwanda","Uganda","Ethiopia","India","Tanzania","Congo Kinshasa"]

# d={city:country for city,country in zip(cities,countries)}


# for key,value in d.items():
#     print(key,value)

# sets

# a={"Nkaka","Runyange","Nkaka","Frank","Runyange","Kanyange"}
# print(a)
s=set()
s.add("Nkaka")
s.add("Kigali")
s.add("Rwanda")
s.add("Nkaka")
print(s)

'''difference between lis and set, set contains unique elements and it is not indexable 
i-e it does start from 0.....n'''