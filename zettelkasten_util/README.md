[release:: 2025-02-14] [version:: 1.1] [status:: alpha]

# `zettelkasten_util`
General utilities for dealing with zettelkasten unique identifiers.


## Usage
Import the `ZettelkastenGenerator` from the `zettelkasten_util` package. This class is an interface between the user and the engine.

## Data
In `data.ZettelkastenUniqueIdentifier` is defined the `zUID` class, representation of the identifier.

## Engine
-   `ZettelkastenDecomposer` implements static methods for decomposing zUIDs (as int, str, datetime or zUID) objects into their structural parts (year, month, day, hour, minute);
-   `ZettelkastenValidator` implements static methods for validating candidates to zUIDs.
-   `ZettelkastenBuilder`: given an int, a str or a datetime, returns a `zUID` iff the argument is valid.

##  Services
The `ZettelkastenSequencer` produces the previous and the next `zUID`s for a given identifier.