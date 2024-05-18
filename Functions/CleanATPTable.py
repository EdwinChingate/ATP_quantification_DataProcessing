from RecordedRows import * #
from CheckIDcolumns import * #
def CleanATPTable(DFAT):    
    DFATP=DFAT.copy()
    if sum(DFATP.index=='<>')+sum(DFATP.index=='A')==0:
        DFATP=CheckIDcolumns(DFATP)
    if sum(np.array(DFATP=='A'))>1:
        return 0
    ATPTable=pd.DataFrame(RecordedRows(DFATP))
    ATPTable=ATPTable[ATPTable.columns[:12]]
    ATPTable.columns=np.arange(1,13)   
    ATPTable=ATPTable.fillna(0)
    return ATPTable
