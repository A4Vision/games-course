from bs4 import BeautifulSoup
from urllib.request import urlopen

my_url = "https://www.timeanddate.com/worldclock/israel/jerusalem"
web_page = urlopen(my_url)

HTML_page = BeautifulSoup(web_page.read(), "html.parser")
print(HTML_page.body.find("span", {"id": "ct"}).text)
