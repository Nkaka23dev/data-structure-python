import itertools
def win(game_map):
    def all_inone(l):
        if l.count(l[0])==len(game_map) and l[0]!=0:
            return True
        else:
            return False
    #horizontal winner
    for row in game_map:
        if all_inone(row):
            print("Game won horizontally.")
            return True
    #vertical winner
    for col in range(len(game_map)):
        check=[]
        for row in game_map:
            check.append(row[col])
        if all_inone(check):
            print("Game won Vertically")
            return True
    #diagonally winned
    check=[]
    for col,row in enumerate(range(len(game_map))):
        check.append(game_map[row][col])
    if all_inone(check):
        print("Game is won diagonally")
        return True

    check=[]
    for col,row in enumerate(reversed(range(len(game_map)))):
        check.append(game_map[row][col])
    if all_inone(check):
        print("Game is won diagonally")
        return True

    
def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
        if game_map[row][column]!=0:
            print("This place is occupied.")    
            return game_map,False
        print("   0  2  3")
        if not just_display:
            game_map[row][column]=player
        for index,row in enumerate(game_map):
            print(index,row)  
        return game_map,True      
    except IndexError as e:
        print("Index out of range,Try agin",e)
        return game_map,False
    except Exception as e:
        print("Error ocuured,Try again.",e)
        return game_map,False
      
    
# game_board(game_map,player=1,row=1,column=1)

play=True
players=[1,2]
while play:
    game_map=[[0,0,0],
              [0,0,0],
              [0,0,0]]
    game_won=False
    player_=itertools.cycle(players)
    game_map,_=game_board(game_map,just_display=True)
   
    while not game_won:
        current_player=next(player_)
        print(f"Current player:{current_player}")
        played=False
        while not played:
            row_choice=int(input("Which row do you want to play?(0,1,2): "))
            column_choice=int(input("Which column do you want to play?(0,1,2): "))
            game_map,played=game_board(game_map,player=current_player,row=row_choice,column=column_choice)
        if win(game_map):
            game_won=True
            cont=input("Do you want to continue?(y/n): ")
            if cont.casefold()=='y':
                print("Restarting...........")
            elif cont.casefold()=='n':
                play=False
                print("Byeeeeeee.......")
            else:
                print("Not a valid answer,Please try again.")
                play=False





    