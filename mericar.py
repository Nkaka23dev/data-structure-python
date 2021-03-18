
# def findNumber(arr,k):
#     if k<=0 or k>=10*5:
#         raise ValueError("Not allowed")
#     if len(arr)<=0 or len(arr)>=10*9:
#         raise ValueError("index??")

#     while k in arr:
#        print("yes")
#        break
#     while k not in arr:
#         print("No")
#         break
            
        

# arr=[1,3,4,5,7]
# number=4
# if __name__=='__main__':
#     findNumber(arr,number)

def oddNumbers(l, r):
    # Write your code here
    arr=[]
    if l<=0 or l<=10*5:
        print("invalid input")
    if r<=0 or r>=10*5:
        print("Invalid r")
    if  l>=r:
        print("not allowed")
    for i in list(range(l,r)):
        if i%2!=0:
            print(i,end=' ')
 
oddNumbers(1,9)