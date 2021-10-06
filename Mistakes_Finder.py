from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv

csv_file = open('Mistakes.csv', 'w', encoding = 'utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Mistaken Words'])

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

for n in range(990, 993):
    url = f"https://data.typeracer.com/pit/result?id=|tr:_cephas_|{n}"

    session = HTMLSession()
    r = session.get(url, headers = header)
    r.html.render(sleep = 2, timeout=50)
    mistaken_words = r.html.find("div.replayWord")

    for word in mistaken_words:
        mistakes = word.text.strip()
        csv_writer.writerow([mistakes])

csv_file.close()
        
