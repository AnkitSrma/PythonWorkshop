


def serviceQuality (quality):
    service = -1
    if (quality == 1):
        service = 0.99
    elif (quality == 2):
        service = 0.85
    elif (quality == 3):
        service = 0.70
    elif (quality == 4):
        service = 0.30
    elif (quality == 5):
        service = 0.15
    elif (quality == 6):
        service = 0
    elif (quality == 7):
        service = int(input("Enter the ratings in percent ( 0- 100)"))/100
    else:
        print("Enter valid response")

    return service



billed_amt = int(input("Enter the total billed amount: "))

print("Choose the following options which best describe quality of service provided by the waiter: ")
print("[1]: Excellent \n [2]: Very Good \n [3]: Good \n [4]: Satisfactory \n [5]: Bad \n [6]: Worst\n [7]: Rate yourself")
choice = int(input())
service_quality = serviceQuality(choice)

no_of_people_served = int(input("Enter no. of people served: "))

tip = (billed_amt * service_quality)/no_of_people_served

print("The tip per person is: {}".format(tip))


