
import time

def calc_square(numbers):
    start=time.time()
    new_numbers=[]
    for num in numbers:
        new_numbers.append(num*num)
    end=time.time()
    print("cal_square took "+str((end-start)*1000)+" mill sec")
    return new_numbers

def calc_cube(numbers):
    start=time.time()
    new_numbers=[]
    for num in numbers:
        new_numbers.append(num*num*num)
    end=time.time()
    print("cal_cube took "+str((end-start)*1000)+" mill sec")
    return new_numbers

numbers=range(1,11)
print(calc_square(numbers))
print(calc_cube(numbers))
 


