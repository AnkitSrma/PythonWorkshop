def disect(t):
    del t[0]
    if(len(t)-1>0):
        del t[len(t)-1]
        return t
