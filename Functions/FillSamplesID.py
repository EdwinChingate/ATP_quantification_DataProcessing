def FillSamplesID(CleanTable,SumTab):
    c=0
    for y in CleanTable.index:
        for x in CleanTable.columns:
            Content=CleanTable[x][y]
            if Content!=0:
                Content=Content.replace(' ','')
                Content=Content.replace('uM','')
                SumTab.loc[c,'SampleInternalID']=Content  
                SumTab.loc[c,'Row']=y
                SumTab.loc[c,'Column']=x
                if str(Content)[0]=='S' or str(Content)[0]=='B':
                    SumTab.loc[c,'SampleType']='Standard'
                    SumTab.loc[c,'Reactor']=Content[-1]
                else:
                    SumTab.loc[c,'SampleType']='Sample'
                    SumTab.loc[c,'Origin']=Content[1]
                    SumTab.loc[c,'Reactor']=Content[0]
                    while True:
                        try:
                            SumTab.loc[c,'Replicate']=Content[2]
                            break
                        except:
                            SumTab.loc[c,'Replicate']=1
                            break
                c=c+1       
    SumTab['Use']=1
