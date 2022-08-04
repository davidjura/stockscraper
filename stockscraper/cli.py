import argparse
import sys
from .scraper import scrape
from .sources import default_datasource, datasource_mapping
from .interval import Interval

def main():
    """
    usage: stock-scraper [-h] [--format [csv|json]]
                         [--interval [1m|5m|15m|30m|1h|4h|1d|1w|1M|1y]]
                         [--start-date YYYY-MM-DD HH:MM:SS]
                         [--end-date YYYY-MM-DD HH:MM:SS]
                         symbol

    CLI entry-point for to download historical stock data to CSV or JSON files.

    positional arguments:
      symbol                The stock ticker symbol to download

    optional arguments:
      -h, --help            show this help message and exit
      --format [csv|json], -f [csv|json]
                            The file format to download data. Default = csv
      --interval [1m|5m|15m|30m|1h|4h|1d|1w|1M|1y], -i [1m|5m|15m|30m|1h|4h|1d|1w|1M|1y]
                            The ticker interval to use
      --start-date YYYY-MM-DD HH:MM:SS, -s YYYY-MM-DD HH:MM:SS
                            The start date/time to scrape from
      --end-date YYYY-MM-DD HH:MM:SS, -e YYYY-MM-DD HH:MM:SS
                            The end date/time to scrape to
    """

    interval_options = [str(v.value) for v in Interval.__members__.values()]
    datasource_options = [str(k) for k in datasource_mapping.keys()]
    default_datasource_name = [k for k,v in datasource_mapping.items() if v == default_datasource][0]

    parser = argparse.ArgumentParser(prog="stock-scraper", description="Download historical stock data to CSV or JSON files")
    parser.add_argument("symbol", metavar="SYMBOL", help="The stock ticker symbol to download")
    parser.add_argument("--format", "-f", metavar="[csv|json]", default="csv", help="The file format to download data. Default = csv")
    parser.add_argument("--output", "-o", metavar="OUTPUT_FILE_PATH", help="The output file path to write the scraped data to")
    parser.add_argument("--interval", "-i", metavar=f"[{'|'.join(interval_options)}]", help="The ticker interval to use")
    parser.add_argument("--start-date", "-s", metavar="YYYY-MM-DD HH:MM:SS", required=False, help="The start date/time to scrape from")
    parser.add_argument("--end-date", "-e", metavar="YYYY-MM-DD HH:MM:SS", required=False, help="The end date/time to scrape to")
    parser.add_argument("--days", "-d", type=int, metavar="DAYS", required=False, help="Optionally scrape data from the last x days as opposed to specifying a start and end date")
    parser.add_argument("--datasource", "-D", metavar=f"[{'|'.join(datasource_options)}]", required=False, default=default_datasource_name, help=f"Optionally specify datasource. Using '{default_datasource_name}' by default")
    args = parser.parse_args()

    symbol = args.symbol
    format = args.format
    output_file = args.output
    interval = args.interval
    start_date = args.start_date
    end_date = args.end_date
    datasource = args.datasource
    days = args.days

    if format.lower() not in ("csv", "json"):
        print(f"'{format}' is not a valid format. Please use either 'csv' or 'json'\n")
        parser.print_help()
        sys.exit(2)

    if interval not in interval_options:
        print(f"'{interval}' is not a valid interval. Please choose from: {', '.join(interval_options)}\n")
        parser.print_help()
        sys.exit(2)

    if datasource not in datasource_options:
        print(f"'{datasource}' is not a valid datasource. Please choose from: {', '.join(datasource_options)}\n")
        parser.print_help()
        sys.exit(2)


    
    # try:
    result = scrape(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        days=days,
        interval=interval,
        datasource=datasource,
    )
    with open(output_file, "w") as out:
        out.write(result.as_csv if format.lower() == "csv" else result.as_json)
    # except Exception as e:
    #     print(e)
    #     sys.exit(1)

if __name__ == "__main__":
    main()
