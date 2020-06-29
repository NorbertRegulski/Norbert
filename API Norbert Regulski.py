import requests
import json
import pprint
import webbrowser
from datetime import datetime,timedelta
"""
API - Application Programming Interface
Program ma na celu pobranie z strony https://stackexchange.com,
a dokładniej https://stackoverflow.com/ pytań zadanych na forum w języku Python.
Ustalam swoje wymagania wobec pytań, gdyż jest ich dużo :
-minimalnie 15 punktów
-posegregowania malejąco
-z ostatniego miesiąca
-kategorii python
https://api.stackexchange.com/docs/questions tutaj jest wyjaśnienie
jak precyzować parametry

"""
timeBefore = timedelta(days=30)
searchDate = datetime.today() - timeBefore

parametry = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : int(searchDate.timestamp()),
    "tagged" : "python",
    "min" : 15
}


r = requests.get("https://api.stackexchange.com/2.2/questions/", parametry)


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
    
