import requests
from bs4 import BeautifulSoup, ResultSet, Tag

print("Benvenuto nel lettore dei titoli del New York Times.")
nome_file = input("Come vuoi chiamare il file .txt su cui verrano salvati i titoli? ")
url_new_york_times = "https://www.nytimes.com"

response = requests.get(url_new_york_times)

html_response_stringa = response.text

parsed_html = BeautifulSoup(html_response_stringa, 'html.parser')

sezioni: ResultSet[Tag] = parsed_html.find_all('section', {'class': 'story-wrapper'})

#The following statement writes to a file and ensures that it is closed automatically after writing
with open(nome_file, 'w') as file_txt:
    for sezione in set(sezioni):
        titolo = sezione.find('p', {'class': 'indicate-hover'}, True)
        if titolo:
            file_txt.write(titolo.text + "\n")