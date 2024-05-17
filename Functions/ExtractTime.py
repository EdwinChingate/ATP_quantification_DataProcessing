from CutW import *
def ExtractTime(DFATP):
    c=0   
    for x in DFATP.columns:
        if sum(DFATP[x]=='End Time:')>0:
            rowDate=int(DFATP[x][DFATP[x]=='End Time:'].index[0])            
            FullDate='d'+DFATP.loc[rowDate][c+1]
            break
        c=c+1
    FullD=FullDate.replace(' ','_')
    FullD=FullD.replace('/','-')
    Day=(CutW(FullDate,'/','/'))    
    FullDate=FullDate.replace('/'+Day+'/','/')
    Year=int(CutW(FullDate,'/',' '))   
    Month=int(CutW(FullDate,'d','/'))    
    Day=int(Day)
    Late=FullDate[-2:]
    Hour=int(CutW(FullDate,' ',':'))
    Minute=int(CutW(FullDate,':',':'))    
    if Late=='PM' and Hour<12:
        Hour=Hour+12
    return [Year,Month,Day,Hour,Minute,FullD]
