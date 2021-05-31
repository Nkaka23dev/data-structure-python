# import itertools

# def win(game):
#     def all_same(l):
#         if l.count(l[0])==len(l) and l[0]!=0:
#             return True
#         else:
#             return False

#     # horizontal winner
#     for row in game:
#         if all_same(row):
#             print("horizontal winner!")
#             return True

#     #vertical winner
#     for col in range(len(game)):
#         check=[]
#         for row in game:
#             check.append(row[0])

#         if all_same(check):
#             print("Vertical winner")
#             return True
        
#     #diagonals winner
#     diags=[]
#     for i,row in enumerate(range(len(game))):
#         diags.append(game[row][i])

#     if all_same(diags):
#         print("Diagonal 1 won.")
#         return True

#     diag=[]
#     for i,row in enumerate(reversed(range(len(game)))):
#         diag.append(game[row][i])
    
#     if all_same(diag):
#         print("Diagonal 2 won")
#         return True

# def game_board(game,player=0,row=0,column=0,just_display=False):
#     try:
#         if game[row][column]!=0:
#             print("The postion is occupied.Try again.")
#             return game,False
#         print("   0  1  2")
#         if not just_display:
#             game[row][column]=player
#         for count,row in enumerate(game):
#             print(count,row)
#         return game,True
#     except IndexError as e:
#         print("Error:make sure you input row/column as 0,1 and 2!",e)
#         return game,False
#     except Exception as e:
#         print("Something went wrong.",e)
#         return game,False

# play=True
# players=[1,2]
# while play:
#     game=[[0,0,0],
#           [0,0,0],
#           [0,0,0]]
#     game_won=False
#     game,_=game_board(game,just_display=True)
#     player_choice=itertools.cycle(players)
    
#     while not game_won:
#         current_player=next(player_choice)
#         print(f"Current player {current_player}")
#         played=False
#         while not played:
#             try:
#                 row_choice=int(input("What row do you want to play?(0,1,2): "))
#                 column_choice=int(input("What column do you want to play?(0,1,2): "))
#                 game,played=game_board(game,current_player,row_choice,column_choice)
#             except Exception as e:
#                 print("Error occured try again.")  
#         if win(game):
#             game_won=True
#             again=input("Do you want to continue the game?(y/n): ")
#             if again.casefold()=='y':
#                 print("Restarting")
#             elif again.casefold()=='n':
#                 print("Byeeeeeeeeeee")
#                 play=False
#             else:
#                 print("Not a valid answer, so..... see you later.")
#                 play=False


