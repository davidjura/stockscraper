import datetime
import inspect
from typing import Optional, Union
from dateutil.parser import parse as parse_timestamp
from .sources import datasource_mapping, default_datasource
from .sources.base import AbstractDatasource
from .interval import Interval
from .result import ScrapeResult

def scrape(
    symbol: str,
    start_date: Optional[Union[datetime.datetime, str]] = None,
    end_date: Optional[Union[datetime.datetime, str]] = None,
    days: Optional[int] = 1,
    interval: Optional[Union[Interval, str]] = Interval.ONE_DAY,
    datasource: Optional[Union[AbstractDatasource, str]] = default_datasource,
) -> ScrapeResult:
    """
    Initiate a stock scrape

    @param symbol: The stock symbol to scrape
    @param start_date: The start timestamp to scrape from
    @param end_date: The end timestamp to scrape to
    @param days: Optional variable to scrape the last x days if start or end date are not specified
    @param interval: The interval to scrape
    @param datasource: The datasource to utilize
    @return The scraped stock data as a ScrapeResult instance
    """

    if not symbol:
        raise ValueError("Please provide a valid symbol")

    if isinstance(start_date, str):
        start_date = parse_timestamp(start_date)
    if isinstance(end_date, str):
        end_date = parse_timestamp(end_date)

    if not end_date:
        end_date = datetime.datetime.now()
    if not start_date:
        start_date = end_date - datetime.timedelta(days=max(days or 1, 1)) # type: ignore

    if isinstance(interval, str):
        interval = Interval.from_str(interval)


    supported_datasources = [str(k) for k in datasource_mapping.keys()]
    if isinstance(datasource, str):
        if datasource not in datasource_mapping:
            raise ValueError(
                f"'{datasource}' is not a valid or supported datasource. Supported: {', '.join(supported_datasources)}"
            )
        datasource = datasource_mapping[datasource]
    if inspect.isclass(datasource) and issubclass(datasource, AbstractDatasource):
        datasource = datasource() # type: ignore
    if not isinstance(datasource, AbstractDatasource):
        raise ValueError(
            f"'{datasource}' is not a valid or supported datasource. Supported: {', '.join(supported_datasources)}"
        )

    return datasource.get_ticks(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        interval=interval
    )
