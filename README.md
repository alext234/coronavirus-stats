

![Top 10](https://img.shields.io/endpoint?color=blue&style=flat-square&url=https%3A%2F%2Fraw.githubusercontent.com%2Falext234%2Fcoronavirus-stats%2Fmaster%2Fdata%2Ftop10.json)


# Charts and Data on Coronavirus (COVID-19)
This repository contains data in (CSV format) which are scraped from reliable sources (e.g. World Health Organisation).

* Data are scraped a few times daily and pushed back to this repository together with generated charts (.PNG files).

* Data scraping are automated with [Github Actions](https://github.com/features/actions).

* Look for those **CSV direct link** below to get the scraped historical data.

* Another repository related to news scraping is available at https://github.com/alext234/coronavirus-news/blob/master/README.md


## Aggregate sites


### [BNO News](https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/)

Below are international stats, excluding China.

[CSV direct link](data/bnonews-international.csv?raw=true)

Bar chart of the latest snapshot.

![](images/bnonews-international.png?raw=true)



## WHO & Government sites 

### From WHO (World Health Organisation) Situation reports
Data are scraped from [these reports](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/) which are in PDF formats. New reports are released daily.


#### Globally confirmed cases

[CSV direct link](data/who-global-cases.csv?raw=true)

![](images/who-global-cases.png?raw=true)

### Stats from China
[This page](https://ncov.dxy.cn/ncovh5/view/pneumonia) has the realtime stats from China. Data are pulled several times a day by the pipeline.

#### All cases in China

[CSV direct link](data/china-summary-cases.csv?raw=true)

![](images/china-summary-cases.png?raw=true)


### Stats from Australia

Data is pulled from Department of Health [website](https://www.health.gov.au/news/coronavirus-update-at-a-glance).

#### Cases in Australia

[CSV direct link](data/australia-cases.csv?raw=true)


### Stats from Singapore

Data are scraped from the MOH (Ministry of Health) local situation [web page](https://www.moh.gov.sg/2019-ncov-wuhan).

#### Cases in Singapore

[CSV direct link](data/singapore-cases.csv?raw=true)




### From US CDC (Centers for Disease Control and Prevention)

#### Cases in the US (data are scraped from [here](https://www.cdc.gov/coronavirus/2019-ncov/cases-in-us.html))

[CSV direct link](data/cdc-us-cases.csv?raw=true)

Chart for US is not plotted due to change in the way stats are collected.



# How it works

* Jupyter notebooks are used for scraping data and output to CSV files
* These notebooks are executed on a schedule by Github Actions pipeline to scrape new data
* This pipeline also commits back new data to this repository


# Development 


* Tools: Python3, Jupyter, Pandas, BeautifulSoup and related stuff (e.g. Selenium for web-scraping). 
It is recommended to start the development environment with this docker image, which is also used for the Github Actions build pipeline.

```
docker run  -p 8888:8888 -it -v $PWD:/stats -w /stats alext234/datascience:latest  bash 
```


* [requirements.txt](requirements.txt) contains Python dependencies

```
pip install -r requirements.txt
```

* Start Jupyter notebook from inside the container and then visit the browser at `http://localhost:8888`

```
jupyter notebook --allow-root --ip=0.0.0.0

```

## Contributions

* Feel free to create new issues for any potential data source worth scraping.
* Pull requests are welcomed!


## Repo status and stats
* Stargazers


![GitHub stars](https://img.shields.io/github/stars/alext234/coronavirus-stats?style=social)

* Last update from pipeline

![Last update](https://img.shields.io/endpoint?color=blue&style=flat-square&url=https%3A%2F%2Fraw.githubusercontent.com%2Falext234%2Fcoronavirus-stats%2Fmaster%2Fdata%2Flast_update.json)

* Pipeline status


![Run notebooks and commit back data/charts](https://github.com/alext234/coronavirus-stats/workflows/Run%20notebooks%20and%20commit%20back%20data/charts/badge.svg?branch=master) 
