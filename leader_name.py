# Task to register leader name who want to participate in election
leader = []
for i in range(1, 6):
    leader_name = input("Enter your leader name :")
    leader.append(leader_name)
    n = len(leader)
    if n < 5 :
        print("You have been successfully registerd")
    else :
        print("Maximum candidate have been enrolled")