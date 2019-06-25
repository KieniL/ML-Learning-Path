#This Script gets the URL from the first param (index = 1) and every other argument needs to be the search param in this format : <key>=<value>
#With the provided arguments we do a request and print out the hrefs
import sys
from urllib import request 
from bs4 import BeautifulSoup

arguments =  sys.argv

#print(arguments)

if arguments:
    queryString = ""
    for index, string in enumerate(arguments):
        if index == 0:
            continue
        if index == 1:
            url = string
        elif index == 2:
            queryString += "?" + string
        else:
            queryString += "&" + string
    requestURL = url + queryString
    url_requested = request.urlopen(requestURL)


    if 200 == url_requested.code:
        page_content=[] 
        html_content = str(url_requested.read())
        soup = BeautifulSoup(html_content, 'html.parser')

        for link in soup.find_all('a'):
            print(link.get('href'))