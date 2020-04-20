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
from selenium.webdriver.common.action_chains import ActionChains

from main import plotData

mainUrl = "https://google.com/covid19-map/"

def parseXpathTr(tr,columns):
    location,confirmed,Case_Per_1M_people,recovered,deaths = '','','','',''

    #span = tr.find_element_by_xpath('//th[@class="l3HOY"]/div/span')
    span = tr.find_elements(By.TAG_NAME, "span")
    if len(span) > 1:
        location = span[1].text
    elif len(span) == 1:
        location = span[0].text
        
    tds = tr.find_elements(By.TAG_NAME, "td")
    #print(len(tds))
    for i,td in enumerate(tds):
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

def clickBtn(driver,btnXpath):
        btn = driver.find_element_by_xpath(btnXpath)
        if btn:
            btn.click()

def scroll_down_element(driver, element):
    try:
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element.click() 
    except Exception as e:
        print('error scrolling down web element', e)
        
def Load(url):
    print("Open:",url)
    driver = webdriver.Chrome()
    driver.get(mainUrl)
    sleep(1)
    
    btn_More='//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[4]/div'
    clickBtn(driver,btn_More)
        
    #X = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div[2]/div[2]/c-wiz/div/div[2]/div/div[1]/table'
    X = '//table[@class="pH8O4c"]'
    table_id = driver.find_element_by_xpath(X)
    scroll_down_element(driver,table_id) #do an table action to get all table lines
    
    thead = table_id.find_element_by_tag_name('thead')
    tbody = table_id.find_element_by_tag_name('tbody')

    columns = getHeader(thead)
    #print('columns = ', columns)
    columns[2]='Case_Per_1M_people'
    
    df = pd.DataFrame()
    result = tbody.find_elements(By.TAG_NAME, "tr")
    print('result=',len(result))
    for i in result:
        df = df.append(parseXpathTr(i, columns),ignore_index=True)
    
    print('df.shape=', df.shape)
    plotData(df)

if __name__ == '__main__':
    #mainUrl=r'file:///E:/python/spider/coronavirus/a.html'
    Load(mainUrl)
    