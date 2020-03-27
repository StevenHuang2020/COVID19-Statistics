#python3 unicode
#author:Steven Huang 27/03/20
#function: Query cases of COVID-19 from website

"""""""""""""""""""""""""""""""""""""""""""""""""""""
#usgae:
#python main.py
"""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
sys.path.append("..")
import pandas as pd
from lxml import etree
from common.getHtml import openUrl, openUrlUrlLib
import matplotlib.pyplot as plt

mainUrl = "https://google.org/crisisresponse/covid19-map"

def preprocessData(df):
    print(df)
    #print('before preprocess:\n\n',df.head())
    #print(df.isnull())
    #print(df.isnull().any(axis=1))
    #null_columns=df.columns[df.isnull().any()]
    #print(df[df.isnull().any(axis=1)][null_columns])

    df[df.columns[1:]] = df[df.columns[1:]].apply(lambda x: x.str.replace(',',''))
    #print('before preprocess:\n\n',df.head())
    
    df['Confirmed Cases'] = pd.to_numeric(df['Confirmed Cases'])
    df['Confirmed Cases'] = df['Confirmed Cases'].astype('int64')

    df['Case_Per_1Mpeople'] = pd.to_numeric(df['Case_Per_1Mpeople'])
    df['Case_Per_1Mpeople'] = df['Case_Per_1Mpeople'].astype(float)

    df['Recovered'] = pd.to_numeric(df['Recovered'])
    df['Recovered'] = df['Recovered'].astype('int64')

    df['Deaths'] = pd.to_numeric(df['Deaths'])
    df['Deaths'] = df['Deaths'].astype('int64')
    
    df.set_index(["Localtion"], inplace=True)
    return df

def plotData(df):
    #['Localtion', 'Confirmed Cases',  'Case_Per_1Mpeople', 'Recovered', 'Deaths']
    number = 20
    df = preprocessData(df)
    #df = df.iloc[1:number,:]
    df1 = df.iloc[1:number,[0]]
    df2 = df.iloc[1:number,[1]]
    df3 = df.iloc[1:number,[2]]
    df4 = df.iloc[1:number,[3]]

    #print(df.head())
    #print(df.dtypes)
    dfs = [('Confirmed Cases',df1),('Case_Per_1Mpeople',df2),('Recovered',df3),('Deaths',df4)]
    for i,data in enumerate(dfs): 
        df = data[1]
        title = data[0]

        ax = df.plot(kind='bar')
        ax.set_title(title)
        ax.legend()
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    plt.show()


def parseXpathTr(tr):
    html = etree.HTML(etree.tostring(tr))
    result = html.xpath('//td') 
    #print(len(result),result)
    location,confirmed,casePer_1Mpeople,recovered,deaths = '','','','',''

    for i,td in enumerate(result):
        if i == 0:
            span = etree.HTML(etree.tostring(td)).xpath('//span')
            #print(len(span),span)
            #print(span[0].text)
            location = span[0].text
        elif i == 1:
            confirmed = td.text.strip()
        elif i == 2:
            casePer_1Mpeople = td.text.strip() 
        elif i == 3:
            recovered = td.text.strip()
        elif i == 4:
            deaths = td.text.strip()

    if casePer_1Mpeople == '' or casePer_1Mpeople == '—':
        casePer_1Mpeople = '0'
    if recovered == '' or recovered == '—':
        recovered = '0'
    if deaths == '' or deaths == '—':
        deaths = '0'
    if confirmed == '' or confirmed == '—':
        confirmed = '0'

    #print('Location:',location,'Confirmed:',confirmed,'Case_Per_1Mpeople:',casePer_1Mpeople,'Recovered:',recovered,'deaths:',deaths)
    columns=['Localtion', 'Confirmed Cases',  'Case_Per_1Mpeople', 'Recovered', 'Deaths']
    dfLine = pd.DataFrame([[location, confirmed, casePer_1Mpeople, recovered, deaths]], columns=columns)
    return dfLine
    
def parseHtml(htmlContent):
    html = etree.HTML(htmlContent)
    #X = '//*[@id="main"]/div[2]/div/div/div/div/div[1]/table'
    X = '//*[@id="main"]/div[2]/div/div/div/div/div[1]/table/tbody/tr'
    result = html.xpath(X)
    #print(len(result),result)

    df  = pd. DataFrame()
    for i in result:
        df = df.append(parseXpathTr(i),ignore_index=True)
    #print(df)
    plotData(df)

def Load(url):
    print("Open:",url)
    #html = openUrl(url)
    html = openUrlUrlLib(url)
    #print(html)
    return parseHtml(html)
    
if __name__ == '__main__':
    #mainUrl=r'file:///E:/python/spider/coronavirus/cov.html'
    Load(mainUrl)
    