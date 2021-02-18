import hashlib
# print(hashlib.sha1(b"Nobody inspects the spammish repetition").hexdigest())

def hash_text(filename):
    ha=hashlib.sha1()
    with open(filename,"rb") as my_file:
        chunk=0
        while chunk!=b'':
            chunk=my_file.read(1024)
            ha.update(chunk)
    return ha.hexdigest()

print(hash_text("files/nkaka.txt"))



