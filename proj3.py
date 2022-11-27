# Projekt: UPA - VUT FIT
# Autory: Slavomír Svorada (xsvora02), Jakub Zaukolec (xzauko00), Jozef Čásar (xcasar03)

import requests
import re
from bs4 import BeautifulSoup

# function to extract html document from given url
def getDocument(url):
    # request for Html document from given URL
    response = requests.get(url)
    return response.text

# my URL
myUrl = "https://store.flightsim.com/product-category/msfs/msfs-scenery/page/2/"

# open file for writing
f = open("urls.txt", "w")

# for cycle to change pages on site
for i in range(3, 17):
    # create document
    document = getDocument(myUrl)

    # create soap object
    soup = BeautifulSoup(document, 'html.parser')

    # find correct data
    sceneriesData = soup.find("body").find('div', {'id': 'page-container'}).find('div', {'id': 'left-area'}).find('ul', {'class': 'products columns-3'})
    
    # find all sceneries from site, attribute starting with "https://"
    for newUrl in sceneriesData.find_all('a', attrs={'href': re.compile("^https://")}): 
        # save url to textfile
        f.write(newUrl.get('href') + '\n')
        
    # change URL to next page for new data
    myUrl = "https://store.flightsim.com/product-category/msfs/msfs-scenery/page/" + str(i) + '/'

# close file
f.close()
