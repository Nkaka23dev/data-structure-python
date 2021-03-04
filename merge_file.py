# this is the program to merge files by multiplicating them into many.

with open("files/nkaka2.txt","r") as cont:
    read=cont.read()
    with open("files/names.txt","r") as names:
        for name in names:
            message="Hello "+name.strip()+" consider the following.\n"+read
            with open('files'+'/'+name.strip()+'.txt','w') as new_f:
                new_f.write(message)
            