def voting_system(nominee_1,nominee_2):
    nm1_vote=0
    nm2_vote=0

    voters=[1,2,3,4,5]
    length=len(voters)
    voting=True
    while voting:
        try:
            if voters==[]:
                if nm1_vote>nm2_vote:
                    percent=(nm1_vote/length)*100
                    print("---------------------------------------------")
                    print(f"{nominee_1} has won election with {percent}%")
                    print("Election is now over...........")
                    break
                elif nm2_vote>nm1_vote:
                    percent=(nm2_vote/length)*100
                    print("---------------------------------------------")
                    print(f"{nominee_2} has won election with {percent}%")
                    print("Election is now over...........")
                    break
                else:
                    print("They got the same vote.")
                    print("Election is now over...........")
                    break
        
            voter_id=int(input("Enter your ID to vote: "))
            if voter_id in voters:
                print("You are now a voter")
                print("---------------------------------")
                print(f"Use 1 to vote for {nominee_1}")
                print(f"Use 2 to vote for {nominee_2}")
                print("=================================")
                vote=int(input("Enter a vote here(1 or 2): "))
                if vote==1:
                    nm1_vote+=1
                    print(f"Successfully vote for {nominee_1} received")
                elif vote==2:
                    nm2_vote+=1
                    print(f"Your vote for {nominee_2} successfully received.")
                else:
                    print("Please use 1 or 2")
                voters.remove(voter_id)
            else:
                print("You have voted or you are not on the list.")
        except Exception as e:
            print("Error Occured",e)
        
        
nom1=input("Enter the first candidate: ")
nom2=input("Ente the second candidate: ")
voting_system(nom1,nom2)