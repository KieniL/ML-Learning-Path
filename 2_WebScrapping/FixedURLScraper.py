#This Script searches for Repository in github based on a defined searchparam, we use the request method form the urllib library
#We receive the html response and parse it with the beautifulsoup library
#We print out all links in this side
from urllib import request 
from bs4 import BeautifulSoup
searchParam = "Python"
url_requested = request.urlopen('https://github.com/search?q='+ searchParam)

if 200 == url_requested.code:
    page_content=[] 
    html_content = str(url_requested.read())
    soup = BeautifulSoup(html_content, 'html.parser')

    for link in soup.find_all('a'):
        print(link.get('href'))