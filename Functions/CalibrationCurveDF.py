import numpy as np
import pandas as pd
def CalibrationCurveDF():    columns=['Intercept','Slope','CoefficientofDetermination','MinSt','MaxSt','LimitofDetection','LimitofQuantification','Researcher','FirstMass(mg)','MolecularWeightSt(Da)','FirstVolume(mL)','InitialConcentration(uM)','FirstDilution']
    Standards=[]
    StandardsC=[]
    for x in np.arange(1,7):
        Standards.append('ST'+str(x))
        StandardsC.append(1/5**(x-1))
    columns=Standards+columns
    df=len(columns)*['-']
    DF=pd.DataFrame(data=df,index=columns,columns=['DilutionsS']).transpose()
    DF[Standards]=np.array(StandardsC)    
    return DF
