'''Create a function that calculate the sum of number from 1 to n using
recursion ''' 
# def find_sum(n):
#     if n==1:
#         return 1 
#     return n+find_sum(n-1)
from functools import lru_cache 

@lru_cache
def fibo(n):
  if type(n)!=int:
      raise TypeError("Only integers are allowed.")
  if n<1:
      raise ValueError("Number should be greater than 1.") 
  if n==1:
      return 1 
  if n==2:
      return 1 
  return fibo(n-1)+fibo(n-2) 

if __name__=='__main__':
    # print(find_sum(100)) 
    n=int(input("Enter a number to find fibonacci sequence: "))

    for i in range(1,n+1):
        print(f"The fibonacci of {i} is: {fibo(i)}")
 
