"""
`ZettelkastenUniqueIdentifier` module
Implements the `zUID` class for creating a Zettelkasten Unique Identifiers (zUIDs).

@author         rdcn
@version        1.0
@since          1.0
@date           2025-02-13
"""

class zUIDException(Exception):
    """
    The `zUIDException` class for creating exceptions for the `zUID` class.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message);
        


class zUID:
    """
    The `zUID` class for creating a Zettelkasten Unique Identifiers (zUIDs).
    """
    def __init__(self, id: int) -> None:
        """
        Initializes the `zUID` object with the given zUID.
        
        Parameters
        ----------
        id : int
            The zUID to initialize the object with.
        
        Raises
        ------
        zUIDException
            If the zUID is not well-formed.
        """
        self.id = id
        

    def __str__(self) -> str:
        return str(self.id);
    
    
    def __repr__(self) -> str:
        return str(self.id);
    
    
    def __eq__(self, other) -> bool:
        return self.id == other.id;
    
    
    def __ne__(self, other) -> bool:
        return self.id != other.id;
    
    
    def __lt__(self, other) -> bool:
        return self.id < other.id;
    
    
    def __le__(self, other) -> bool:
        return self.id <= other.id;
    
    
    def __gt__(self, other) -> bool:
        return self.id > other.id;
    
    
    def __ge__(self, other) -> bool:
        return self.id >= other.id;
    
    
    def __hash__(self) -> int:
        return hash(self.id);
    
    
    def __int__(self) -> int:
        return int(self.id);
    