phrase=input("Enter a phrase with a lot of punctuations: ")

def remove_puct(phrase):
    punc=''',.<>'/?;:"{}[]=+-_)(*&^%$#@!~`'''
    new_phrase=""
    for p in phrase:
        if p not in punc:
            new_phrase=new_phrase+p
    return new_phrase

print(remove_puct(phrase))