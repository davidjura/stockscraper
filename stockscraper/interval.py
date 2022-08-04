from enum import Enum

class Interval(Enum):
    """
    This enum will allow us to define the different types of
    support time intervals
    """

    ONE_MINUTE = "1m"
    FIVE_MINUTE = "5m"
    FIFTEEN_MINUTE = "15m"
    THIRTY_MINUTE = "30m"
    ONE_HOUR = "1h"
    FOUR_HOUR = "4h"
    ONE_DAY = "1d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1M"
    ONE_YEAR = "1y"

    def __str__(self):
        """
        Override to-string method to return the value of the enum
        @return: The string value of the enum
        """

        return str(self.value)

    @classmethod
    def from_str(cls, value:str) -> "Interval":
        """
        Infer the enum using its string value

        @param value: The enum string value
        @return: The interval object 
        """

        for v in cls.__members__.values():
            if v.value == value:
                return v
        raise ValueError(f"'{value}' is not a valid interval. Please chose from {', '.join(cls.__members__.keys())}")
