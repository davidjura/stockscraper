import csv
import json
import datetime
import pandas
from typing import Dict, List
from collections import OrderedDict
from io import StringIO
from .interval import Interval
from .tick import Tick

class ScrapeResult(object):
    """
    Enapsulate the scrape results into it's own object

    @param symbol: The stock symbol string
    @param interval: The intervale enum
    @param ticks: A list of Tick object instances
    @param start_date: The timestamp of where the scraping starts
    @param end_date: The timestamp of where the scrapin ends
    """

    def __init__(
        self,
        symbol: str,
        interval: Interval,
        ticks: List[Tick],
        start_date: datetime.datetime,
        end_date: datetime.datetime
    ):
        self.symbol = str(symbol).upper()
        self.interval = interval
        self.ticks = ticks
        self.start_date = str(start_date)
        self.end_date = str(end_date)

    @property
    def as_dict(self) -> Dict:
        """
        Convert the results into a dictionary

        @return: The scrape results as a dictionary
        """
        return OrderedDict(
            symbol=self.symbol,
            start_date=self.start_date,
            end_date=self.end_date,
            interval=self.interval,
            ticks=[t.as_dict for t in self.ticks]
        )

    @property
    def as_json(self) -> str:
        """
        Convert the scrape results to a JSON string

        @return: The JSON string of the scraped results
        """

        return json.dumps(self.as_dict, default=str)
        
    @property
    def as_csv(self) -> str:
        """
        Convert the scrape results to a CSV string

        @return A CSV string with the timestamp, open, high, low, close, and volume as
            the data headers
        """

        csv_buff = StringIO()
        writer = csv.writer(
            csv_buff,
            quoting=csv.QUOTE_NONNUMERIC,
        )
        writer.writerows(
            [["timestamp", "open", "high", "low", "close", "volume"]] + [
                t.as_list for t in self.ticks
            ]

        )
        csv_buff.seek(0)
        return csv_buff.read()

    @property
    def as_pandas(self) -> pandas.DataFrame:
        """
        Convert the scrape results to a pandas DataFrame

        @return: The tick results represented as a Pandas DataFrame
        """
        timestamp = []
        open = []
        high = []
        low = []
        close = []
        volume = []

        for tick in self.ticks:
            timestamp.append(tick.timestamp)
            open.append(tick.open)
            high.append(tick.high)
            low.append(tick.low)
            close.append(tick.close)
            volume.append(tick.volume)

        return pandas.DataFrame(OrderedDict(
            timestamp=timestamp,
            open=open,
            high=high,
            low=low,
            close=close,
            volume=volume
        ))
