# Stockscraper
A stock market scraping CLI utility that downloads intraday data to CSV or JSON files

### Requirements
* python >= 3.8

### Supported Datasources (more to come)
* Yahoo Finance

### Installation Instructions
```
git clone https://github.com/davidjura/stockscraper.git
cd stockscraper
pip install -e .
```

### Usage Instructions
```
usage: stock-scraper [-h] [--format [csv|json]] [--output OUTPUT_FILE_PATH]
                     [--interval [1m|5m|15m|30m|1h|4h|1d|1w|1M|1y]]
                     [--start-date YYYY-MM-DD HH:MM:SS]
                     [--end-date YYYY-MM-DD HH:MM:SS] [--days DAYS]
                     [--datasource [yahoo]]
                     SYMBOL

Download historical stock data to CSV or JSON files

positional arguments:
  SYMBOL                The stock ticker symbol to download

optional arguments:
  -h, --help            show this help message and exit
  --format [csv|json], -f [csv|json]
                        The file format to download data. Default = csv
  --output OUTPUT_FILE_PATH, -o OUTPUT_FILE_PATH
                        The output file path to write the scraped data to
  --interval [1m|5m|15m|30m|1h|4h|1d|1w|1M|1y], -i [1m|5m|15m|30m|1h|4h|1d|1w|1M|1y]
                        The ticker interval to use
  --start-date YYYY-MM-DD HH:MM:SS, -s YYYY-MM-DD HH:MM:SS
                        The start date/time to scrape from
  --end-date YYYY-MM-DD HH:MM:SS, -e YYYY-MM-DD HH:MM:SS
                        The end date/time to scrape to
  --days DAYS, -d DAYS  Optionally scrape data from the last x days as opposed
                        to specifying a start and end date
  --datasource [yahoo], -D [yahoo]
                        Optionally specify datasource. Using 'yahoo' by
                        default
```

### Example CLI Command
* Download 1-minute ticker intervals over the last 2 days for SPY and write it to a CSV file
> `stock-scraper SPY --format csv --interval 1m --days 2 --output result.csv`
