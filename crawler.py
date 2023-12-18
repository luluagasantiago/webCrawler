import requests 
from bs4 import BeautifulSoup
import csv

# initialize the list of discovered urls 
# with the first page to visit
urls = ["https://scrapeme.live/shop/Bulbasaur/"]

# just used to limit the loop
ITERS = 10

products = {}

#until all pages have been visited
    
while len(urls) != 0 and ITERS > 0:
    ITERS -= 1

    # get the page to visit from the list
    current_url = urls.pop()
    
    # crawling logic
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    link_elements = soup.select("a[href]")
    for link_element in link_elements:
        url = link_element["href"]
        if "https://scrapeme.live/shop" in url:
            urls.append(url)
    # if current_url is product page
    product = {}
    if soup.select_one(".product_title"):
        name = soup.select_one(".product_title").contents[0]
        if name not in products:
            product["name"] = name 
            product["url"] = current_url
            product["image"] = soup.select_one(".wp-post-image")["src"]
            product["price"] =  "".join(list(soup.select_one(".price").descendants)[-2:])
            products[name] = product



with open('products.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)

    # populating the CSV
    for key,value in products.items():
        writer.writerow(value.values())

