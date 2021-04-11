stock_prize=[]
with open("files\stock.csv","r") as f:
    for line in f:
        tokens=line.split(',')
        day=tokens[0]
        price=float(tokens[1])
        stock_prize.append([day,price])

for l in stock_prize:
    if l[1]==345:
        print(l[0])

stock_prize={}
with open("files\stock.csv","r") as f:
    for line in f:
        tokens=line.split(',')
        day=tokens[0]
        price=float(tokens[1])
        stock_prize[day]=price


print(stock_prize["6-Mar"])