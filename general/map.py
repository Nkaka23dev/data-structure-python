import math
#the below code are normal way of calculating areas of different radii using loop
#but wit a map function it can be accomplished by one line of code.
# def area(r):
#     return round((math.pi)*(r**2),2)

# radii=[2,5,7.1,0.3,10]
# areas=[]
# for r in radii:
#     a=area(r)
#     areas.append(a)

# print(areas)


# we can even use list comprehension to reduce the size of the code
# def area(r):
#     return round((math.pi)*(r**2),2)

# radii=[2,5,7.1,0.3,10]
# print([area(r) for r in radii])

# let us use map now

# radii=[2,5,7.1,0.3,10]
print(list(map(lambda r:round(math.pi*(r**2),2),radii)))




































