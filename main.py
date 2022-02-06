import requests
from bs4 import BeautifulSoup
import csv
   
URL = "http://www.values.com/inspirational-quotes"
resp = requests.get(URL)
   
soup = BeautifulSoup(resp.content, 'html5lib')
   
quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'all_quotes'}) 
   
for row in table.findAll('div',
                         attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
   
filename = 'quotes.csv'
with open(filename, 'w') as f:
    w = csv.DictWriter(f,['lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)