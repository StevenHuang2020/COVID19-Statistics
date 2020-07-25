#python3 unicode
#author:Steven Huang 07/25/20
#function: Query NZ COVID-19 from https://www.health.govt.nz/
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#usgae:
#python .\mainNZ.py
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotCoronavirous import gSaveBasePath

#reference: https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases
#https://www.health.govt.nz/system/files/documents/pages/covid-cases-24july20.xlsx

def readExcel(file,sheetname=0,header=3,verbose=False):
    df = pd.read_excel(file,sheet_name=sheetname,header=header)
    print(type(df),'df.shape=',df.shape)
    
    if verbose:
        print(df.describe().transpose())
        print(df.head())
        #df.set_index(["Location"], inplace=True)
        print('df.columns=',df.columns)
        print('df.dtypes = ',df.dtypes)
        #df = df.apply(pd.to_numeric, axis=0)
        #print('df.dtypes = ',df.dtypes)
    return df

def plotStatistcs(df,title):
    fontsize = 8
    
    kind='bar'
    # if df.shape[0]>25:
    #     kind='barh'
            
    ax = df.plot(kind=kind,legend=False) #color='gray'
    
    x_offset = -0.05
    y_offset = 2.5
    for p in ax.patches:
        b = p.get_bbox()
        val = "{}".format(int(b.y1 + b.y0))        
        ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize=fontsize)
    
    ax.set_title(title,fontsize=fontsize)
    #ax.legend(fontsize=fontsize)
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right",fontsize=fontsize)
    plt.setp(ax.get_yticklabels(),rotation=30, fontsize=fontsize)
    plt.xlabel('')
    plt.ylabel('')
    plt.subplots_adjust(left=0.2, bottom=0.22, right=0.98, top=0.94, wspace=None, hspace=None) 
    plt.savefig(gSaveBasePath + 'NZ_'+title+'.png')
    plt.show()
    
    
def parseConfirmed(df):
    Sex = list(set(df['Sex']))
    #AgeGroup = list(set(df['Age group']))
    #AgeGroup.sort()
    AgeGroup = [ '<1', '1 to 4', '5 to 9', '10 to 14', '15 to 19', '20 to 29', '30 to 39', '40 to 49', '50 to 59', '60 to 69', '70+']
    
    DHB = list(set(df['DHB']))
    bOverseas = list(set(df['Overseas travel']))
    bOverseas.remove(' ')
    LastTravelCountry = list(set(df['Last country before return']))
    LastTravelCountry.remove(np.nan)
    
    print('Sex=',Sex)
    print('AgeGroup=',AgeGroup)
    print('DHB=',DHB)
    print('bOverseas=',bOverseas)
    print('LastTravelCountry=',LastTravelCountry)
    
    columns=['Gender','Number']
    dfSex  = pd.DataFrame()
    for i in Sex:
        line = pd.DataFrame([[i, df[df['Sex']==i].shape[0]]],columns=columns)
        dfSex = dfSex.append(line, ignore_index=True) 
    dfSex.set_index(["Gender"], inplace=True)
   
    columns=['Group','Number']
    dfAgeGroup  = pd.DataFrame()
    for i in AgeGroup:
        line = pd.DataFrame([[i, df[df['Age group']==i].shape[0]]],columns=columns)
        dfAgeGroup = dfAgeGroup.append(line, ignore_index=True) 
    dfAgeGroup.set_index(["Group"], inplace=True)
    
    columns=['DHB','Number']
    dfDHB  = pd.DataFrame()
    for i in DHB:
        line = pd.DataFrame([[i, df[df['DHB']==i].shape[0]]],columns=columns)
        dfDHB = dfDHB.append(line, ignore_index=True) 
    #print(dfDHB)
    dfDHB.set_index(["DHB"], inplace=True)
    
    columns=['Overseas','Number']
    dfbOverseas  = pd.DataFrame()
    for i in bOverseas:
        line = pd.DataFrame([[i, df[df['Overseas travel']==i].shape[0]]],columns=columns)
        dfbOverseas = dfbOverseas.append(line, ignore_index=True) 
    dfbOverseas.set_index(["Overseas"], inplace=True)
    
    columns=['RecturnCountry','Number']
    dfLastTravelCountry  = pd.DataFrame()
    for i in LastTravelCountry:
        line = pd.DataFrame([[i, df[df['Last country before return']==i].shape[0]]],columns=columns)
        dfLastTravelCountry = dfLastTravelCountry.append(line, ignore_index=True) 
    dfLastTravelCountry.set_index(["RecturnCountry"], inplace=True)
    
    #dfSex = dfSex.sort_values(by = 0, axis=1) #dfSex.sort_values(by=['Female'],ascending=False)
    # dfAgeGroup = dfAgeGroup.sort_values(by=['Case_Per_1M_people'],ascending=False)
    dfDHB = dfDHB.sort_values(by=['Number'],ascending=False)
    # dfbOverseas = dfbOverseas.sort_values(by=['Case_Per_1M_people'],ascending=False)
    dfLastTravelCountry = dfLastTravelCountry.sort_values(by=['Number'],ascending=False)
    
    # print(dfSex)
    # print(dfAgeGroup)
    # print(dfDHB)
    # print(dfbOverseas)
    # print(dfLastTravelCountry)
    
    plotStatistcs(dfSex,title='Gender')
    plotStatistcs(dfAgeGroup,title='AgeGroup')
    plotStatistcs(dfDHB,title='DHB')
    plotStatistcs(dfbOverseas,title='IsOVerseas')
    plotStatistcs(dfLastTravelCountry,title='LastTravelCountry')
    
def main():
    file=r'.\NZ\covid-cases-24july20.xlsx'
    dfConfirmed = readExcel(file,'Confirmed') #'Probable'
    #dfConfirmed = readExcel(file, ['Confirmed','Probable'])
    parseConfirmed(dfConfirmed)
    
if __name__ == '__main__':
    main()
    