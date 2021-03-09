def prime(num1,num2):
    for i in range(num1,num2+1):
        if num1>1 and num2>1:
            if i%2!=0:
                print(i)

prime(900,1000)