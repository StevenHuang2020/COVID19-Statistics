# COVID-19 Statistics :grinning::+1:
![GitHub Stars](https://img.shields.io/github/stars/StevenHuang2020/WebSpider?label=Stars&style=social)
![GitHub watchers](https://img.shields.io/github/watchers/StevenHuang2020/WebSpider?label=Watch) 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python Version](https://img.shields.io/badge/Python-v3.6-blue)
![Tensorflow Version](https://img.shields.io/badge/Tensorflow-V2.2.0-brightgreen)
![Last update](https://img.shields.io/endpoint?color=brightgreen&style=flat-square&url=https%3A%2F%2Fraw.githubusercontent.com%2FStevenHuang2020%2FWebSpider%2Fmaster%2Fcoronavirus%2Fupdate.json)


The added mortality column calculated by  this: df['Deaths'] / df['Confirmed'].<br/>
Please note that this is not necessarily the correct definition.<br/>
Reference: https://google.com/covid19-map/ <br/>
https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv

#### main.py
Using lxml to get data from website.
<br/>

#### main_v1.2.py
Using selenium to crawl data.
Requirment: pip install selenium. <br/>
Download proper verison of [chromdriver.exe](https://chromedriver.chromium.org/downloads)
then put it in to your python install path(.\python36\Scripts\).
<br/>
For detailed statistics of covid-19 in NZ, please refer to 
[here](https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases).

#### main_v1.3.py
Updated to adapt to the new google page.<br/>
<br/>

<table>
  <tr>
    <td><img src="images/nc1.png" width="320" height="240" /></td>
    <td><img src="images/nd2.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/1.png" width="320" height="240" /></td>
    <td><img src="images/2.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/3.png" width="320" height="240" /></td>
    <td><img src="images/4.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/5.png" width="320" height="240" /></td>
    <td><img src="images/6.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/7.png" width="320" height="240" /></td>
    <td><img src="images/8.png" width="320" height="240" /></td>
  </tr>
 </table>
 
<br/>

#### Statistics cases by time.
<br/>
<table>
  <tr>
    <td><img src="images/countries_Confirmed.png" width="320" height="240" /></td>
    <td><img src="images/countries_Deaths.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/countries_NewConfirmed.png" width="320" height="240" /></td>
    <td><img src="images/countries_NewDeaths.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/countries0_Confirmed.png" width="320" height="240" /></td>
    <td><img src="images/countries0_Deaths.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/countries0_NewConfirmed.png" width="320" height="240" /></td>
    <td><img src="images/countries0_NewDeaths.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/countries1_Confirmed.png" width="320" height="240" /></td>
    <td><img src="images/countries1_Deaths.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/countries1_NewConfirmed.png" width="320" height="240" /></td>
    <td><img src="images/countries1_NewDeaths.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/World_Cases.png" width="320" height="240" /></td>
    <td><img src="images/World_newCases.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/World_recentNewCases.png" width="320" height="240" /></td>
    <td><img src="images/World_Deaths.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/World_NewDeaths.png" width="320" height="240" /></td>
    <td><img src="images/World_RecentNewDeaths.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/WorldChange.png" width="320" height="240" /></td>
  </tr>
  
 </table>
<br/>

#### Prediction
<br/>
World predicted confirmed cases by using LSTM algorithm.<br/>
Source reference: https://ourworldindata.org/covid-cases<br/>
<br/>

<table>
  <tr>
    <td><img src="images/WorldPredictCompare.png" width="320" height="240" /></td>
    <td><img src="images/WorldFuturePredict.png" width="320" height="240" /></td>
  </tr>
  <tr>
    <td><img src="images/WorldFuturePredictPrecise.png" width="320" height="240" /></td>
  </tr>
</table>