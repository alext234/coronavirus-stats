
## Charts and Data on Coronavirus 
This repository contains data in (CSV format) which are scraped from reliable sources (e.g. World Health Organisation).
Data are frequently scraped and pushed back to this repository together with generated charts (.PNG files).


### From WHO (World Health Organisation) Situation reports
[These reports](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/) are in PDF formats. New reports are released daily.


#### Globally confirmed cases

[CSV direct link](data/who-global-cases.csv?raw=true)

![](images/who-global-cases.png?raw=true)

### From US CDC (Centers for Disease Control and Prevention)

#### [Cases in the US](https://www.cdc.gov/coronavirus/2019-ncov/cases-in-us.html)

[CSV direct link](data/cdc-us-cases.csv?raw=true)

![](images/cdc-us-cases.png?raw=true)


### More data to come...


## How it works

* Jupyter notebooks are used for scraping data and output to CSV files
* These notebooks are executed on a schedule by Github Actions pipeline to scrape new data
* This pipeline also commits back new data to this repository


## Development 


* Tools: Python3, Jupyter, Pandas and related stuff. Here is one way to have them with this docker image

```
docker run --user root -it -v $PWD:/stats jupyter/datascience-notebook bash
```


* [requirements.txt](requirements.txt) contains Python dependencies

```
pip install -r requirements.txt
```

## Contributions

* Feel free to create new issues for any potential data source worth scraping.
* Pull requests are welcomed!
