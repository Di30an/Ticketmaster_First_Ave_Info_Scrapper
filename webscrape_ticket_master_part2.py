import requests
from urllib.error import HTTPError
from django.http import HttpResponse
from django.db import IntegrityError

import json
'''
This one was tricky. The json shows 20 elements per page and there are 30 pages. Needed to interate through these. Perhaps I went the wrong way around it, but it works.

'''



key ='7CyQJ1JxlnqGBJe0uEkZw9h8SMvjoLQ9'

page = 0
elements = 0



query = {'apikey': key , 'locale': '*' ,  'city' : 'Minneapolis' , 'countryCode' : 'US','page' : page, 'name' : 'music'}
url = "https://app.ticketmaster.com/discovery/v2/events"
data = requests.get(url, params=query).json()
other_data = requests.get(url, params=query)
r = requests.get(url, params=query)

data_dict = {}

elements_range = (data['page']['size'])
page_range = (data['page']['totalPages']) # this gets the number of pages availble.

for page in range(0, page_range):
    query = {'apikey': key , 'locale': '*' , 'page' : page, 'city' : 'Minneapolis' , 'countryCode' : 'US'}
    url = "https://app.ticketmaster.com/discovery/v2/events"
    data = requests.get(url, params=query).json()
    elements_range = (data['page']['size'])
    print('Element Range' ,elements_range )
    for elements in range(elements_range):
        print(elements_range)
        print(data['_embedded']['events'][elements]['name']) 



