# # this is the first method of sorting words alphabetically.
# text="Hello nkaka are you doing good tell us bro."

# new_text=[]

# for t in text.split(' '):
#     new_text.append(t.casefold())


# new_text.sort(reverse=True)
# print(new_text)
# end of first method

# second method of sorting words alphabetically using list comprehension

text=input("Enter words to sort alphabeticall: ")

def sort_words(text):
    text=text.casefold()
    new_text=[t for t in text.split(' ')]
    new_text.sort()
    return new_text

print(sort_words(text))

    

