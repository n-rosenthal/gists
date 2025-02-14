"""
`ZettelkastenBuilder` module
Implements the `ZettelkastenBuilder` class for creating a Zettelkasten Unique Identifiers (ZUIDs).

@author         rdcn
@version        1.0
@since          1.0
@date           2025-02-13
"""

import datetime;
from typing import List, Tuple, Any, TypeVar;
from engine.ZettelkastenValidator import ZettelkastenValidator as validator;
from data.ZettelkastenUniqueIdentifier import zUID;


#   Exception class for Zettelkasten Unique Identifiers (ZUIDs)
zUIDException = TypeVar("zUIDException");

class ZettelkastenBuilder:
    """
    The `ZettelkastenBuilder` class for creating a Zettelkasten Unique Identifiers (ZUIDs).
    """
    
    @staticmethod
    def build(id: int | str | datetime.datetime) -> zUID:
        """
        Creates a Zettelkasten Unique Identifier (ZUID) from an integer, string or datetime object.
        
        Parameters
        ----------
        id : int | str | datetime
            The integer, string or datetime object to create the ZUID from.
            
        Returns
        -------
        zUID
            The created ZUID.
        """
        if isinstance(id, int):
            return ZettelkastenBuilder.from_int(id);
        elif isinstance(id, str):
            return ZettelkastenBuilder.from_string(id);
        elif isinstance(id, datetime.datetime):
            return ZettelkastenBuilder.from_datetime(id);
        else:
            raise zUIDException("The given argument is not a valid Zettelkasten Unique Identifier (ZUID).");
    
    @staticmethod
    def from_int(id: int) -> zUID:
        """
        Creates a Zettelkasten Unique Identifier (ZUID) from an integer.
        
        Parameters
        ----------
        id : int
            The integer to create the ZUID from.
        
        Returns
        -------
        zUID
            The created ZUID.
        """
        #   Check for validity of ZUID
        if validator.validate(id) == True:
            return zUID(id);
        else:
            raise zUIDException("\n".join(validator.find_error(id)));
        
    @staticmethod
    def from_string(id: str) -> zUID:
        """
        Creates a Zettelkasten Unique Identifier (ZUID) from a string.
        
        Parameters
        ----------
        id : str
            The string to create the ZUID from.
        
        Returns
        -------
        zUID
            The created ZUID.
        """
        #   If the integer is shorter than 12 characters, append zeros to the right
        id_int : int = int(id);
        
        if len(str(id_int)) < 12:
            id_int = id_int * 10 ** (12 - len(str(id_int)));
        
        return ZettelkastenBuilder.from_int(id_int);
    
    @staticmethod
    def from_datetime(id: datetime) -> zUID:
        """
        Creates a Zettelkasten Unique Identifier (ZUID) from a datetime object.
        
        Parameters
        ----------
        id : datetime
            The datetime object to create the ZUID from.
        
        Returns
        -------
        zUID
            The created ZUID.
        """
        return ZettelkastenBuilder.from_int(int(id.strftime("%Y%m%d%H%M")));


def build_from_datetime(id: datetime) -> zUID:
    """
    Exportable function for use in other modules.
    Creates a Zettelkasten Unique Identifier (ZUID) from a datetime object.
    
    Parameters
    ----------
    id : datetime
        The datetime object to create the ZUID from.
        
    Returns
    -------
    zUID
        The created ZUID.
    """
    return ZettelkastenBuilder.from_datetime(id);