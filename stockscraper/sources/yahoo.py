import datetime
import requests
import json
from fake_useragent import UserAgent
from .base import AbstractDatasource
from ..interval import Interval
from ..result import ScrapeResult
from ..tick import Tick

class YahooDatasource(AbstractDatasource):
    """
    This class will handle implementing fetching stock data from Yahoo's API
    """

    BASE_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?symbol={symbol}&period1={start_date}&period2={end_date}&useYfid=true&interval={interval}&includePrePost=true"

    def get_ticks(
        self, 
        symbol: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        interval: Interval
    ) -> ScrapeResult:
        """
        Initiate scraping from Yahoo's API

        @param symbol: The symbol to scrape
        @param start_date: The starting timestamp to scrape from
        @param end_date: The ending timestamp to scrape to
        @param interval: The interval of ticks to scrape as an Interval enum
        @return: The scraping results encapsulated in a ScrapeResult instance
        """

        query_url = self.BASE_URL.format(
            symbol=symbol.upper(),
            start_date=start_date.strftime("%s"),
            end_date=end_date.strftime("%s"),
            interval=str(interval)
        )

        result = requests.get(query_url, headers={"User-Agent": UserAgent().random})
        if int(result.status_code/100) != 2:
            raise ValueError(f"An error has occurred attempting to retrieve data from Yahoo:\n{result.text}")

        data = result.json()
        raw_ticks = data["chart"]["result"][0]["indicators"]["quote"][0]

        timestamps = data["chart"]["result"][0]["timestamp"]
        opens = raw_ticks["open"]
        highs = raw_ticks["high"]
        lows = raw_ticks["low"]
        closes = raw_ticks["close"]
        volumes = raw_ticks["volume"]

        ticks = [
            Tick(
                timestamp=timestamps[i],
                open=opens[i],
                high=highs[i],
                low=lows[i],
                close=closes[i],
                volume=volumes[i]
            )
            for i in range(len(timestamps))
        ]

        return ScrapeResult(
            symbol=symbol,
            interval=interval,
            ticks=ticks,
            start_date=start_date,
            end_date=end_date
        )

