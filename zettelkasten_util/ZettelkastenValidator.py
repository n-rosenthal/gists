"""
`ZettelkastenValidator` module
Static methods for validating Zettelkasten Unique Identifiers (ZUIDs).

@author         rdcn
@version        1.0
@since          1.0
@date           2025-02-13
"""

from typing import Tuple, List, TypeVar;
from ZettelkastenDecomposer import ZettelkastenDecomposer as decomposer;
from datetime import datetime;

#   Zettelkasten Unique Identifier
zUID = TypeVar("zUID");

class ZettelkastenValidator:
    """
    Static methods for validating Zettelkasten Unique Identifiers (ZUIDs).
    """
    @staticmethod
    def validate(id: int | str | datetime | zUID) -> bool:
        """
        Validates a Zettelkasten Unique Identifier (ZUID) by checking if it is well-formed.
        
        Parameters
        ----------
        id : int | str | datetime | "zUID"
            The ZUID to validate.
            
        Returns
        -------
        bool
            `True` if the ZUID is well-formed, `False` otherwise.
        """
        try:
            year, month, day, hour, minute = decomposer.decompose(id);
            
            if ZettelkastenValidator.validate_year(year) and ZettelkastenValidator.validate_month(month) and ZettelkastenValidator.validate_day(day) and ZettelkastenValidator.validate_hour(hour) and ZettelkastenValidator.validate_minute(minute):
                return True;
            else:
                return False;
        except:
            return False;
        
    @staticmethod
    def find_error(id: int | str | datetime | zUID) -> List[str]:
        try:
            year, month, day, hour, minute = decomposer.decompose(id);
            err = [];
            
            if not ZettelkastenValidator.validate_year(year):
                err.append(f"Year {year} is not between 1970 and 2170.");
            if not ZettelkastenValidator.validate_month(month):
                err.append(f"Month {month} is not between 1 and 12.");
            if not ZettelkastenValidator.validate_day(day):
                err.append(f"Day {day} is not between 1 and 31.");
            if not ZettelkastenValidator.validate_hour(hour):
                err.append(f"Hour {hour} is not between 0 and 23.");
            if not ZettelkastenValidator.validate_minute(minute):
                err.append(f"Minute {minute} is not between 0 and 59.");
            
            if len(err) == 0:
                return ["The given argument is a valid Zettelkasten Unique Identifier (ZUID)."];    
            return err;
        except Exception as e:
            return ["The given argument is not a well-formed Zettelkasten Unique Identifier (ZUID).",
                    e.__class__.__name__ + ": " + str(e)];
        
        
    @staticmethod
    def validate_year(year: int) -> bool:
        return 1970 <= year <= 2170;
    
    @staticmethod
    def validate_month(month: int) -> bool:
        return 1 <= month <= 12;
    
    @staticmethod
    def validate_day(day: int) -> bool:
        return 1 <= day <= 31;
    
    @staticmethod
    def validate_hour(hour: int) -> bool:
        return 0 <= hour <= 23;
    
    @staticmethod
    def validate_minute(minute: int) -> bool:
        return 0 <= minute <= 59;