game=[[0,0,0],
      [0,0,0],
      [0,0,0]]

def game_board(player=0,row=0,column=0,display=False):
    print("   a  b  c")
    if not display:
         game[row][column]=player
    for index,row in enumerate(game,start=1):
        print(index,row)


game_board(just_display=False)
game_board(player=1,row=2,column=1,just_display=True)


# x=game_board
# x()
print("==============")
# game[0][1]=1
# game[2][1]=1
# x()

# for row in game:
#     # print(row)
#     for item in row:
#         print(item)