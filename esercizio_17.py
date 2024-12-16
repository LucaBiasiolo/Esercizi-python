"""Note: this is a 4-chili exercise, not because it introduces a concept (although it introduces a new library), 
but because this exercise is more like a project. Feel free to skip this and come back when you’re more ready!
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage."""

import requests
from bs4 import BeautifulSoup, ResultSet, Tag

url_new_york_times = "https://www.nytimes.com"

response = requests.get(url_new_york_times)

html_response_stringa = response.text

parsed_html = BeautifulSoup(html_response_stringa, 'html.parser')

sezioni: ResultSet[Tag] = parsed_html.find_all('section', {'class': 'story-wrapper'})

for sezione in set(sezioni):
    titolo = sezione.find('p', {'class': 'indicate-hover'}, True)
    if titolo:
        print(titolo.text)