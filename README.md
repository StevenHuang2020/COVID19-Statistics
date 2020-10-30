# COVID-19 Statistics
![GitHub Stars](https://img.shields.io/github/stars/StevenHuang2020/WebSpider?label=Stars&style=social)
![GitHub watchers](https://img.shields.io/github/watchers/StevenHuang2020/WebSpider?label=Watch) 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python Version](https://img.shields.io/badge/Python-v3.6-blue)
![Tensorflow Version](https://img.shields.io/badge/Tensorflow-V2.2.0-brightgreen)
![Last update](https://img.shields.io/endpoint?color=brightgreen&style=flat-square&url=https%3A%2F%2Fraw.githubusercontent.com%2FStevenHuang2020%2FWebSpider%2Fmaster%2Fcoronavirus%2Fupdate.json)


The added mortality column calculated by  this: df['Deaths'] / df['Confirmed'].<br/>
Please note that this is not necessarily the correct definition.<br/>
Data Reference: https://google.com/covid19-map/ <br/>
https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv
<br/>
Please report any bugs [here.](https://github.com/StevenHuang2020/COVID-19-Statistics/issues)
#### main_v1.0.py
Using lxml to get data from the website.
<br/>

#### main_v1.2.py
Using selenium to crawl data.
Requirements: pip install selenium. <br/>
Download the proper version of [chromdriver.exe](https://chromedriver.chromium.org/downloads)
then put it into your python install path(.\python36\Scripts\).
<br/>
For detailed statistics of covid-19 in NZ, please refer to 
[here](https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases).

#### main_v1.3.py
Updated to adapt to the new google page.<br/>
<br/>

|||
|---|---|
|<img src="images/nc1.png" width="320" height="240" />|<img src="images/nd2.png" width="320" height="240" />|
|<img src="images/1.png" width="320" height="240" />|<img src="images/2.png" width="320" height="240" />|
|<img src="images/3.png" width="320" height="240" />|<img src="images/4.png" width="320" height="240" />|
|<img src="images/5.png" width="320" height="240" />|<img src="images/6.png" width="320" height="240" />|
|<img src="images/7.png" width="320" height="240" />|<img src="images/8.png" width="320" height="240" />|
|<img src="images/9.png" width="320" height="240" />||
 
<br/>

### Statistics cases by time
<br/>

|||
|---|---|
|<img src="images/countries_Confirmed.png" width="320" height="240" />|<img src="images/countries_Deaths.png" width="320" height="240" />|
|<img src="images/countries_NewConfirmed.png" width="320" height="240" />|<img src="images/countries_NewDeaths.png" width="320" height="240" />|
|<img src="images/countries0_Confirmed.png" width="320" height="240" />|<img src="images/countries0_Deaths.png" width="320" height="240" />|
|<img src="images/countries0_NewConfirmed.png" width="320" height="240" />|<img src="images/countries0_NewDeaths.png" width="320" height="240" />|
|<img src="images/countries1_Confirmed.png" width="320" height="240" />|<img src="images/countries1_Deaths.png" width="320" height="240" />|
|<img src="images/countries1_NewConfirmed.png" width="320" height="240" />|<img src="images/countries1_NewDeaths.png" width="320" height="240" />|
|<img src="images/World_Cases.png" width="320" height="240" />|<img src="images/World_NewCases.png" width="320" height="240" />|
|<img src="images/World_RecentNewCases.png" width="320" height="240" />|<img src="images/World_Deaths.png" width="320" height="240" />|
|<img src="images/World_NewDeaths.png" width="320" height="240" />|<img src="images/World_RecentNewDeaths.png" width="320" height="240" />|
|<img src="images/WorldChange_confirmed.png" width="320" height="240" />|<img src="images/WorldChange_deaths.png" width="320" height="240" />|
|<img src="images/WorldChange_newCases.png" width="320" height="240" />|<img src="images/WorldChange_mortality.png" width="320" height="240" />|
|<img src="images/WorldChange_all.png" width="320" height="240" />||
<br/>

### World Prediction
<br/>
The world predicted confirmed cases by using LSTM algorithm.<br/>
Data Source reference: https://ourworldindata.org/covid-cases<br/>
<br/>

|||
|---|---|
|<img src="images/WorldPredictCompare.png" width="320" height="240" />|<img src="images/WorldFuturePredict.png" width="320" height="240" />|
|<img src="images/WorldFuturePredictPrecise.png" width="320" height="240" />||
|||

### NZ Covid-19 Statistic
<br/>
Source reference: https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases/covid-19-current-cases-details#download<br/>
<br/>

|||
|---|---|
|<img src="images/NZ_Gender.png" width="320" height="240" />|<img src="images/NZ_DHB.png" width="320" height="240" />|
|<img src="images/NZ_AgeGroup.png" width="320" height="240" />|<img src="images/NZ_COVID-19_RecentCases.png" width="320" height="240" />|
|<img src="images/NZ_COVID-19_EveryDayCases.png" width="320" height="240" />|<img src="images/NZ_COVID-19_CumlativeCases.png" width="320" height="240" />|
|<img src="images/NZ_IsOVerseas.png" width="320" height="240" />||
|||

