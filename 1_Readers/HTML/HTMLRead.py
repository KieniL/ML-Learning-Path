#For Reading html you need the module html5lib (do pip install html5lib) and beautifulsoup4 (do pip install BeautifulSoup4)
import pandas as pd

#You can only read a table from the webpage, otherwise there will be an error
path = "https://www.w3schools.com/html/html_tables.asp"

data = pd.read_html(path)


print(data)