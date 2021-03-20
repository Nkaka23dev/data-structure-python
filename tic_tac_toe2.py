game=[[1,3,1],
      [3,1,4],
      [3,2,1]]

# horizontal winner
for row in game:
    if row.count(row[0])==len(row):
        print("horizontal winner!")

#vertical winner
for col in range(len(game)):
    check=[]
    for row in game:
        check.append(row[0])

    if check.count(check[0])==len(check):
        print("Vertical winner")

#diagonals winner
diags=[]
for i,row in enumerate(range(len(game))):
    diags.append(game[row][i])

if diags.count(diags[0])==len(diags): 
    print("Horizontal 1 winner.")

diag=[]
for i,row in enumerate(reversed(range(len(game)))):
    diag.append(game[row][i])
   
if diag.count(diag[0])==len(diag):
    print("Horizontal 2 winner")

 



















































































































































# diags=[]
# for col,row in enumerate(reversed(range(len(game)))):
#     diags.append(game[row][col])

# print(diags)

# diags=[]
# for ix in range(len(game)):
#     diags.append(game[ix][ix])

# print(diags)

# cols=list(reversed(range(len(game))))
# rows=range(len(game))

# for idx in rows:
#     print(idx,cols[idx])   

# diag=[]
# for ix in reversed(range(len(game))):
#     diag.append(game[ix][ix])

# print(diag)


# diags=[]
# for ix in range(len(game)):
#     diags.append(game[ix][ix])

# print(diags)

# # diagonal winner hard coded
# if game[0][0]==game[1][1]==game[2][2]:
#     print("Winner")

# if game[2][0]==game[1][1]==game[0][2]:
#     print("Winner again!")

# # Verical winner
# for col in range(len(game)):
#     check=[]
#     for row in game:
#         check.append(row[col])
    
#     print(check,end='')
#     if check.count(check[0])==len(check):
#         print("Winner!")

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



    