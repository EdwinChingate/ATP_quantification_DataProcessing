from CalibrationCurveDF import *
from FillDataBaseCalibration import *
import pandas as pd
from datetime import datetime
import os
def MakeCalibrationDataBaseFromList(fileS,Folder=os.getcwd(),Save=0):  
    List=list(pd.read_csv(fileS,index_col=0)['0'])
    DFcalibration=CalibrationCurveDF()
    for x in List:
        file=Folder+'/'+x
        DFcalibration=FillDataBaseCalibration(file=file,DFcalibration=DFcalibration)
    DFcalibration=DFcalibration.sort_index()
    if Save!=0:
        Today=datetime.today().strftime('%Y-%m-%d')
        DFcalibration.to_excel('CalibrationCurveATP-'+Save+'-Processed'+Today+'.xlsx')
