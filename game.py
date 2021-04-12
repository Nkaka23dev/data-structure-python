game_board=[[0,0,1],
            [0,1,1],
            [0,0,0]]


# winner horizontally.
for row in game_board:
    if row.count(row[0])==len(row) and row[0]!=0:
        print("Game won horizontally.")
   
# winner vertically

check=[]




def game_map(game_board,player=None,row=None,column=None,just_display=False):
    try:
        if not just_display:
            game_board[row][column]=player
        
        for row in game_board:
            print(row)
    except IndexError as e:
        print("Error!",e)
    except Exception as e:
        print("Error occured!",e)
        
    
# game_map(game_board,player=2,row=1,column=0)
