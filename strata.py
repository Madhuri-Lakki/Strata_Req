'''
Develop a CLI application with below features:
1. Should Accept a Search Parameter (ID) and display entities returned by search API
GET
https://services.odata.org/TripPinRESTierService/People('russellwhyte')

2. Accept Entity Parameters from User and Call Create Entity API
POST 
https://services.odata.org/TripPinRESTierService/People


3. Get Filter Parameters from User and use the filter endpoint to fetch the results
GET
https://services.odata.org/TripPinRESTierService/People?$filter=FirstName eq 'Scott'
''';

import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

import requests
import typer
import json

app = typer.Typer()

session = 'mj3uu3aix04nddo5vamez2lp'

@app.command()
def get_userid(username):
    x = requests.request('GET', f"https://services.odata.org/TripPinRESTierService/(S({session}))/People('{username}')").json()
    print(json.dumps(x, indent=2))
    return x

@app.command()
def post_user_data(filepath):
    data = json.load(open(filepath, 'r'))
    headers = {'Content-Type': 'application/json'}
    x = requests.request("POST",
        f"https://services.odata.org/TripPinRESTierService/(S({session}))/People", 
        data=json.dumps(data),
        headers=headers
    ).json()
    print(json.dumps(x, indent=2))
    return x

@app.command()
def search_by_first_name(name):
    x =  requests.request('GET',f"https://services.odata.org/TripPinRESTierService/(S({session}))/People?$filter=FirstName eq '{name}'").json()
    print(json.dumps(x, indent=2))
    return x

if __name__ == '__main__':
    app()