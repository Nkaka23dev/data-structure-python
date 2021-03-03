import hashlib 

def hash_file(filename):
    hash_file=hashlib.sha1()
    with open(filename,'rb') as my_file:
        chunk=0
        while chunk!=b'':
            chunk=my_file.read(1024)
            hash_file.update(chunk)
    return hash_file.hexdigest()

x=input("enter the path of file1: ")
y=input("Enter the second path: ")
file1=hash_file(x)
file2=hash_file(y)
if file1==file2:
    print("these are two file with the same content and different name.")
else:
    print("two files with different content.")

print("====================================================================")
print(file1)
print(file2)