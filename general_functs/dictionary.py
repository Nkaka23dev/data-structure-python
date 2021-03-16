posts={
    "author":"Nkaka Eric",
    "title":"Greetings",
    "body":"Hello all my people how are you.",
    "posted_date":"26 June 2020"
}

# #two ways of getting value assigned to a certain key.
# print(posts['author'])
# print(posts.get('title'))

# #getting all keys or values
# print(posts.keys())
# print(posts.values())

# #adding and modifying key and value
# posts["author"]="Shyaka willy"
# posts["viewers"]=["Nkaka,eric","Kubwimana Mourice","Kazitunga"]
# print(posts.keys())

#getting keys and value at the same time use items()
# print(posts.items())

#Removing items we have pop(),popitem() and del
# print(posts.pop("author"))
# print(posts)

# #this remove the last item
# print(posts.popitem())
# print(posts)

# #delete or clear all items of the list
# del posts
# posts.clear()
# print(posts)

# # loop in dictionary
# for key,post in posts.items():
#     print(key+":"+post)

# # copying dictionary
# new_post=posts
# print(new_post)
#or 
copied=posts.copy()
print(copied)