import numpy as np
import pandas as pd
def EmptySumRawTable(SamplesNumber=1):    
    columns=['Researcher','Year','Month','Day','Hour','Minute','Time(days)','Row','Column','SampleInternalID','SampleType','Reactor','Origin','Replicate','Luminescence','Use']
    fil=np.zeros((SamplesNumber,len(columns)))
    DF=pd.DataFrame(data=fil.copy(),columns=columns)
    return DF
    
