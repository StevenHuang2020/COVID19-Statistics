#python3 unicode
#author:Steven Huang 31/03/20
#function: Query cases of COVID-19 from website using selenium

"""""""""""""""""""""""""""""""""""""""""""""""""""""
#usgae:
#python main.py
"""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
sys.path.append("..")
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

mainUrl = "https://google.com/covid19-map/"

def writeToCsv(df):
    daytime = datetime.datetime.now()
    today = datetime.date.today()
    t = str(today) + '_' + str(daytime.hour) + str(daytime.minute)
    #file='coronavirous.csv'
    file='coronavirous' + t + '.csv'
    df.to_csv(file,index=True)
              
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
    df.set_index(["Localtion"], inplace=True)

    print('\n\nAfter preprocess:\n',df.head())
    writeToCsv(df)
    return df

def plotData(df):
    #['Localtion', 'Confirmed',  'Case_Per_1M_people', 'Recovered', 'Deaths']
    number = 20
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

    #print(df.head())
    #print(df.dtypes)
    #worldDf = df.loc[df['Deaths'] == 24073]
    worldDf = df.loc['Worldwide']
    #print(worldDf,worldMor)
    ccWorld = 'Confirmed(world: ' + str(int(worldDf['Confirmed'])) + ')'
    cpWorld = 'Case_Per_1M_people(world: ' + str(int(worldDf['Case_Per_1M_people'])) + ')'
    reWorld = 'Recovered(world: ' + str(int(worldDf['Recovered'])) + ')'
    deWorld = 'Deaths(world: ' + str(int(worldDf['Deaths'])) + ')'
    moWorld = 'Mortality(world: ' + str(round(worldDf['Mortality'],3)) + ')'
    # print(ccWorld)
    # print(cpWorld)
    # print(reWorld)
    # print(deWorld)
    # print(moWorld)
    dfs = [(ccWorld, df1),(cpWorld, df2),(reWorld, df3),(deWorld, df4),(moWorld, df5)]
    for i,data in enumerate(dfs): 
        df = data[1]
        title = data[0]

        if i==4: #mortality
            ax = df.plot(kind='bar',color='r')
        else:
            ax = df.plot(kind='bar')

        ax.set_title(title)
        ax.legend()
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    plt.show()


def parseXpathTr(tr):
    tds = tr.find_elements(By.TAG_NAME, "td")
    #print(len(tds))

    location,confirmed,casePer_1Mpeople,recovered,deaths = '','','','',''
    for i,td in enumerate(tds):
        if i == 0:
            location = td.find_element(By.TAG_NAME, "span").text
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

    #print('Location:',location,'Confirmed:',confirmed,'Case_Per_1M_people:',casePer_1Mpeople,'Recovered:',recovered,'deaths:',deaths)
    columns=['Localtion', 'Confirmed',  'Case_Per_1M_people', 'Recovered', 'Deaths']
    dfLine = pd.DataFrame([[location, confirmed, casePer_1Mpeople, recovered, deaths]], columns=columns)
    return dfLine

def getHeader(thead):
    ths = thead.find_elements_by_xpath('//th')
    #print('len=',len(ths))
    lc,cf,cp,re,de = '','','','',''
    for i,th in enumerate(ths):
        lc = th.find_element_by_xpath("//div[@id='c1']").text
        cf = th.find_element_by_xpath("//div[@id='c2']").text
        cp = th.find_element_by_xpath("//div[@id='c3']").text
        re = th.find_element_by_xpath("//div[@id='c4']").text
        de = th.find_element_by_xpath("//div[@id='c5']").text
    return [lc,cf,cp,re,de]

def Load(url):
    print("Open:",url)
    driver = webdriver.Chrome()
    driver.get(mainUrl)
    sleep(1)
    
    #table_id = driver.find_element_by_class_name('SAGQRd')
    X = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div[2]/div[2]/c-wiz/div/div[2]/div/div[1]/table'
    table_id = driver.find_element_by_xpath(X)
    thead = table_id.find_element_by_tag_name('thead')
    tbody = table_id.find_element_by_tag_name('tbody')

    columns = getHeader(thead)

    result = tbody.find_elements(By.TAG_NAME, "tr")

    df = pd.DataFrame()
    for i in result:
        df = df.append(parseXpathTr(i),ignore_index=True)
    print('df.shape=', df.shape)
    plotData(df)

if __name__ == '__main__':
    #mainUrl=r'file:///E:/python/spider/coronavirus/cov.html'
    #mainUrl = 'file:///E:/python/spider/coronavirus/Coronavirus%20(COVID-19)%20map.html'
    Load(mainUrl)
    