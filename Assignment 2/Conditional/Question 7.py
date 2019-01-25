import re
x= input("Your password: ")
y= True
while y:  
    if (len(x)<6 or len(x)>12):
        break
    elif not re.search("[a-z]",x):
        break
    elif not re.search("[0-9]",x):
        break
    elif not re.search("[A-Z]",x):
        break
    elif not re.search("[$#@]",x):
        break
    elif re.search("\s",x):
        break
    else:
        print("It's a Valid Password")
        y=False
        break

if y:
    print("It's not a Valid Password")

