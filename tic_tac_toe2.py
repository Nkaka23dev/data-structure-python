game=[[1,0,4],
      [0,6,4],
      [1,3,4]]

# Verical winner
for col in range(len(game)):
    check=[]
    for row in game:
        check.append(row[col])
    
    if check.count(check[0])==len(check):
        print("Winner!")


# #Horizontal winner
# for row in game:
#     if row.count(row[0])==len(row):
#         print("Winner!!")
#         break
#     else:
#         print("No winner")
#         break


# def win(current_game):
#     for index,row in enumerate(current_game,start=1):
#         print(row)
#         col1=row[0]
#         col2=row[1]
#         col3=row[2]
#         if col1==col2==col3:
#             print(f"{index} row  have won")

# win(game)



    