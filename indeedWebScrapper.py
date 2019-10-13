import requests
import bs4
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import pandas as pd
import datetime
import time

def indeedScrape(keyWord):
    searchWord =keyWord.replace(" ","+")
    page = requests.get('https://www.indeed.com/jobs?q='+searchWord+'&l=Marietta%2C+GA', verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    pageBody = soup.find('td', {'id': 'resultsCol'})
    jobList = pageBody.find_all('div', {'class': 'jobsearch-SerpJobCard'})
    f = open(keyWord+".txt", "w+")
    f.write(str(datetime.datetime.now()))
    f.write('\n')
    for i in jobList:
        title = i.find('div', {'class': 'title'})
        url = 'https://indeed.com/'+title.contents[1].attrs['href']  
        sjcl = i.find('div', {'class': 'sjcl'})
        employer = i.find('div', {'class': 'serp-ResponsiveEmployer'})
        salary = i.find('div', {'class': 'salarySnippet'})
        summary = i.find('div', {'class': 'summary'})
        print('Title: '+title.text.strip(),file=f)
        if(sjcl != None):
            companyName = sjcl.find('a', {'data-tn-element': 'companyName'})
            if(companyName != None):
                companyName = companyName.text.strip()
                print('Company Name: '+companyName,file=f)
            reviewStars = sjcl.find('a', {'data-tn-element': 'reviewStars'})
            if(reviewStars != None):
                ratings = reviewStars.find('span', {'class': 'ratings'})
                print('Ratings: '+ratings.attrs['aria-label'],file=f)
                print('Number of Reviews: '+reviewStars.text.strip(),file=f)
        if(employer != None):
            print('Employer: '+employer.text.strip(),file=f)
        if(salary != None):
            print('Salary: '+salary.text.strip(),file=f)
        print('Summary: '+summary.text.strip(),file=f)
        print('URL: '+url,file=f)
        print('-----------------------',f)
    return(keyWord+".txt")

