#python3 unicode
#author:Steven Huang 27/03/20
#function: Query cases of COVID-19 from website

"""""""""""""""""""""""""""""""""""""""""""""""""""""
#usgae:
#python main.py
"""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
sys.path.append("..")
import datetime
import pandas as pd
from lxml import etree
from common.getHtml import openUrl, openUrlUrlLib
import matplotlib.pyplot as plt

from jsonUpdate import updateJson

mainUrl = "https://google.com/covid19-map/" #"https://google.org/crisisresponse/covid19-map"

def writeToCsv(df):
    daytime = datetime.datetime.now()
    today = datetime.date.today()
    t = str(today) + '_' + str(daytime.__format__('%H%M%S'))
    
    #file='coronavirous.csv'
    file='coronavirous_' + t + '.csv'
    df.to_csv(file,index=True)
          
#columns=['Location', 'Confirmed', 'Case_Per_1M_people', 'Recovered', 'Deaths']    
def preprocessData(df):
    #print(df)
    print('\n\nBefore preprocess:\n',df.head())
    #print(df.isnull())
    #print(df.isnull().any(axis=1))
    #null_columns=df.columns[df.isnull().any()]
    #print(df[df.isnull().any(axis=1)][null_columns])

    df[df.columns[1:]] = df[df.columns[1:]].apply(lambda x: x.str.replace(',',''))
    #print('before preprocess:\n\n',df.head())
    
    df['Confirmed'] = pd.to_numeric(df['Confirmed'])
    df['Confirmed'] = df['Confirmed'].astype('int64')

    df['Case_Per_1M_people'] = pd.to_numeric(df['Case_Per_1M_people'])
    df['Case_Per_1M_people'] = df['Case_Per_1M_people'].astype(float)

    df['Recovered'] = pd.to_numeric(df['Recovered'])
    df['Recovered'] = df['Recovered'].astype('int64')

    df['Deaths'] = pd.to_numeric(df['Deaths'])
    df['Deaths'] = df['Deaths'].astype('int64')
    
    '''Add coloumn mortality rate: df['Deaths'] / df['Confirmed'].
    But please note that this is not necessarily the correct defintion.
    '''
    Mortality = df['Deaths']/df['Confirmed']
    #print(type(Mortality))
    #print(Mortality)
    dfMortality = pd.DataFrame(Mortality, columns=['Mortality'])

    df = pd.concat([df, dfMortality], axis=1)
    df.set_index(["Location"], inplace=True)

    print('\n\nAfter preprocess:\n',df.head())
    writeToCsv(df)
    updateJson()
    return df

def plotData(df,number = 25):    
    df = preprocessData(df)

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

def parseXpathTr(tr, columns):
    html = etree.HTML(etree.tostring(tr))
    
    #print(len(result),result)
    location,confirmed,Case_Per_1M_people,recovered,deaths = '','','','',''
    span = html.xpath('//span')
    if len(span) > 1:
        location = span[1].text
    elif len(span) == 1:
        location = span[0].text
    
    result = html.xpath('//td') 
    for i,td in enumerate(result):
        if i == 0:
            confirmed = td.text.strip()
        elif i == 1:
            Case_Per_1M_people = td.text.strip() 
        elif i == 2:
            recovered = td.text.strip()
        elif i == 3:
            deaths = td.text.strip()

    if Case_Per_1M_people == '' or Case_Per_1M_people == '—':
        Case_Per_1M_people = '0'
    if recovered == '' or recovered == '—':
        recovered = '0'
    if deaths == '' or deaths == '—':
        deaths = '0'
    if confirmed == '' or confirmed == '—':
        confirmed = '0'

    print('Location:',location,'Confirmed:',confirmed,'Case_Per_1M_people:',Case_Per_1M_people,'Recovered:',recovered,'deaths:',deaths)
    #columns=['Location', 'Confirmed', 'Cases per 1M people', 'Recovered', 'Deaths']
    dfLine = pd.DataFrame([[location, confirmed, Case_Per_1M_people, recovered, deaths]], columns=columns)
    return dfLine

def getHeader(thead):
    html = etree.HTML(etree.tostring(thead))
    #res = html.xpath('//th//div[@id="c1"]')
    #res = html.xpath('//div[@class="DdCLrb"]')
    res = html.xpath('//tr[@class="sgXwHf"]//span')
    print(len(res))
    lc,cf,cp,re,de = '','','','',''
    for i,div in enumerate(res):
        if i == 0:
            lc = div.text
        elif i == 1:
            cf = div.text
        elif i == 2:
            cp = div.text
        elif i == 3:
            re = div.text
        elif i == 4:
            de = div.text
                 
    return [lc,cf,cp,re,de]

def parseHtml(htmlContent):
    html = etree.HTML(htmlContent)
    #X = '//*[@id="main"]/div[2]/div/div/div/div/div[1]/table'
    #X = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div[2]/div[2]/c-wiz/div/div[2]/div/div[1]/table/tbody/tr'
    #X = '/html/body/c-wiz/div/div/div/div/div[2]/div[2]/c-wiz/div/div[2]/div/div[1]/table/tbody/tr'
    X = '//table[@class="pH8O4c"]/thead'
    #X = '//table'
    resHead = html.xpath(X)
    #print(len(resHead))    
    columns = getHeader(resHead[0])
    #print(columns)
    columns[2]='Case_Per_1M_people'
    
    X = '//table[@class="pH8O4c"]//tr' #[@class="SAGQRD"]'
    result = html.xpath(X)
    print(len(result))
    df  = pd. DataFrame()
    for i in result:
        df = df.append(parseXpathTr(i, columns),ignore_index=True)
    print('df.shape=', df.shape)
    plotData(df)

def Load(url):
    print("Open:",url)
    #html = openUrl(url)
    html = openUrlUrlLib(url)
    #print(html)
    return parseHtml(html)
    
if __name__ == '__main__':
    #mainUrl=r'file:///E:/python/spider/coronavirus/a.html'
    Load(mainUrl)
    