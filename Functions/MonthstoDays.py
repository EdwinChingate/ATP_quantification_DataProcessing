def MonthstoDays(m,d=0):
    if m==0:
        return d
    if d==0:
        m=m-1
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        d=d+31
    elif m==2:
        d=d+28
    elif m==0:
        return d
    else:
        d=d+30
    return MonthstoDays(m-1,d)
