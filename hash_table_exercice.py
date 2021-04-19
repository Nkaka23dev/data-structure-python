class Hash:
    def __init__(self):
        self.Max=100
        self.arr=[[] for i in range(self.Max)]

    def hash_key(self,key):
        key=key.casefold()
        h=0
        for char in key:
            h+=ord(char)
        return h%self.Max

    def __setitem__(self,key,value):
        key=key.casefold()
        found=False
        ha=self.hash_key(key)
        for idx,element in enumerate(self.arr[ha]):
            if len(element)==2 and element[0]==key:
                self.arr[ha][idx]=(key,value)
                found=True
                break
        if not found:
            self.arr[ha].append((key,value))

    def __getitem__(self,key):
        key=key.casefold()
        ha=self.hash_key(key)
        for element in self.arr[ha]:
            if len(element)==2 and element[0]==key:
                print(element[1])
                break
        
    def __delitem__(self,key):
        key=key.casefold()
        ha=self.hash_key(key)
        for idx,element in enumerate(self.arr[ha]):
            if element[0]==key:
                del self.arr[ha][idx]
                break


h=Hash()
h["nkaka"]="My name is Nkaka."
h["nkaka"]=1000000000000000
# h["nkaka"]="Ndumiwe"
h["march 6march 6"]=6346765
del h["march 6march 6"]
print(h.arr)
h['march 6march 6']
h['Nkaka']









