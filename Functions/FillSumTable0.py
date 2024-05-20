import numpy as np
import pandas as pd
from CleanATPTable import * 
from EmptySumRawTable import * 
from FillSamplesID import * 

def FillSumTable0(FileName,SumTab=0):
    Data0=pd.ExcelFile(FileName)
    Sheet=[] 
    Samples=0
    for x in Data0.sheet_names:
        while True:
            try:
                RawTable=pd.read_excel(FileName,sheet_name=x)                
                if sum(sum(np.array(RawTable=='Time:')))==1: #Stores the sheets names with experimental data
                    Sheet.append(x)                    
                else: #Extracts the samples names from the sheet with the samples distribution                    
                    CleanTable=CleanATPTable(RawTable)
                    AllWell=CleanTable.shape[0]*CleanTable.shape[1]
                    EmptyWell=sum(sum(np.array(CleanTable==0)))
                    Samples=AllWell-EmptyWell
                    SumTab=EmptySumRawTable(Samples)
                    FillSamplesID(CleanTable,SumTab)
                break
            except: 
                print('error with: ',FileName,' ',x)
                break
    return [Sheet,SumTab,Samples]
    
   
