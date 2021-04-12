# stock_prize=[]
# with open("files\stock.csv","r") as f:
#     for line in f:
#         tokens=line.split(',')
#         day=tokens[0]
#         price=float(tokens[1])
#         stock_prize.append([day,price])

# for l in stock_prize:
#     if l[1]==345:
#         print(l[0])

# stock_prize={}
# with open("files\stock.csv","r") as f:
#     for line in f:
#         tokens=line.split(',')
#         day=tokens[0]
#         price=float(tokens[1])
#         stock_prize[day]=price


# print(stock_prize["6-Mar"])


# def hash_func(key):
#     h=0
#     for char in key:
#         h+=ord(char)
#     return h%100 

# print(hash_func("nkaka"))

# class HashTable:
#     def __init__(self):
#         self.Max=100
#         self.arr=[None for i in range(self.Max)]

#     def hash_func(self,key):
#         key=key.casefold()
#         h=0
#         for char in key:
#             h+=ord(char)
#         return h%self.Max

#     def __setitem__(self,key,value):
#         h=self.hash_func(key)
#         self.arr[h]=value 
#         return 

#     def __getitem__(self,key):
#         h=self.hash_func(key)
#         print(self.arr[h])

#     def __delitem__(self,key):
#         h=self.hash_func(key)
#         self.arr[h]=None

# t=HashTable()
# t["march 6"]="Nkaka"
# t["march 10"]=100
# t["march 9"]=8975
# t["march 28"]=1000000
# # print(t.arr)
# del t["March 28"]
# t["march 28"]

# print(t.hash_func("march 6"))


class Hash_table:
    def __init__(self):
        self.Max=100
        self.arr=[[] for i in range(self.Max)]

    def hash_keys(self,key):
        key=key.lower()
        h=0
        for char in key:
            h+=ord(char)
        return h%self.Max

    def __setitem__(self,key,value):
        ha=self.hash_keys(key)
        found=False
        for idx,element in enumerate(self.arr[ha]):
            if len(element)==2 and element[0]==key:
                self.arr[ha][idx]=(key,value)
                found=True
                break
        if not found:
            self.arr[ha].append((key,value))
        
    def __getitem__(self,key):
        h=self.hash_keys(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self,key):
        h=self.hash_keys(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]
              


ht=Hash_table()
ht["nkaka"]="Never again genocide"
ht["nkaka"]="Yes I got updated now"
ht["march 6march 6"]="Hello my people"
# ht["march 6march 6"]=1746463
del ht["nkaka"]

print(ht.arr)



