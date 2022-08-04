import datetime
from dateutil.parser import parse as parse_datetime
from collections import OrderedDict
from typing import Dict, List, Union

class Tick(object):
    """
    Encapsulate scraped data into it's own object
    
    @param timestamp: The timestamp of the tick as an int epoch, datetime object, or string
    @param open: The open price of the tick
    @param high: The high price of the tick
    @param low: The low price of the tick
    @param close: The close price of the tick
    @param volume: The volume of the tick
    """

    def __init__(
        self, 
        timestamp: Union[datetime.datetime, int, str],
        open: float,
        high: float,
        low: float,
        close: float,
        volume: int
    ):
        if not isinstance(timestamp, datetime.datetime):
            if isinstance(timestamp, (int, float)):
                timestamp = datetime.datetime.fromtimestamp(timestamp)
            elif isinstance(timestamp, str):
                try:
                    timestamp = datetime.datetime.fromtimestamp(float(timestamp))
                except:
                    timestamp = parse_datetime(timestamp)

        self.timestamp = timestamp
        self.open = float(open) if open is not None else None
        self.high = float(high) if open is not None else None
        self.low = float(low) if low is not None else None
        self.close = float(close) if close is not None else None
        self.volume = int(volume) if volume is not None else None

    @property
    def as_list(self) -> List:
        """
        Retrieve the tick data as a list of the timestamp, open price, high price,
        low price, close price, and volume

        @return: [timestamp, open price, high price, low price, close price, volume]
        """

        return [self.timestamp, self.open, self.high, self.low, self.close, self.volume]

    @property
    def as_dict(self) -> Dict:
        """
        Retrieve the tick data as a dictionary

        @return: {timestamp, open, high, low, close, volume}
        """

        return OrderedDict(
            timestamp=self.timestamp,
            open=self.open,
            high=self.high,
            low=self.low,
            close=self.close,
            volume=self.volume
        )
