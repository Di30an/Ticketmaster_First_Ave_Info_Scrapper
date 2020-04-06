import re

from urllib.request import urlopen
from bs4 import BeautifulSoup

link_list =[]

def getHTMLContent(link): # passing url information to the function
    html = urlopen(link) # opening url using the urlopen method
    soup = BeautifulSoup(html, 'html.parser') # with the html we are able use Beautiful Soup
    return soup # output that we can extract data from

def getArtistsRange():
    months =['01']
    years = ['2018']
    # months =['01','02','03','04','05','06','07','08','09','10','11','12'] # Was the easiest way to iterate. Had issues trying to append a 0 if the number has a lenght of less than 2
    # years = ['2018','2019','2020'] # TODO make sure that it does not crash when I try any month after the current for the current year.
    for year in years:
        for month in months:
            htmlLink = f'https://first-avenue.com/calendar/all/{year}-{month}'
            content = getHTMLContent(htmlLink)
            getDistinctLink(content) # The bands name appears several times throught the HTML document. This function makes certain that I only have it once per occurance. 



def getDistinctLink(content):

    for link in content.find_all('a', attrs={'href': re.compile("/event")}):
        clean_link = (link.get('href'))
        if clean_link not in link_list:
            print(clean_link)
            link_list.append(clean_link)

def getArtistInfo():
    getArtistsRange()
    for link in link_list:
        artists = getHTMLContent(f'https://first-avenue.com{link}')
        if(artists.find('span', {'class': 'price'})): # There are private events that are listed on the website. If price is not present it should just skip
            artist = artists.find('div',{'class': 'performers'})
            date = artists.find('span', {'class': 'datepart'})
            price = artists.find('span', {'class': 'price'})
            # Found this class by inspecting the webpage and not using the pret
            # Ctrl + F for the end of a table using /table. This finds the ends of a table element. Found it useful
            # gather all the data and return a 
            print(artist.get_text())
            print(date.get_text())
            print(price.get_text())


getArtistInfo()