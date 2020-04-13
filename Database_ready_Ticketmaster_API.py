import requests
from urllib.error import HTTPError
from django.http import HttpResponse
from django.db import IntegrityError

import json
'''
This one was tricky. The json shows 20 elements per page and there are 30 pages. Needed to interate through these. Perhaps I went the wrong way around it, but it works.

'''


url = "https://app.ticketmaster.com/discovery/v2/events/"

def get_all_data(requests):
    try:
        # Try catch block, provides a response if working
        get_artists_list()
        get_venues_list()
        get_shows()
        return HttpResponse('working')
    except Exception as ex:
        print(ex) 
        return HttpResponse('did not work.')

key ='7CyQJ1JxlnqGBJe0uEkZw9h8SMvjoLQ9'

page = 0
elements = 0

def get_artists_list():
    query = {'apikey': key , 'locale': '*' , 'page' : page, 'city' : 'Minneapolis' , 'countryCode' : 'US', 'name':'music'}
    data = requests.get(url, params=query).json()
    #artists = Artist.objects.all().order_by('name')
    artist_names = []
    for artist in artists:
            artist_names.append(artist.name)
    try:
        data = requests.get(url).json()
        events = data['_embedded']['events']
        for event in events:
            artist_name = (event['name'])
            if artist_name not in artist_names:
                #new_artist = Artist(name = artist_name)
                #new_artist.save()
                print('artist '+ artist_name + ' added')
        ## calling api for events and finding artists
        ## saving name and creating new Artist Object if not already created
            else:
                print('duplicate artist')
    except Exception as e:
        print(e)
        
get_artists_list()


while(page <= page_range):

    if(elements <= elements_range):
        print(data['_embedded']['events'][elements]['name']) 
        elements +=1
    if (elements_range <= elements):
        elements = 0
        page += 1
        query = {'apikey': key , 'locale': '*' , 'page' : page, 'city' : 'Minneapolis' , 'countryCode' : 'US'}
        url = "https://app.ticketmaster.com/discovery/v2/events"
        data = requests.get(url, params=query).json()

    if (page >= page_range):
        break

for page in page_range: