def RemoveColumns(DFATP,Columns0,ColId):
    DFATP.index=DFATP[Columns0[ColId]]
    DFATPClean=DFATP.drop(Columns0[:ColId+1],axis=1)
    return DFATPClean
