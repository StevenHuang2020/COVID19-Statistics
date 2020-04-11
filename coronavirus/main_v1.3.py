#python3 unicode
#author:Steven Huang 31/03/20
#function: Query cases of COVID-19 from website using selenium
"""""""""""""""""""""""""""""""""""""""""""""""""""""
#usgae:
#python .\main_v1.3.py
"""""""""""""""""""""""""""""""""""""""""""""""""""""
import datetime
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from main import plotData

mainUrl = "https://google.com/covid19-map/"

def parseXpathTr(tr,columns):
    tds = tr.find_elements(By.TAG_NAME, "td")
    #print(len(tds))

    location,confirmed,Case_Per_1M_people,recovered,deaths = '','','','',''
    for i,td in enumerate(tds):
        if i == 0:
            location = td.find_element(By.TAG_NAME, "span").text
        elif i == 1:
            confirmed = td.text.strip()
        elif i == 2:
            Case_Per_1M_people = td.text.strip()
        elif i == 3:
            recovered = td.text.strip()
        elif i == 4:
            deaths = td.text.strip()

    if Case_Per_1M_people == '' or Case_Per_1M_people == '—':
        Case_Per_1M_people = '0'
    if recovered == '' or recovered == '—':
        recovered = '0'
    if deaths == '' or deaths == '—':
        deaths = '0'
    if confirmed == '' or confirmed == '—':
        confirmed = '0'

    #print('Location:',location,'Confirmed:',confirmed,'Case_Per_1M_people:',Case_Per_1M_people,'Recovered:',recovered,'deaths:',deaths)
    #columns=['Localtion', 'Confirmed',  'Case_Per_1M_people', 'Recovered', 'Deaths']
    dfLine = pd.DataFrame([[location, confirmed, Case_Per_1M_people, recovered, deaths]], columns=columns)
    return dfLine

def getHeader(thead):
    ths = thead.find_elements_by_xpath('//tr[@class="sgXwHf"]//span')
    print('len=',len(ths))
    lc,cf,cp,re,de = '','','','',''
    for i,th in enumerate(ths):
        if i==0:
            lc = th.text
        elif i ==1:
            cf = th.text
        elif i ==2:
            cp = th.text
        elif i ==3:
            re = th.text
        elif i ==4:
            de = th.text
        #print(th.text)
    return [lc,cf,cp,re,de]

def Load(url):
    print("Open:",url)
    driver = webdriver.Chrome()
    driver.get(mainUrl)
    sleep(1)
    
    #X = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div[2]/div[2]/c-wiz/div/div[2]/div/div[1]/table'
    X = '//table[@class="pH8O4c"]'
    table_id = driver.find_element_by_xpath(X)
    thead = table_id.find_element_by_tag_name('thead')
    tbody = table_id.find_element_by_tag_name('tbody')

    columns = getHeader(thead)
    #print('columns = ', columns)
    columns[2]='Case_Per_1M_people'
    
    df = pd.DataFrame()
    result = tbody.find_elements(By.TAG_NAME, "tr")
    for i in result:
        df = df.append(parseXpathTr(i, columns),ignore_index=True)
    
    print('df.shape=', df.shape)
    plotData(df)

if __name__ == '__main__':
    #mainUrl=r'file:///E:/python/spider/coronavirus/a.html'
    Load(mainUrl)
    