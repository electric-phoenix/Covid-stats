import json

from urllib.request import urlopen

with urlopen("https://api.covid19api.com/summary") as resp:
    source = resp.read()

stats = json.loads(source)
Country = dict()
for Nations in stats['Countries']:
    name = Nations['Country']
    new_cases = Nations['NewConfirmed']
    total_confirmed = Nations['TotalConfirmed']
    Country[name]=new_cases
print(25*"=","Daily Covid-19 cases by country",25*"=")
while True:
    cname=input('Enter country: ')
    if cname=='exit' or cname == 'Exit':
        break 
    try:
        print("Today's cases for", cname,":", Country[cname])
    except KeyError:
        print("Invalid input\n Check your spelling, make sure the first letter is capitalised")    