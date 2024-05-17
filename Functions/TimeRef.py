from MonthstoDays import *
def TimeRef(TimeV,Ref=[2021,1,0,0,0]):
    DaysBeforeTV=MonthstoDays(TimeV[1])+TimeV[2]-1+TimeV[3]/24+TimeV[4]/1440
    DaysBeforeRef=MonthstoDays(Ref[1])+Ref[2]-1+Ref[3]/24+Ref[4]/1440
    Days=365*(TimeV[0]-Ref[0])+(DaysBeforeTV-DaysBeforeRef)
    return float(Days)
