import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup

#Boilerplate BeautifulSoup stuff and url
page = requests.get('https://en.wikipedia.org/wiki/List_of_American_artists_1900_and_after')
soup = BeautifulSoup(page.text, 'html.parser')

#Searching for target html div
target_class = soup.find(class_='mw-parser-output')
target_div = target_class.find_all('ul')

csv_list = []

for info in target_div[2:]:
	for individual_artist in info.find_all('li'):
		list_ = individual_artist.text.split(' ')
		csv_list.append(list_)

modified_list = []

for entry in csv_list:
	entry[:] = [' '.join(entry[:])]
	for chars in entry:
		modified_entry = chars.replace('(', ' ').replace('-', ' ').replace('\u2013', ' ').replace(')', '').replace(' born ', ' ').replace('c.', ' ').replace(' and ', ' ').replace(',', '').replace('  ', ' ')
		n = modified_entry.split(' ')
		modified_list.append(n)	

#Prints neatly to console
for index in modified_list:
	print(index)

#Writes data to output file
with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(modified_list)
