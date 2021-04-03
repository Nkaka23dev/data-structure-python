import itertools
def win(game_board):
    def all_row(l):
        if l.count(l[0])==len(l) and l[0]!=0:
            return True 
        else:
            return False

    # horizontal winner
    for row in game_board:
        if all_row(row):
            print("Game won horizontally")
            return True

    #Vertical winner
    for row in range(len(game_board)):
        check=[]
        for col in game_board:
            check.append(col[row])
        if all_row(check):
            print("Game won vertically")
            return True

    # diagonal winner
    check=[]
    for index,row in enumerate(range(len(game_board))):
        check.append(game_board[index][row])
    if all_row(check):
        print("Game won diagonally up")
        return True

    check=[]
    for index,row in enumerate(reversed(range(len(game_board)))):
        check.append(game_board[row][index])
    if all_row(check):
        print("Game won diagonally down")
        return True


def game_map(game_board,player=0,row=0,column=0,just_display=False):
    try:
        if game_board[row][column]!=0:
            print("The place is occupied. Try again.")
            return game_board,False

        if not just_display:
            game_board[row][column]=player    
        print('   0  1  2')
        for index,row in enumerate(game_board):
            print(index,row)
        return game_board,True

    except IndexError as e:
        print("Invalid index,Choose between 0,1 and 2",e)
        return game_board,False
    except Exception as e:
       print("Error Occured! Try again Please.",e)
       return game_board,False

play=True
players=[1,2]

while play:
    game_board=[[0,0,0],
                [0,0,0],
                [0,0,0]]
    game_won=False
    game_map(game_board,just_display=True)
    player_choice=itertools.cycle(players)
    while not game_won:
        current_player=next(player_choice)
        print("Current player is player: {}".format(current_player))
        played=False
        while not played:
            try:
                row=int(input("Enter a row you want to play(0 1 2): "))
                column=int(input("Which column do you want to play(1 2 3): "))
                game_board,played=game_map(game_board,current_player,row,column)
            except Exception as e:
                print("Only numbers between 0,1 and 2 are allowed.")
            if win(game_board):
                game_won=True
                print("=====================")
                print("Game Over")
                print("======================")
                cont=input("Do you want to continue the game(y/n): ")
                if cont.casefold()=='y':
                    print("^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("Restarting the game......")
                    play=True
                elif cont.casefold()=='n':
                    print('Thank you for playing TIC TAC TOE, Byeeeeeeeeeeeeeee....')
                    play=False
                else:
                    print("Not a valid answer......see next time.........")
                    


    
            

    





