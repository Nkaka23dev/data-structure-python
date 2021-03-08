def sum_of_naturalNumber(num):
    if num<=1:
        return num
    return num+sum_of_naturalNumber(num-1)

number=int(input("Enter a number to find sum: "))

if number<=0:
    print("Natural ca not be negative or zero!")
else:
    print(sum_of_naturalNumber(number))