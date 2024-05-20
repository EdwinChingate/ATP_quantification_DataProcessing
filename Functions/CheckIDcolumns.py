import pandas as pd
from RemoveColumns import *
def CheckIDcolumns(DFATP): #In case the table was moved
    Columns0=DFATP.columns
    Columns=pd.DataFrame(Columns0,columns=['Col'])
    if sum(Columns['Col']=='<>')>0:
        ColId=Columns[Columns['Col']=='<>'].index[0]
    else:
        c=0
        for x in Columns0:
            if sum(DFATP[x]=='<>')>0:
                ColId=c
                break
            c=c+1    
    DFATPClean=RemoveColumns(DFATP,Columns0,ColId)
    return DFATPClean  
