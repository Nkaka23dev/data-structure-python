# exercices from data structure and algorithm from codebasics on youtube

exp=[2200,2350,2600,2130,2190]
#1
# extra_spent=exp[1]-exp[0]
# print(extra_spent)

# #2
# # total in first quarter
# # total=0
# # for i in exp[:3]:
# #     total+=i
# tot=exp[0]+exp[1]+exp[2]
# print(tot)

# # 3
# # if we have spent exactly 2000 in any month

# # for i in exp:
# #     if i==2000:
# #         print(True)
# print(2000 in exp)

#June month just finished and your expense is 1980 dollar.
# Add this item to our monthly expense list

# exp.append(1980)
# print(exp)

#  You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on th

# exp[3]=exp[3]-200
# print(exp)
  

heros=['spider man','thor','hulk','iron man','captain america']
# # 1. Length of the list
# print(len(heros))

# #2. Add 'black panther' at the end of this list
# heros.append("black panther")
# print(heros)

#3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# heros.remove(heros[-1])
# heros.remove("black panther")
# print(heros)

# # 4. Now you don't like thor and hulk because they get angry easily :)
# #    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# #    Do that with one line of code.

# heros[1:3]=["Doctor strange"]
# print(heros)

# #Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
# heros.sort(reverse=True)
# print(heros)

# 3 Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function


# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

numbers=int(input("Enter a maximum number: "))
print([i for i in list(range(1,numbers+1)) if i%2!=0])

# print(list(map(lambda x:x**2,list(range(1,numbers+1)))))




   
    