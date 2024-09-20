import requests
from bs4 import BeautifulSoup
import re
import sqlite3


#adding amazon product codes
database_name='CatOfficeProducts.db'
category_name="officeelectronics"
product_codes = [
"B08PH5Q51P",
"B00IOFD08C",
"B0BLGPVTFR",
"B003822IRA",
"B07DFYZ8FF",
"B07GKHQ9M6",
"B08XW7LT9P",
"B08DXDKF3L",
"B096MYB1H1",
"B08FBHTD9B"      
]


def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


#extracting required information from pages
def get_reviews(soup, product_name, category):
    reviews = soup.find_all('div', {'data-hook':'review'})
    for item in reviews:
        review = {
            'product': soup.title.text.replace('Amazon.com: Customer reviews:', '').strip(),
            'title': item.find('a', {'data-hook':'review-title'}).text.replace('out of 5 stars', '-').strip(),
            'rating': float(item.find('i', {'data-hook':'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'description': item.find('span', {'data-hook':'review-body'}).text.strip(),
            'category': category
        }
        listreview.append(review)

#creating the database
def save_to_sqlite(data, db_name=database_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            product TEXT,
            category TEXT,
            title TEXT,
            rating REAL,
            description TEXT
        )
    ''')

    c.executemany('INSERT INTO reviews VALUES (?, ?, ?, ?, ?)', data)
    
    conn.commit()
    conn.close()

listreview = []

#pasing product codes and loading amazon website
for product_code in product_codes:
    print(f'product: {product_code}')
    for x in range(1, 20):
        soup = get_soup(f'https://www.amazon.com/AmazonBasics-Multipurpose-Copy-Printer-Paper/product-reviews/{product_code}/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
        print(f'page: {x}')
        get_reviews(soup, soup.title.text.replace('Amazon.com: Customer Reviews:', '').strip(), category_name) 
        print(len(listreview))
        if not soup.find('li', {'class': 'a-disabled a-last'}):
            pass
        else:
            break

#saving database
save_to_sqlite([(review['product'], review['category'], review['title'], review['rating'], review['description']) for review in listreview])
print('Finished and data has been saved to SQLite database.')
