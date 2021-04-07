# Strata_Req
## CLI(Command Line Interafce) application requirement
 
 ## Step 0:
 * Run `pip install requests typer` to install dependencies. 
 
 ## Step 1:
 * Visit the url  https://services.odata.org/TripPinRESTierService and get the sessionID that looks like `0cgbdaptvxijd4jnz1tu3yt1` and replace it in the file `strata.py`.
 
 ## Step 2:
 * Run `python strata.py --help` to see the relevant functions.
 * Run `python strata.py post-user-data data.txt` to post data that is contained in `data.txt`.
 * Run `python strata.py get-userid madhuri` while doing this please replace username `madhuri` with the username you mentioned in the POST data of `data.txt` file.
 * Run `python strata.py search-by-first-name Strata` to get all the record details which have the firstname `Strata`.

 
