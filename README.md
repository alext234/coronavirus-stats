
## Charts and Data on Coronavirus 
This repository contains data in (CSV format) which are scraped from reliable sources (e.g. World Health Organisation).
Data are frequently scraped and pushed back to this repository together with generated charts (.PNG files).


### From WHO (World Health Organisation) Situation reports

#### Globally confirmed cases

[CSV direct link](data/who-global-cases.csv?raw=true)

![](images/who-global-cases.png?raw=true)


## How does this work

* Jupypter notebooks are used for scraping data and output to CSV files
* These notebooks are scheduled to be executed by Github Actions pipeline to scrape new data
* This pipeline also commits back new data to this repository


## Development 


* Tools: Python3, Jupyter, Pandas and related stuff. Here is one way to have them with this docker image

```
docker run --user root -it -v $PWD:/temp1 jupyter/datascience-notebook bash
```


* `requirements.txt` contains the dependencies

```
pip install -r requirements.txt
```

## Contributions

* Feel free to create new issues for any potential data source worth scraping.
* Pull requests are welcomed!
