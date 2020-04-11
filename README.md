# lsra-scraper

[![GitHub last commit](https://img.shields.io/github/last-commit/houfu/lsra-scraper)](https://github.com/houfu/lsra-scraper)

Obtains a list of law practices in Singapore from the [Legal Services Regulatory Authority Home](https://eservices.mlaw.gov.sg/lsra/search-lawyer-or-law-firm). 

## Features

Output: _comma separated values (CSV) files._

* Name of Law Practice
* Type of Law Practice (Singapore law practice, foreign law practice)
* Key practice areas: a list of practice areas as provided by the law firm
* Size of law practice (1-5 lawyers etc)
* Telephone number, website, email address (as provided by the law practices)

## Install

* Install via PIP

```shell script
pip install lsra-scraper
```

* Once the package is installed, use the command line tool `lsra_scraper` to use the script.

* If necessary, install [Chrome](https://www.google.com/chrome/) 
and [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Selenium to work.

## Usage

As the script can only be used for scraping law firms, 
passing no arguments to the script will result in the default behaviour 
(ie. scrapes the law firms and render output by csv).

Type `--help` option to see a full list of options.

**The script is not fully automated!!** 
You need to pass captcha in order to scrape the website contents.
Follow the directions in the console to do this.

## Contact

Please feel free to  
[email me](mailto:houfu@outlook.sg). 
It would be nice to know how you use the data collected using this script.
Comments, suggestions and other feedback is also welcomed.