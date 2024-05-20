import pandas as pd
from scipy import stats
import numpy as np
def MakeCalibrationCurves(file='',name='',Save=0): #Better to take a simmilar approach as with the calibration curves for the TOrCs, so... check one by one... with the widgets!    
    if file=='':
        CalCurDB=pd.read_excel(name,index_col=0)
    else:
        CalCurDB=file
        if file=='':
            return 0
    CalCurDB['InitialConcentration(uM)'][1:]=1e6*CalCurDB['FirstMass(mg)'][1:]/CalCurDB['MolecularWeightSt(Da)'][1:]/CalCurDB['FirstVolume(mL)'][1:]
    minVal=6
    for x in CalCurDB.index[1:]:
        MinSt=CalCurDB.loc[x]['MinSt']
        MaxSt=CalCurDB.loc[x]['MaxSt']        
        ConvCon=float(CalCurDB.loc[x]['InitialConcentration(uM)'])/float(CalCurDB.loc[x]['FirstDilution'])
        ATPCon=np.log(list(ConvCon*CalCurDB.loc['DilutionsS'][MaxSt:MinSt]))
        ATPLum=np.log(list(CalCurDB.loc[x][MaxSt:MinSt]))
        print(x)
        reg=stats.linregress(ATPCon,ATPLum)  
        CalCurDB.loc[x,['Intercept','Slope','CoefficientofDetermination']]=[reg[1],reg[0],reg[2]**2]        
    if Save!=0:
        CalCurDB.to_excel(name)
