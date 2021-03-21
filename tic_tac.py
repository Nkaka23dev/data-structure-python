
def game_board(game_map,player=0,row=0,column=0,display=False):
    try:
        print("   a  b  c")
        if not display:
            game[row][column]=player
        for index,row in enumerate(game,start=1):
            print(index,row)
    except IndexError as e:
        print("Error:make sure you input row/column between 0,1 and 2?!",e)
    except Exception as e:
        print("Something went very bad!!",e)
    else:
        pass
    finally:
        pass

game=[[0,0,0],
      [0,0,0],
      [0,0,0]]

# game_board(game,display=False)
game_board(game_r,player=1,row=1,column=1,display=False)


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