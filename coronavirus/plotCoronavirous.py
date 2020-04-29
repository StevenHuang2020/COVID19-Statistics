#python3 unicode
#author:Steven Huang 25/04/20
#function: Query cases of COVID-19 from website

"""""""""""""""""""""""""""""""""""""""""""""""""""""
#usgae:
#python main.py
"""""""""""""""""""""""""""""""""""""""""""""""""""""
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def plotData(df,number = 25):    
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
    
    #print(df.head())
    #print(df.dtypes)
    worldDf = df.loc['Worldwide']
    #print(worldDf,worldMor)
    now = datetime.datetime.now()
    
    today = str(' Date:') + str(now.strftime("%Y-%m-%d %H:%M:%S"))
    topStr = 'Top '+str(number) + ' '
    
    ccWorld = topStr + 'Confirmed(World: ' + str(int(worldDf['Confirmed'])) + today + ')'
    cpWorld = topStr + 'Case_Per_1M_people(World: ' + str(int(worldDf['Case_Per_1M_people'])) + today + ')'
    reWorld = topStr + 'Recovered(World: ' + str(int(worldDf['Recovered'])) + today + ')'
    deWorld = topStr + 'Deaths(World: ' + str(int(worldDf['Deaths']))+ today + ')'
    moWorld = topStr + 'Mortality(World: ' + str(round(worldDf['Mortality'],3)) + today + ')'
    moCountries = 'Mortality(Countries: ' + str(dfDeaths.shape[0]) + ' Deaths>200' + today + ')'
    coCountries = 'Mortality(Countries: ' + str(dfConfirmed.shape[0]) + ' Confirmed>5k' + today + ')'
    dzCountries = 'Confirmed(Countries: ' + str(dfDeathsZero.shape[0]) + ' Deaths==0' + today + ')'
    dnzCountries = 'Mortality(Countries: ' + str(dfDeathsThanZero.shape[0]) + ' Deaths>0' + today + ')'
    
    dfs = [(ccWorld, df1),(cpWorld, df2),(reWorld, df3),(deWorld, df4),(moWorld, df5),\
        (moCountries,df6),(coCountries,df7),(dzCountries,df8),(dnzCountries,df9)]
    
    fontsize = 8
    for i,data in enumerate(dfs): 
        df = data[1]
        kind='bar'
        if number>25:
            df = binaryDf(df)
            kind='barh'
             
        title = data[0]

        if i==3 or i==4 or i==5 or i==6: #deaths mortality
            ax = df.plot(kind=kind,color='r')
        else:
            ax = df.plot(kind=kind)

        ax.set_title(title,fontsize=fontsize)
        ax.legend()
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right",fontsize=fontsize)
        plt.setp(ax.get_yticklabels(),fontsize=fontsize)
        
        if number>25:
            plt.subplots_adjust(left=0.30, bottom=None, right=0.98, top=None, wspace=None, hspace=None)
        
        plt.savefig(str(i+1)+'.png')
    plt.show()

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

def readCsv(file):
    df = pd.read_csv(file)
    print(df.describe().transpose())
    print(df.head())
    df.set_index(["Location"], inplace=True)
    print('df.columns=',df.columns)
    #print('df.dtypes = ',df.dtypes)
    #df = df.apply(pd.to_numeric, axis=0)
    #print('df.dtypes = ',df.dtypes)
    #plotTest(df)
    #plotDataCompare(df)
    plotData(df)
      
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
    if 0:
        for i,data in enumerate(dfs): 
            df = data[1]
            df = binaryDf(df)  #index divide 2
            title = data[0]

            if i==3 or i==4 or i==5 or i==6: #deaths mortality
                ax = df.plot(kind='barh',color='r')
            else:
                ax = df.plot(kind='barh')

            ax.set_title(title,fontsize=fontsize)
            ax.legend()
            plt.setp(ax.get_xticklabels(), rotation=30, ha="right",fontsize=fontsize)
            plt.setp(ax.get_yticklabels(),fontsize=fontsize)
            plt.subplots_adjust(left=0.30, bottom=None, right=0.98, top=None, wspace=None, hspace=None)
            
            plt.savefig(str(i+1)+'new.png')
        plt.show()
    
    #------------------------#
    df = df.sort_values(by=['Confirmed'],ascending=False)
    df = binaryDf(df)
    
    dfConfirmed = df.iloc[1:number,[0]]
    dfCase_Per_1M_people = df.iloc[1:number,[1]]
    dfRecovered = df.iloc[1:number,[2]]
    dfDeaths = df.iloc[1:number,[3]]
    dfMortality = df.iloc[1:number,[4]]
    
    # dfConfirmed = binaryDf(dfConfirmed)
    # dfRecovered = binaryDf(dfRecovered)
    # dfDeaths = binaryDf(dfDeaths)
    # print(dfConfirmed.head())
    # print(dfRecovered.head())
    # print(dfDeaths.head())
    
    width = 0.5
    ax = plt.subplot(1,1,1)
    if 0:
        ax.barh(dfConfirmed.index, dfConfirmed.iloc[:,0] , width, label='Confirmed',color='b')
        ax.barh(dfConfirmed.index, dfRecovered.iloc[:,0] , width, label='Recovered',color='g',left=dfConfirmed['Confirmed'])
        ax.barh(dfConfirmed.index, dfDeaths.iloc[:,0] , width, label='Deaths',color='r',left=dfRecovered['Recovered']+dfConfirmed['Confirmed'])
        #ax.bar(df.index, df['b'], width, bottom = df['a'], label='b')
    else:
        colors=['b','g','r']
        dd = []
        ddName=[]
        dd.append(dfConfirmed.iloc[:,0]),ddName.append('Confirmed')
        dd.append(dfRecovered.iloc[:,0]),ddName.append('Recovered')
        dd.append(dfDeaths.iloc[:,0]),ddName.append('Deaths')
        dfCompareds = [(ddName, dd)]
        
        # dd = []
        # ddName=[]
        # dd.append(dfDeaths.iloc[:,0]),ddName.append('Deaths')
        # dd.append(dfMortality.iloc[:,0]),ddName.append('Mortality')
        # dfCompareds.append((ddName, dd))
       
        for i in dfCompareds:
            newDf = pd.DataFrame()
            for id,(name,data) in enumerate(zip(i[0],i[1])):
                print(id,name)
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
            plt.setp(ax.get_xticklabels(), rotation=30, ha="right",fontsize=fontsize)
            plt.setp(ax.get_yticklabels(),fontsize=fontsize)
            plt.subplots_adjust(left=0.30, bottom=None, right=0.98, top=None, wspace=None, hspace=None)
            #plt.savefig(str(i+1)+'new.png')
            plt.show()   
           

        
if __name__ == '__main__':
    readCsv(r'./coronavirous2020-04-26_1457.csv')
    