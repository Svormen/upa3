import requests
import re
from bs4 import BeautifulSoup
import fileinput
import sys


# function for controlling arguments (limited arguments says i will extract only 20 products)
def argCheck():
    arguments = sys.argv[1:]
    if ("--limited") in arguments:
        return True
    else:
        return False


# function to extract html document from given url
def getDocument(url):
    # request for Html document from given URL
    response = requests.get(url)
    return response.text


# open file for writing
f = open("data.tsv", "w")

limited = argCheck()
counter = 0
for line in fileinput.input(encoding="utf-8"):
    myUrl = line.replace('\n', '')
    try:
        # create document
        document = getDocument(myUrl)
        # create soap object
        soup = BeautifulSoup(document, 'html.parser')
        # selceting name of product
        title = soup.find(class_='product_title entry-title').getText()
        # selecting price of product
        price = soup.find(class_='price').getText()
        # constructing final string
        final_string = myUrl + "\t" + title + "\t" + price
        # save url to textfile
        f.write(final_string + '\n')
        counter += 1
        if((limited) and (counter == 20)):
            break
    except:
        pass

# close file
f.close()
