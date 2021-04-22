# def area(base,height):
#     print("__name__:",__name__)
#     return 1/2*(base*height)

# if __name__=="__main__":
#     a=area(10,20)
#     print("Area",a)


# x=input("Enter the first number: ")
# y=input("Enter the second number: ")


# try:
#     sum=int(x)/int(y) 
# except ZeroDivisionError:
#     print("You can not divide by zero.")
# except TypeError :
#     print("Type error exception.")
# finally:
#     print("sum is: ", sum)

# class Human:
#     def __init__(self,name,occupation):
#         self.name=name
#         self.occupation=occupation

#     def do_work(self):
#         if self.occupation=="actor":
#             print(self.name," is the best actor in the movie")
#         elif self.occupation=="player":
#             print(self.name,"Is a football player")

#     def speak(self):
#         print(self.name,"says how are you.")
    
# human=Human("Nyaxo","actor")
# human.do_work()
# human.speak()

# class Vehicle:
#     def general_usage(self):
#         print("General usage: Transportation")

# class Car(Vehicle):
#     def __init__(self):
#         print("I am a Car")
#         self.wheels=4
#         self.has_roof=True
    
#     def specific_usage(self):
#         self.general_usage()
#         print("Specific usage: Commute to work and family trip")

# class MotorCycle(Vehicle):
#     def __init__(self):
#         self.wheels=2
#         self.has_roof=False

#     def specific_usage(self):
#         print("Specific usage: Rood Trip and racing")

# c=Car()
# c.specific_usage()
# print(f"Car has: {c.wheels}")
# print(f"Does it has a rooftop: {c.has_roof}")

# print("=======================================")

# m=MotorCycle()
# m.specific_usage()
# print(f"Motorcycle has: {m.wheels} wheels")
# print(f"Does it has a rooftop: {m.has_roof}")


# try:
#     raise MemoryError("Memory Error.")
# except MemoryError as e:
#     print(e)


# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg=msg

#     def print_e(self):
#         print("Accident occured")


# try:
#     raise Accident("Two car crushed.")

# except Accident as e:
#     # e.print_e()
#     print(e)


a=["Nkaka","amakuru",2,"CMU","see"]

# for i in a:
#     print(i)

itr=iter(a)
print(next(itr))

