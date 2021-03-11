words=input("Enter a text to count vowels: ")

def vowel_counter(words):
    vowels="aeiou"
    words=words.casefold()
    counter=dict.fromkeys(vowels,0)
    for char in words:
        if char in vowels:
            counter[char]+=1
    return counter

print(vowel_counter(words))