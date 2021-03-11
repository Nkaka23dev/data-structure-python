def find_fac(n):
    if n==1:
        return n
    else:
        return n*find_fac(n-1)

number=int(input("Enter a number to find factorial: "))

if number<0:
    print("No factorial of negative numbers! Only positive numbers.")
elif number==0:
    print(1)
else:
    print(find_fac(number))
