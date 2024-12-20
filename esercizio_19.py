import requests
from bs4 import BeautifulSoup, ResultSet, Tag

url_new_york_times = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

response = requests.get(url_new_york_times)

html_response_stringa = response.text

parsed_html = BeautifulSoup(html_response_stringa, 'html.parser')

print(parsed_html.text)