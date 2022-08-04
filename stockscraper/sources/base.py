import datetime
from io import StringIO
from abc import ABC, abstractmethod
from collections import OrderedDict
from ..interval import Interval
from ..tick import Tick
from ..result import ScrapeResult

class AbstractDatasource(ABC):
    """
    Defines the abstract class and methods for a datasource
    """

    @abstractmethod
    def get_ticks(
        self, 
        symbol: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        interval: Interval
    ) -> ScrapeResult:
        """
        Implementation should initiate scraping from the given datasource

        @param symbol: The symbol to scrape
        @param start_date: The starting timestamp to scrape from
        @param end_date: The ending timestamp to scrape to
        @param interval: The interval of ticks to scrape as an Interval enum
        @return: The scraping results encapsulated in a ScrapeResult instance
        """

        raise NotImplementedError
