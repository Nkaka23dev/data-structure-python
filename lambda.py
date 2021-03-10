# lambda is a function with no name
# example of normal functions

# def calc_num(x):
#     return 3*x+1

# print(calc_num(3))

# g=lambda x:3*x+1
# print(g(3))

# full_name=lambda f_name,l_name:f"{f_name.strip().title()} {l_name.strip().title()} "
# print(full_name("Eric ","     Nkaka"))

# name=lambda:"Hello Nkaka how are you."
# print(name())

def quadratic_eq(a,b,c):
    return lambda x:a*x**2+b*x+c

print(quadratic_eq(2,3,-5)(2))