courses=["Math","English","Python","Java","Chemistry"]
# #Methods to add elements on the list are //append,//extend and //insert
# courses.extend(["Geograph","Physics","Biology","History"])
# # method to remove from the list are remove and pop()
# courses.remove('English')
# courses.pop()
# method to sort
# courses.sort(reverse=True)
# #sorting without altering the original list
# sorted_courses=sorted(courses)
# print(sorted_courses)
# print(courses.index("Java"))
# print(courses)

# # looping into the list and searching into the list
# print("English" in courses) 

# for course in courses:
#     print(course)

# for index,course in enumerate(courses,start=1):
#     print(index,course)

## spliting and joining list items

# course_str='/'.join(courses)
# course_spl=course_str.split('/')
# print(course_str)
# print(course_spl)
# print(courses)

numbers=[12,4,3,6,9,65,22,56,8,0,2,13,567,543]
#you can use max,min and sum
# print(max(numbers))
# print(numbers[4:])

# #Turning a range into a list
# x=list(range(1,10))
# y=list("Nkaka")
# print(y)
# print(sum(x))

# exercice 1

# import statistics

# my_nums=list(range(12,19))
# avg=statistics.mean(my_nums)
# # print([num**2 for num in my_nums])
# # print(list(map(lambda x:x**2,my_nums)))
# yy=list(filter(lambda x:x<avg,my_nums))
# print(yy)

def voting_system(nominee_1,nominee_2):
    nm1_votes=0
    nm2_votes=0

    voters=[1,2,3,4,5]

    voters_size=len(voters_id)

    while True:
        voter_id=int(input("Enter your ID number to vote: "))
        if voter_id in voters:
            voters.remove(voter_id)
            print("You are a voter now")
            print("================================")
            print(f"Enter 1 to vote for {nominee_1}")
            print(f"Enter 2 to vote for {nominee_2}")
            print("=================================")
            vote=int(input("Enter a vote here: "))
            if vote==1:
                nm1_votes+=1
            elif vote==2:
                nm2_votes+=1
            else:
                print("You entered a wrong key,Please try again.")
        else:
            
        

nominee_1=input("Enter first nominee: ")
nominee_2=input("Enter nominee two: ")

