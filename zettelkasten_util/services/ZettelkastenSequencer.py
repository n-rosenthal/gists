"""
`ZettelkastenSequencer` module
Implements the `ZettelkastenSequencer` class as a service.
The sequencer is responsible for generating the next and previous zUIDs of a given zUID.

@author         rdcn
@version        1.1
@since          1.1
@date           2025-02-14
"""

from typing import List, Tuple, TypeVar, Any, Callable;
import datetime

#   Zettelkasten Unique Identifier
zUID = TypeVar("zUID");

#   `decompose(id: int | str | datetime)` method of the `ZettelkastenDecomposer` class
from engine.ZettelkastenDecomposer import decompose;

#   `build_from_datetime(id: datetime)` method of the `ZettelkastenBuilder` class
from engine.ZettelkastenBuilder import build_from_datetime as build;

class ZettelkastenSequencer:
    """
    `ZettelkastenSequencer` class.
    
    static methods
    --------------
    get_next(id: int | str | datetime | "zUID") -> "zUID"
        Returns the next zUID of the given zUID.
    get_previous(id: int | str | datetime | "zUID") -> "zUID"
        Returns the previous zUID of the given zUID.
    """
    @staticmethod
    def get_next(id: int | str | datetime.datetime | zUID) -> zUID:
        """
        Returns the next zUID of the given zUID.
        
        Parameters
        ----------
        id : int | str | datetime | "zUID"
            The zUID to get the next zUID of.
            
        Returns
        -------
        "zUID" | None
            The next zUID of the given zUID.
        """
        if not id:
            return None;
        dt : datetime.datetime = datetime.datetime(*decompose(id));
        return build(dt + datetime.timedelta(minutes=1));
    
    @staticmethod
    def get_previous(id: int | str | datetime.datetime | zUID) -> zUID:
        """
        Returns the previous zUID of the given zUID.
        
        Parameters
        ----------
        id : int | str | datetime | "zUID"
            The zUID to get the previous zUID of.
            
        Returns
        -------
        "zUID" | None
            The previous zUID of the given zUID.
        """
        if not id:
            return None;
        dt : datetime.datetime = datetime.datetime(*decompose(id));
        return build(dt - datetime.timedelta(minutes=1));
        
        