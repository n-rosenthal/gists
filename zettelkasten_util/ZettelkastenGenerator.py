"""
`ZettelkastenGenerator` module
Main module for generating Zettelkasten Unique Identifiers (zUIDs).
This class should be used for all Zettelkasten operations. It allows:

-   Create a Zettelkasten Unique Identifier (zUID) from the current date and time.
-   Creating a Zettelkasten Unique Identifier (zUID) from an integer, string or datetime object.
-   Decomposing a Zettelkasten Unique Identifier (zUID) into its components (year, month, day, hour, minute).
-   Validating a Zettelkasten Unique Identifier (zUID) by checking if it is well-formed.
-   Getting the previous and next zUIDs of a given zUID.

@author         rdcn
@version        1.1
@since          1.1
@date           2025-02-14
"""

#   Zettelkasten Unique Identifier (zUID) class
from data.ZettelkastenUniqueIdentifier  import zUID;

#   Engine: validator, decomposer and builder
from engine.ZettelkastenValidator       import ZettelkastenValidator as validator;
from engine.ZettelkastenDecomposer      import ZettelkastenDecomposer as decomposer;
from engine.ZettelkastenBuilder         import ZettelkastenBuilder as builder;

#   Services: sequencer
from services.ZettelkastenSequencer     import ZettelkastenSequencer as sequencer;


from typing import List, Tuple, TypeVar, Any;
from datetime import datetime;


class ZettelkastenGenerator:
    """
    Main class for generating Zettelkasten Unique Identifiers (zUIDs).
    This class should be used for all Zettelkasten operations. It allows:

    -   Creating a Zettelkasten Unique Identifier (zUID) from an integer, string or datetime object.
    -   Decomposing a Zettelkasten Unique Identifier (zUID) into its components (year, month, day, hour, minute).
    -   Validating a Zettelkasten Unique Identifier (zUID) by checking if it is well-formed.
    -   Getting the previous and next zUIDs of a given zUID.


    @author         rdcn
    @version        1.1
    @since          1.1
    @date           2025-02-14
    """    
    __slots__ = ('current', 'history', 'identifiers');
    
    def __init__(self):
        """
        Constructor for the `ZettelkastenGenerator` class.
        """
        self.current        : zUID = None;
        self.history        : List[zUID] = list();
        self.identifiers    : List[zUID] = list();
        
    
    def now(self) -> zUID:
        """
        Tries to create a Zettelkasten Unique Identifier (zUID) from the current date and time.
        
        Returns
        -------
        zUID
            The created zUID.
        """
        return self.create(datetime.now());
    
    def create(self, id: int | str | datetime) -> zUID | None:
        """
        Creates a Zettelkasten Unique Identifier (zUID) from an integer, string or datetime object.
        
        Parameters
        ----------
        id : int | str | datetime
            The integer, string or datetime object to create the zUID from.
        
        Returns
        -------
        zUID | None
            The created zUID or None if the given argument is not a valid zUID.
        """
        try:
            zuid : zUID = builder.build(id);
            if zuid not in self.identifiers:
                self.identifiers.append(zuid);
                self.history.append(zuid);
                self.current = zuid;
                return zuid;
            return None;
        except Exception as e:
            print(e);
        
        
    def decompose(self, id: int | str | datetime | zUID) -> Tuple[int, int, int, int, int]:
        """
        Decomposes a Zettelkasten Unique Identifier (zUID) into its components (year, month, day, hour, minute).
        
        Parameters
        ----------
        id : int | str | datetime | zUID
            The integer, string or datetime object or zUID to decompose.
        
        Returns
        -------
        Tuple[int, int, int, int, int]
            The decomposed components (year, month, day, hour, minute).
        """
        return decomposer.decompose(id);
    
    
    def validate(self, id: int | str | datetime | zUID) -> bool:
        """
        Validates a Zettelkasten Unique Identifier (zUID) by checking if it is well-formed.
        
        Parameters
        ----------
        id : int | str | datetime | zUID
            The integer, string or datetime object or zUID to validate.
        
        Returns
        -------
        bool
            `True` if the zUID is well-formed, `False` otherwise.
        """
        return validator.validate(id);
    
    
    def get_previous(self, id: int | str | datetime | zUID) -> zUID | None:
        """
        Gets the previous zUID of a given zUID.
        
        Parameters
        ----------
        id : int | str | datetime | zUID
            The integer, string or datetime object or zUID to get the previous zUID of.
        
        Returns
        -------
        zUID | None
            The previous zUID or None if the given argument is not a valid zUID.
        """
        return sequencer.get_previous(id);
    
    
    def get_next(self, id: int | str | datetime | zUID) -> zUID | None:
        """
        Gets the next zUID of a given zUID.
        
        Parameters
        ----------
        id : int | str | datetime | zUID
            The integer, string or datetime object or zUID to get the next zUID of.
        
        Returns
        -------
        zUID | None
            The next zUID or None if the given argument is not a valid zUID.
        """
        return sequencer.get_next(id);
    
def try_build(param: int | str | datetime, expected: Tuple[int, int, int, int, int]) -> bool:
    try:
        zuid : zUID = builder.build(param);
        return decomposer.decompose(zuid) == expected;
    except Exception as e:
        print(e);
        return False;

def msg_wrapper_try_build(param: int | str | datetime, expected: Tuple[int, int, int, int, int]) -> str:
    if try_build(param, expected):
        return f"Zettelkasten Unique Identifier (zUID) {param} is well-formed.";
    else:
        return f"Zettelkasten Unique Identifier (zUID) {param} is not well-formed.";

if __name__ == "__main__":
    zgen : ZettelkastenGenerator = ZettelkastenGenerator();
    
    #   Create Zettelkasten Unique Identifiers (zUIDs)
    integer : int = 199507141431;                       #    1995-07-14 14:30
    string  : str  = "199507141432";                    #    1995-07-14 14:30
    dt      : datetime = datetime(1995, 7, 14, 14, 33); #    1995-07-14 14:30
    
    print(msg_wrapper_try_build(integer, (1995, 7, 14, 14, 31))); #    1995-07-14 14:30
    print(msg_wrapper_try_build(string,  (1995, 7, 14, 14, 32))); #    1995-07-14 14:30
    print(msg_wrapper_try_build(dt,     (1995, 7, 14, 14, 33))); #    1995-07-14 14:30
    
    
    #   Decompose Zettelkasten Unique Identifiers (zUIDs)
    print(f"{zgen.decompose(integer)} => {zgen.decompose(string)} => {zgen.decompose(dt)}");
    
    
    #   Validate Zettelkasten Unique Identifiers (zUIDs)
    print(f"{202502141151} => {zgen.validate(202502141151)}");
    
    
    #   Get previous and next Zettelkasten Unique Identifiers (zUIDs)
    counter : int = 0;
    identifier : int = 202502142330;
    
    while counter < 50:
        print(f"{counter:3d} :: {identifier}");
        identifier = zgen.get_next(identifier);
        counter += 1;
        
        
    #   Get the current (`now()`) Zettelkasten Unique Identifier (zUID)
    print(f"Current Zettelkasten Unique Identifier (zUID): {zgen.now()}");
    