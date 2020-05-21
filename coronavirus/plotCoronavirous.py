#python3 unicode
#author:Steven Huang 25/04/20
#function: Query cases of COVID-19 from website
#World case statistics by time reference: https://ourworldindata.org/covid-cases

import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt

gSaveBasePath=r'.\images\\'

def plotData(df,number = 25):    
    if number>df.shape[0]:
        number = df.shape[0]
    #df = df.iloc[1:number,:]
    worldDf = df.iloc[:1,:]
    
    df = df.sort_values(by=['Confirmed'],ascending=False)
    df1 = df.iloc[1:number,[0]]
    df = df.sort_values(by=['Case_Per_1M_people'],ascending=False)
    df2 = df.iloc[1:number,[1]]
    df = df.sort_values(by=['Recovered'],ascending=False)
    df3 = df.iloc[1:number,[2]]
    df = df.sort_values(by=['Deaths'],ascending=False)
    df4 = df.iloc[1:number,[3]]
    df = df.sort_values(by=['Mortality'],ascending=False)
    df5 = df.iloc[1:number,[4]]

    dfDeaths = df[df['Deaths'] > 200]
    df6 = dfDeaths.sort_values(by=['Mortality'],ascending=True).iloc[:number,[4]]
    
    dfConfirmed = df[df['Confirmed'] > 5000]
    df7 = dfConfirmed.sort_values(by=['Mortality'],ascending=True).iloc[:number,[4]]
        
    dfDeathsZero = df[df['Deaths'] == 0]
    df8 = dfDeathsZero.sort_values(by=['Confirmed'],ascending=False).iloc[:number,[0]]
    
    dfDeathsThanZero = df[df['Deaths'] > 0]
    df9 = dfDeathsThanZero.sort_values(by=['Mortality'],ascending=True).iloc[:number,[4]]
    
    #print(df.head())
    #print(df.dtypes)
    #worldDf = df.loc['Worldwide']
    #print(worldDf)
    now = datetime.datetime.now()
    
    today = str(' Date:') + str(now.strftime("%Y-%m-%d %H:%M:%S"))
    topStr = 'Top '+str(number) + ' '
    
    ccWorld = topStr + 'Confirmed(World: ' + str(int(worldDf['Confirmed'][0])) + today + ')'
    cpWorld = topStr + 'Case_Per_1M_people(World: ' + str(int(worldDf['Case_Per_1M_people'][0])) + today + ')'
    reWorld = topStr + 'Recovered(World: ' + str(int(worldDf['Recovered'][0])) + today + ')'
    deWorld = topStr + 'Deaths(World: ' + str(int(worldDf['Deaths'][0]))+ today + ')'
    moWorld = topStr + 'Mortality(World: ' + str(round(worldDf['Mortality'][0],3)) + today + ')'
    moCountries = 'Mortality(Countries: ' + str(dfDeaths.shape[0]) + ' Deaths>200' + today + ')'
    coCountries = 'Mortality(Countries: ' + str(dfConfirmed.shape[0]) + ' Confirmed>5k' + today + ')'
    dzCountries = 'Confirmed(Countries: ' + str(dfDeathsZero.shape[0]) + ' Deaths==0' + today + ')'
    dnzCountries = 'Mortality(Countries: ' + str(dfDeathsThanZero.shape[0]) + ' Deaths>0' + today + ')'
    
    dfs = [(ccWorld, df1),(cpWorld, df2),(reWorld, df3),(deWorld, df4),(moWorld, df5),\
        (moCountries,df6),(coCountries,df7),(dzCountries,df8),(dnzCountries,df9)]

    fontsize = 8
    for i,data in enumerate(dfs): 
        dataFrame = data[1]
        #print('dataFrame.shape=',i,dataFrame.shape)
        if dataFrame.shape[0] == 0:
            continue
            
        kind='bar'
        if number>25:
            dataFrame = binaryDf(dataFrame)
            kind='barh'
             
        title = data[0]

        if i==3 or i==4 or i==5 or i==6: #deaths mortality
            ax = dataFrame.plot(kind=kind,color='r')
        else:
            ax = dataFrame.plot(kind=kind)

        ax.set_title(title,fontsize=fontsize)
        ax.legend()
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right",fontsize=fontsize)
        plt.setp(ax.get_yticklabels(),fontsize=fontsize)
        
        if number>25:
            plt.subplots_adjust(left=0.30, bottom=None, right=0.98, top=None, wspace=None, hspace=None)
        
        plt.savefig(gSaveBasePath + str(i+1)+'.png')
    plt.show()
    
    #plotTable(worldDf)
    plotChangeBydata()
    plotWorldStatisticByTime()
    
def binaryDf(df):
    newdf = pd.DataFrame(columns=df.columns)
    #print('pd.shape=',df.shape)
    newIndex = []
    for i in range(df.shape[0]//2):
        dd = df.loc[df.index[i*2], :]
        #print('dd=',df.index[i*2], dd.values)
        newIndex.append(df.index[i*2] +',' + df.index[i*2+1])
        newdf = newdf.append(dd,ignore_index=True)
        
    #print('newIndex=',len(newIndex),newIndex)
    #print('newdf.shape=',newdf.shape)
    newdf.index = newIndex
    return newdf

def plotTable(df):
    print(df)
    fig, ax = plt.subplots()
    # hide axes
    #fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    plt.title('World statitic')
    #fig.tight_layout()
    plt.show()
    
def readCsv(file):
    df = pd.read_csv(file)
    #print(df.describe().transpose())
    #print(df.head())
    #df.set_index(["Location"], inplace=True)
    #print('df.columns=',df.columns)
    #print('df.dtypes = ',df.dtypes)
    #df = df.apply(pd.to_numeric, axis=0)
    #print('df.dtypes = ',df.dtypes)
    #plotTest(df)
    #plotDataCompare(df)
    return df
      
def plotTest(df,number = 20):
    #df = df.iloc[1:number,:]
    df = df.sort_values(by=['Confirmed'],ascending=False)
    df1 = df.iloc[1:number,[0]]
    df = df.sort_values(by=['Case_Per_1M_people'],ascending=False)
    df2 = df.iloc[1:number,[1]]
    df = df.sort_values(by=['Recovered'],ascending=False)
    df3 = df.iloc[1:number,[2]]
    df = df.sort_values(by=['Deaths'],ascending=False)
    df4 = df.iloc[1:number,[3]]
    df = df.sort_values(by=['Mortality'],ascending=False)
    df5 = df.iloc[1:number,[4]]

    dfDeaths = df[df['Deaths'] > 200]
    df6 = dfDeaths.sort_values(by=['Mortality'],ascending=True).iloc[:number,[4]]
    
    dfConfirmed = df[df['Confirmed'] > 5000]
    df7 = dfConfirmed.sort_values(by=['Mortality'],ascending=True).iloc[:number,[4]]
        
    #print(df.head())
    #print(df.dtypes)
    worldDf = df.loc['Worldwide']
    #print(worldDf,worldMor)
    now = datetime.datetime.now()
    
    today = str(' Date:') + str(now.strftime("%Y-%m-%d %H:%M:%S"))
    
    ccWorld = 'Confirmed(World: ' + str(int(worldDf['Confirmed'])) + today + ')'
    cpWorld = 'Case_Per_1M_people(World: ' + str(int(worldDf['Case_Per_1M_people'])) + today + ')'
    reWorld = 'Recovered(World: ' + str(int(worldDf['Recovered'])) + today + ')'
    deWorld = 'Deaths(World: ' + str(int(worldDf['Deaths']))+ today + ')'
    moWorld = 'Mortality(World: ' + str(round(worldDf['Mortality'],3)) + today + ')'
    moCountries = 'Mortality(Countries: ' + str(dfDeaths.shape[0]) + ' Deaths>200' + today + ')'
    coCountries = 'Mortality(Countries: ' + str(dfConfirmed.shape[0]) + ' Confirmed>5k' + today + ')'
    
    #dfs = [(ccWorld, df1),(cpWorld, df2),(reWorld, df3),(deWorld, df4),(moWorld, df5),(moCountries,df6),(coCountries,df7)]
    
    df = df[df['Deaths'] > 0]
    df = df.iloc[1:,:]
    print('df.shape=',df.shape)
    
    df = binaryDf(binaryDf(df))
    
    dfs = [('test', df)]
    fontsize = 8
    for i,data in enumerate(dfs): 
        df = data[1]
        title = data[0]

        kinds = ['bar']# ['line','bar','barh','hist','box','kde','density','area']  
        for k in kinds:
            #df.plot(kind=k, title=k, y='Confirmed',  x = 'Deaths')
            #df.plot(kind=k, title=k, y='Confirmed')
            ax = df.plot(kind=k, title=k, y='Mortality')
            #plt.scatter(x=df['Deaths'], y=df['Confirmed'])
            plt.setp(ax.get_xticklabels(), rotation=30, ha="right",fontsize=fontsize)
            plt.setp(ax.get_yticklabels(),fontsize=fontsize)
            plt.show()
            
        #kinds = ['pie','scatter','hexbin']
        kinds =[]# ['hexbin']
        for k in kinds:
            #df.plot(kind=k, title=k, y='Confirmed',  x = 'Deaths')
            #hexbin
            df.plot(kind=k, title=k, y='Confirmed',  x = 'Deaths', bins=10,xscale='log',yscale='log')
            #plt.scatter(x=df['Deaths'], y=df['Confirmed'])
            plt.show()
        break
    
    plt.show()
    
def plotDataCompare(df,number = 50):
    #df = df.iloc[1:number,:]
    df = df.sort_values(by=['Confirmed'],ascending=False)
    df1 = df.iloc[1:number,[0]]
    df = df.sort_values(by=['Case_Per_1M_people'],ascending=False)
    df2 = df.iloc[1:number,[1]]
    df = df.sort_values(by=['Recovered'],ascending=False)
    df3 = df.iloc[1:number,[2]]
    df = df.sort_values(by=['Deaths'],ascending=False)
    df4 = df.iloc[1:number,[3]]
    df = df.sort_values(by=['Mortality'],ascending=False)
    df5 = df.iloc[1:number,[4]]

    dfDeaths = df[df['Deaths'] > 200]
    df6 = dfDeaths.sort_values(by=['Mortality'],ascending=True).iloc[:number,[4]]
    
    dfConfirmed = df[df['Confirmed'] > 5000]
    df7 = dfConfirmed.sort_values(by=['Mortality'],ascending=True).iloc[:number,[4]]
        
    dfDeathsZero = df[df['Deaths'] == 0]
    df8 = dfDeathsZero.sort_values(by=['Confirmed'],ascending=False).iloc[:number,[0]]
    
    dfDeathsThanZero = df[df['Deaths'] > 0]
    df9 = dfDeathsThanZero.sort_values(by=['Mortality'],ascending=True).iloc[:number,[4]]
    
    worldDf = df.loc['Worldwide']
    #print(worldDf,worldMor)
    now = datetime.datetime.now()
    
    today = str(' Date:') + str(now.strftime("%Y-%m-%d %H:%M:%S"))
    
    ccWorld = 'Confirmed(World: ' + str(int(worldDf['Confirmed'])) + today + ')'
    cpWorld = 'Case_Per_1M_people(World: ' + str(int(worldDf['Case_Per_1M_people'])) + today + ')'
    reWorld = 'Recovered(World: ' + str(int(worldDf['Recovered'])) + today + ')'
    deWorld = 'Deaths(World: ' + str(int(worldDf['Deaths']))+ today + ')'
    moWorld = 'Mortality(World: ' + str(round(worldDf['Mortality'],3)) + today + ')'
    moCountries = 'Mortality(Countries: ' + str(dfDeaths.shape[0]) + ' Deaths>200' + today + ')'
    coCountries = 'Mortality(Countries: ' + str(dfConfirmed.shape[0]) + ' Confirmed>5k' + today + ')'
    dzCountries = 'Confirmed(Countries: ' + str(dfDeathsZero.shape[0]) + ' Deaths==0' + today + ')'
    dnzCountries = 'Mortality(Countries: ' + str(dfDeathsThanZero.shape[0]) + ' Deaths>0' + today + ')'
    
    dfs = [(ccWorld, df1),(cpWorld, df2),(reWorld, df3),(deWorld, df4),(moWorld, df5),\
        (moCountries,df6),(coCountries,df7),(dzCountries,df8),(dnzCountries,df9)]
    
    fontsize = 8
    #------------------------#
    df = df.sort_values(by=['Confirmed'],ascending=False)
    if number>25:
        df = binaryDf(df)
    
    dfConfirmed = df.iloc[1:number,[0]]
    dfCase_Per_1M_people = df.iloc[1:number,[1]]
    dfRecovered = df.iloc[1:number,[2]]
    dfDeaths = df.iloc[1:number,[3]]
    dfMortality = df.iloc[1:number,[4]]
    
    # print(dfConfirmed.head())
    # print(dfRecovered.head())
    # print(dfDeaths.head())
    
    width = 0.5
    ax = plt.subplot(1,1,1)
    
    colors=['b','g','r']
    dd = []
    ddName=[]
    dd.append(dfConfirmed.iloc[:,0]),ddName.append('Confirmed')
    dd.append(dfRecovered.iloc[:,0]),ddName.append('Recovered')
    dd.append(dfDeaths.iloc[:,0]),ddName.append('Deaths')
    dfCompareds = [(ddName, dd, 'covid-19 statistics')]
    
    # dd = []
    # ddName=[]
    # dd.append(dfDeaths.iloc[:,0]),ddName.append('Deaths')
    # dd.append(dfMortality.iloc[:,0]),ddName.append('Mortality')
    # dfCompareds.append((ddName, dd))
    '''
    for i in dfCompareds:
        newDf = pd.DataFrame()
        title = i[2]
        for id,(name,data) in enumerate(zip(i[0],i[1])):
            print(id,name,title)
            color = colors[id%len(colors)]
            if 1: #style1 cumulate
                if id==0:
                    ax.barh(data.index, data , width, label=name,color=color)
                    lf = i[1][id]
                else:
                    ax.barh(data.index, data , width, label=name,color=color,left=lf)
                    lf +=i[1][id]
            else:
                newDf[name] = data
                #newDf = newDf.append(pd.DataFrame({name: data}, index=data.index))
                ax.barh(data.index, data , width, label=name,color=color)
            
        #print(newDf.head())
        #ax = newDf.plot.barh(rot=0,width=0.8)  
        ax.legend()
        ax.set_title(title)
        
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right",fontsize=fontsize)
        plt.setp(ax.get_yticklabels(),fontsize=fontsize)
        plt.subplots_adjust(left=0.30, bottom=None, right=0.98, top=None, wspace=None, hspace=None)
        #plt.savefig(str(i+1)+'new.png')
        plt.show()   
    '''
       
    #-------------------------#
    dC = dfConfirmed.iloc[:,0]
    dM = dfMortality.iloc[:,0]
    dD = dfDeaths.iloc[:,0]
    ax.bar(dC.index, dC , width, label='Confirmed',color=colors[0])
    #ax.plot(dC.index, dC)
    #print(dC.index,dC.shape)
    ax.plot(dM.index, dM)
    ax.plot(dD.index, dD)
    #print(dM.index,dM.shape)
    ax.set_title('Confirmed & Mortality')
    
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right",fontsize=fontsize)
    plt.setp(ax.get_yticklabels(),fontsize=fontsize)
    plt.subplots_adjust(left=0.30, bottom=None, right=0.98, top=None, wspace=None, hspace=None)
    plt.show()   
        
def pathsFiles(dir,filter=''): #"cpp h txt jpg"
    def getExtFile(file):
        return file[file.find('.')+1:]
    
    def getFmtFile(path):
        #/home/User/Desktop/file.txt    /home/User/Desktop/file     .txt
        root_ext = os.path.splitext(path) 
        return root_ext[1]

    fmts = filter.split()    
    if fmts:
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                if getExtFile(getFmtFile(filename)) in fmts:
                    yield dirpath+'\\'+filename
    else:
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                yield dirpath+'\\'+filename    
           
def getDateFromFileName(name):
    name = name[name.find('s')+1 : ]
    name = name[: name.find('.')]
    
    if name[0] == '_':
        name = name[1 : ]
    
    name = name[: name.rfind('_')]
    #print('name=',name)
    return name

def plotChangeBydata(csvpath=r'./data/'):
    pdDate = pd.DataFrame()
    for i in pathsFiles(csvpath,'csv'):
        #print(i,getDateFromFileName(i))
        df = readCsv(i)
        df.set_index(["Location"], inplace=True)
        
        dateTime = getDateFromFileName(i)
        
        #print(worldDf)
        #print(worldDf.values)
        if pdDate.shape[0]>0:
            if pdDate['DataTime'].isin([dateTime]).any():
                continue
            
        worldDf = df.iloc[:1,:]        
        #worldDf['DataTime'] = dateTime
        worldDf.insert(5, "DataTime", dateTime, True) 
        pdDate = pdDate.append(worldDf)
  
    #print(pdDate.shape)
    #print(pdDate.head())
    pdDate.set_index(["DataTime"], inplace=True)
    df = pdDate.sort_values(by=['DataTime'],ascending=False)
    #print(pdDate.head())
    
    df1 = pdDate.iloc[:,[0]]
    
    fontsize = 8
    ax = pdDate.plot(kind='line')
    ax.set_title('World COVID19 Change')
    
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right",fontsize=fontsize)
    plt.setp(ax.get_yticklabels(),fontsize=fontsize)
    plt.subplots_adjust(left=0.07, bottom=0.16, right=0.96, top=0.94, wspace=None, hspace=None)
    plt.savefig(gSaveBasePath + 'WorldChange.png')
    plt.show()
    
def plotPdColumn(index,data,title,label,color=None):
    fontsize = 6
    ax = plt.subplot(1,1,1)
    
    ax.set_title(title,fontsize=fontsize)
    #ax.barh(dfWorld.index,dfWorld['Cases'])
    if color:
        ax.bar(index,data,label=label,width=0.6,color=color)
    else:            
        ax.bar(index,data,label=label,width=0.6)
    
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right",fontsize=fontsize)
    plt.setp(ax.get_yticklabels(),fontsize=fontsize)
    plt.subplots_adjust(left=0.08, bottom=None, right=0.98, top=0.92, wspace=None, hspace=None)
    plt.savefig(gSaveBasePath + label+'World.png')
    plt.show()
        
def plotWorldStatisticByTime(csvpath=r'./'):
    csv = csvpath + 'total-cases-covid-19.csv'
    df = readCsv(csv)
    df = df[df['Entity'] == 'World' ]
    df = df.rename(columns={"Total confirmed cases of COVID-19 (cases)": "Cases"})
    #print(df.head())
    
    data = {'Date':df['Date'], 'Cases': df['Cases']}
    dfWorld = pd.DataFrame(data=data)
    dfWorld.set_index(["Date"], inplace=True)
    #print(dfWorld.tail())
    #print(dfWorld['Cases'].shape)
    #print(dfWorld['Cases'])
    
    dfNewCases = [0]
    for i in range(len(dfWorld['Cases']) -1):
        numberI = dfWorld.iloc[i,0]
        numberINext = dfWorld.iloc[i+1,0]
        newCases = numberINext-numberI
        #print(numberI,numberINext,newCases)
        dfNewCases.append(newCases)
        
    #print(len(dfNewCases))
    dfWorld['newCases'] = dfNewCases
    #print(dfWorld.head())
    #print(dfWorld.index)
    
    newRecentDays = 40
    dfWorldNew = dfWorld.iloc[-1-newRecentDays:-1, :]
    dfWorld = dfWorld.iloc[::3] # even #dfWorld.iloc[1::2] #odd
    #print(dfWorldNew.shape)
    
    plotPdColumn(dfWorld.index,dfWorld['Cases'],title='World COVID-19 Cases',label='Cases')
    plotPdColumn(dfWorld.index,dfWorld['newCases'],title='World COVID-19 New Cases',label='newCases',color='y')
    plotPdColumn(dfWorldNew.index,dfWorldNew['newCases'],title='World COVID-19 Recent New Cases',label='recentNewCases',color='y')
    
if __name__ == '__main__':
    csvpath=r'./data/'
    #readCsv(csvpath+'coronavirous_2020-05-05_193026.csv')
    #plotChangeBydata(csvpath)
    plotWorldStatisticByTime()