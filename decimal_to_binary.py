def binary(number):
    if number<=0:
        raise TypeError("Please enter positive number")
    if number>1:
        binary(number//2)
    print(number%2,end='')


binary(34)

