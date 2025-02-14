"""
`ZettelkastenBuilder` module
Implements the `ZettelkastenBuilder` class for creating a Zettelkasten Unique Identifiers (ZUIDs).

@author         rdcn
@version        1.0
@since          1.0
@date           2025-02-13
"""

import hashlib
import datetime;
import json;
from ZettelkastenUniqueIdentifier import zUID, zUIDException;
from ZettelkastenCounter import ZettelkastenCounter as counter;
from ZettelkastenValidator import ZettelkastenValidator as validator;

class ZettelkastenBuilder:
    """
    The `ZettelkastenBuilder` class for creating a Zettelkasten Unique Identifiers (ZUIDs).
    """
    
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
        return ZettelkastenBuilder.from_int(int(id));
    
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
    