import indeedWebScrapper
import csv
with open('keyWord.csv', 'r') as csvfile:
    csvfilereader = csv.reader(csvfile, deliiniter=",", quotechar='|')
    for row in csvfilereader:
        print(row)
fileName = indeedWebScrapper.indeedScrape('Admin Assistant')
