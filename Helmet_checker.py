from bs4 import BeautifulSoup
import requests
import csv
import sys

csv_file = open('helmet.csv', 'w', encoding = 'utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Stars', 'Review Count', 'Price', 'Old_Price', 'Image_Link', 'Amazon_Link'])

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

for n in range(1,15):
    url = f"https://www.amazon.in/s?k=helmets+for+men&i=automotive&rh=n%3A4772060031%2Cp_89%3ASteelbird%7CStudds%7CVega%2Cp_36%3A150000-200000&dc&page={n}&qid=1629448200&rnid=5814682031&ref=sr_pg_{n}"

    page = requests.get(url, headers = header)
    soup = BeautifulSoup(page.content, 'lxml')

    for content in soup.select('div.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.AdHolder.sg-col.sg-col-4-of-20'):
        title = content.select_one('span.a-size-base-plus.a-color-base.a-text-normal').get_text(strip=True)
        stars = content.select_one('span.a-icon-alt').get_text(strip=True)
        rev = content.select_one('span.a-size-base').get_text(strip=True)
        price = content.select_one('span.a-price-whole').get_text(strip=True)
        old_price = content.select_one('span.a-offscreen').get_text(strip=True)[1:]
        image = content.find('img', class_='s-image')
        link = content.select_one('a.a-link-normal.a-text-normal')
        links = "https://www.amazon.in" + link['href']
    
        csv_writer.writerow([title,stars, rev, price, old_price, image['src'], links])
        
csv_file.close()
        
        
        
        
    
