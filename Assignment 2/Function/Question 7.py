Q.Write a shutting down program:
Solution:
    
def shut_down(s):
    if s=="yes":
      return "Shutting down"
    elif s=="no":
          return "Shutdown aborted"
    return "Sorry"

print(shut_down(str(input())))
