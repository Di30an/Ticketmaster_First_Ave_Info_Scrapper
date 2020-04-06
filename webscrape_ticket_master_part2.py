import requests
from urllib.error import HTTPError

import json
'''
This one was tricky. The json shows 20 elements per page and there are 30 pages. Needed to interate through these. Perhaps I went the wrong way around it, but it works.

'''

key =''

page = 0
elements = 0



query = {'apikey': key , 'locale': '*' , 'page' : page, 'city' : 'Minneapolis' , 'countryCode' : 'US'}
url = "https://app.ticketmaster.com/discovery/v2/events"
data = requests.get(url, params=query).json()
other_data = requests.get(url, params=query)
r = requests.get(url, params=query)

data_dict = {}

elements_range = (data['page']['size'])
page_range = (data['page']['totalPages']) # this gets the number of pages availble.


while(page <= page_range):

    if(elements <= elements_range):
        print(data['_embedded']['events'][elements]['name']) # this gets the number of pages availble. 
        elements +=1
    if (elements_range <= elements):
        elements = 0
        page += 1
        query = {'apikey': key , 'locale': '*' , 'page' : page, 'city' : 'Minneapolis' , 'countryCode' : 'US'}
        url = "https://app.ticketmaster.com/discovery/v2/events"
        data = requests.get(url, params=query).json()

    if (page >= page_range):
        break

