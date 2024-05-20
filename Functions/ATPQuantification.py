import pandas as pd
import numpy as np
from EmptySumRawTable import *
def ATPQuantification(CalCurFile='',name='',Folder=os.getcwd(),Save=0):
    if CalCurFile=='':
        CalCurDB=pd.read_excel(name,index_col=0)
    else:
        CalCurDB=CalCurFile
        if CalCurFile=='':
            return 0    
    DF=EmptySumRawTable(SamplesNumber=1)
    DF.index=['Del']
    for x in CalCurDB.index[1:]:
        mDF=len(DF.index)
        file=Folder+'/'+x+'.xlsx'
        DFn=pd.read_excel(file,index_col=0)
        DFn=DFn[DFn['SampleType']=='Sample']
        indexDFn=DFn.index                
        DFn.index=np.arange(mDF,len(indexDFn)+mDF)
        Slope=CalCurDB.loc[x,'Slope']
        Intercept=CalCurDB.loc[x,'Intercept']
        DFn['ATPConc(nM)']=(DFn['Luminescence']-Intercept)/Slope*1000
        DF=DF.append(DFn)        
    DF=DF.drop('Del')
    DF=DF.sort_values(by='Time(days)')
    if Save!=0:
        FinName=name.replace('CalibrationCurveATP-','')
        DF.to_excel(FinName)
    return DF
