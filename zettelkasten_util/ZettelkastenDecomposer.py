"""
`ZettelkastenDecomposer` module

Implements the `ZettelkastenDecomposer` class for decomposing a Zettelkasten Unique Identifier (ZUID) into its components (year, month, day, hour, minute).

@author         rdcn
@version        1.0
@since          1.0
@date           2025-02-13
"""

from typing import Tuple, TypeVar;
from datetime import datetime;

#   Zettelkasten Unique Identifier
zUID = TypeVar("zUID");

class ZettelkastenDecomposer:
    @staticmethod
    def decompose(id: int | str | datetime | zUID) -> Tuple[int, int, int, int, int]:
        """
        Decomposes a Zettelkasten Unique Identifier (ZUID) into its components.
        
        Parameters
        ----------
        id : int | str | datetime | "zUID"
            The ZUID to decompose.
            
        Returns
        -------
        Tuple[int, int, int, int, int]
            A tuple containing the year, month, day, hour, and minute components of the ZUID.
        """
        if isinstance(id, int):
            return ZettelkastenDecomposer.decompose_int(id);
        elif isinstance(id, str):
            return ZettelkastenDecomposer.decompose_string(id);
        elif isinstance(id, datetime):
            return ZettelkastenDecomposer.decompose_datetime(id);
        elif isinstance(id, zUID):
            return ZettelkastenDecomposer.decompose_int(id.id);
        else:
            raise TypeError("The given argument is not a valid Zettelkasten Unique Identifier (ZUID).");
        
    @staticmethod
    def decompose_int(id: int) -> Tuple[int, int, int, int, int]:
        """
        Decomposes a Zettelkasten Unique Identifier (ZUID) into its components.
        
        Parameters
        ----------
        id : int
            The ZUID to decompose.
            
        Returns
        -------
        Tuple[int, int, int, int, int]
            A tuple containing the year, month, day, hour, and minute components of the ZUID.
        """
        return int(str(id)[0:4]), int(str(id)[4:6]), int(str(id)[6:8]), int(str(id)[8:10]), int(str(id)[10:12]);
    
    @staticmethod
    def decompose_string(id: str) -> Tuple[int, int, int, int, int]:
        """
        Decomposes a Zettelkasten Unique Identifier (ZUID) into its components.
        
        Parameters
        ----------
        id : str
            The ZUID to decompose.
            
        Returns
        -------
        Tuple[int, int, int, int, int]
            A tuple containing the year, month, day, hour, and minute components of the ZUID.
        """
        return int(id[0:4]), int(id[4:6]), int(id[6:8]), int(id[8:10]), int(id[10:12]);
    
    @staticmethod
    def decompose_datetime(id: datetime) -> Tuple[int, int, int, int, int]:
        """
        Decomposes a Zettelkasten Unique Identifier (ZUID) into its components.
        
        Parameters
        ----------
        id : datetime
            The ZUID to decompose.
            
        Returns
        -------
        Tuple[int, int, int, int, int]
            A tuple containing the year, month, day, hour, and minute components of the ZUID.
        """
        return id.year, id.month, id.day, id.hour, id.minute;