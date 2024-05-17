def RecordedRows(DFATP):
    PlateRows=['A','B','C','D','E','F','G','H']
    Recorded=[]
    for x in PlateRows:
        if sum(DFATP.index==x)>0:
            Recorded.append(x)
    return DFATP.loc[Recorded]  
