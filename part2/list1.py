import itertools
'''This is a simple project in python. it talks about game and it touches little bit about 
datastructure i-e list''' 

def game_board(game,player=0,row=0,col=0,just_display=False): 
    try:
        if game[row][col]!=0:
           print("The postion is occupied.Try again.")
           return game,False
        if not just_display:
            game[row][col]=player
        print("   0  1  2")
        for idx,row in enumerate(game):
            print(idx,row)  
        return game,True
    except IndexError as e:
        print("you played on unavailable slot kindly use(0,1 and 2)") 
        return game,False
    except Exception as e:
        print("Something went wrong!",e) 
        return game,False


#  detecting a winner  

def win(game):

    for row in game: 
        # horizontal winner
        if row.count(row[0])==len(row) and row[0]!=0:
            print("Congraturation you won horizontally.")   

    for col in range(len(game)):
        # vertical winner
        cols=[] 
        for row in game:
            cols.append(row[col]) 
        if cols.count(row[0])==len(cols) and cols[0]!=0:
            print("Congz you won Vertically")
      
    diags=[]
    for idx,row in enumerate(range(0,len(game))):
        diags.append(game[idx][row])  

    if diags.count(diags[0])==len(diags) and diags[0]!=0:
        print("Congraturation, you win diagonal left.")  
       
    diag=[]
    for idx,row in enumerate(reversed(range(0,len(game)))):
        diag.append(game[idx][row])  

    if diag.count(diag[0])==len(diag) and diag[0]!=0:
        print("Congraturation, you won diagonal right.")  

play=True 
players=[1,2] 
while play: 
    game=[[0,0,0],
          [0,0,0],
          [0,0,0]] 
    game_won=False  
    game,_=game_board(game,just_display=True)
    player_choice=itertools.cycle(players)
    while not game_won:
       current_player=next(player_choice) 
       print(f"Current play {current_player}")
       played=False 
       while not played:
           try:
                row=int(input("Enter row you want to play(0,1,2): ")) 
                col=int(input("What is the column you want to play(0,1,2): ")) 
                game,played=game_board(game,current_player,row,col)  
           except Exception as e:
                print("Please use 0,1 and 2",)
       if win(game):
           game_won=True 
           again=input("Do you want to play again?(y/n): ") 
           if again=="y":
               print("restarting") 
           elif again=="n":
                print("Game Over!")
                play=False 
           else:
                print("Not a valid answer type y or n.")
                play=False 
                








    




    
    