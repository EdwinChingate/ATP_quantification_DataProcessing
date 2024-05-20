import pandas as pd
import numpy as np
from CutW import *
def FillDataBaseCalibration(StructuratedLumin='',file='',MinSt=5,MaxSt=0,DFcalibration=CalibrationCurveDF(),MolecularWeightSt=551.1,FirstMass=6.889,FirstVolume=25,FirstDilution=500):
    if StructuratedLumin=='':
        DF=pd.read_excel(file,index_col=0)
    else:
        DF=StructuratedLumin
    columns=DFcalibration.columns
    fileID=str(CutW(file,'/d','.xlsx'))
    df=np.zeros((1,len(columns)))
    DFCal=pd.DataFrame(data=df,index=[fileID],columns=columns)
    InitialConcentration=FirstMass/(MolecularWeightSt*FirstVolume)*1e6
    DFCal.loc[fileID,['MolecularWeightSt(Da)','FirstMass(mg)','FirstVolume(mL)','FirstDilution','InitialConcentration(uM)','MinSt','MaxSt']]=[MolecularWeightSt,FirstMass,FirstVolume,FirstDilution,InitialConcentration,MinSt,MaxSt]
    DFCal.iloc[0,:6]=DF[DF['SampleType']=='Standard']['Luminescence'][:6]
    DFcalibration=DFcalibration.append(DFCal)
    return DFcalibration
