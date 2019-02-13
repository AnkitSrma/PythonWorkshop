
#Marriage Point Calculator in Python
value_point = int(input("Enter the value of point= Rs. "))
total_maal = int(input("Enter the maal: "))
seejoker = int(input("Enter '1' in the case you see the joker and '0' elsewise "))
if seejoker == 0:
    net_loss = value_point * (total_maal + 10)
    print("You have to pay total = Rs. {net_loss}")
else:
    num_playercont = int(input("Enter the total number of players: "))
    maal = int(input("Enter your maal: "))
    net_loss = ((total_maal + 3) - (maal * num_playercont)) * value_point
    if net_loss < 0:
        print("You won: Rs. {net_loss * -1}")
    else:
        print("you have to pay a total of : Rs. {net_loss}")