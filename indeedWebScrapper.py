import requests
import bs4
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import pandas as pd
import time

page = requests.get('https://www.indeed.com/jobs?q=Admin+Assistant&l=Marietta%2C+GA', verify=False)
soup = BeautifulSoup(page.text, 'html.parser')
pageBody = soup.find('body')
for i in pageBody.contents:
    if(i.attrs.get('id') == 'resultsBody'):
        print("Found job table")
