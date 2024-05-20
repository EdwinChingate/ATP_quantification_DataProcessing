import numpy as np
import pandas as pd
from FillSumTable0 import *
from ExtractTime import *
from TimeRef import *
from CleanATPTable import *

def FillTable(FileName):
    Fill0=FillSumTable0(FileName)
    Sheet=Fill0[0]
    SumTab=Fill0[1]
    SumTabFinal=SumTab.copy()
    Samples=Fill0[2]
    Tsam=[0.0,Sheet[0],'',SumTab.copy()]    
    c=0
    for x in Sheet:
        k=0
        while True:
            try:
                SumTab=Fill0[1]
                RawTable=pd.read_excel(FileName,sheet_name=x)
                Time=ExtractTime(RawTable)
                tref=TimeRef(Time)
                CleanTable=CleanATPTable(RawTable) 
                for s in np.arange(Samples):        
                    Row=SumTab.loc[s,'Row']
                    Column=SumTab.loc[s,'Column']
                    SumTab.loc[s,'Luminescence']=CleanTable.loc[Row,Column]                
                SumTab['Year']=Time[0]
                SumTab['Month']=Time[1]
                SumTab['Day']=Time[2]
                SumTab['Hour']=Time[3]
                SumTab['Minute']=Time[4]
                SumTab['Time(days)']=TimeRef(Time)         
                if tref>Tsam[0]:
                    Tsam=[tref,x,Time[5],SumTab.copy()]                
                c=c+1
                break
            except:   
                print(FileName,x)
                k=1
                break
    return [Tsam[2],Tsam[3]]
