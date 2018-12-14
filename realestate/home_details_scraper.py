from bs4 import BeautifulSoup
from urllib.request import urlopen

# page = open("D:\Projects\web-scraper\listings.html").read()
url = "https://www.point2homes.com/CA/Home-For-Sale/MB/Winnipeg/Downtown-Winnipeg/Minto/809-Ashburn-Street/67105439.html"
page = urlopen(url)
soup = BeautifulSoup(page, features="lxml")

# homes = soup.find_all("div", {"class": "smallListingCardAddress"})
# print (homes)
# for h in homes:
#     print (h.text.strip())

price = soup.find("span", {"itemprop": "price"})
print(price.text.strip())

beds = soup.find("li", {"data-label": "Beds"})
print(beds.text.strip())

baths = soup.find("li", {"data-label": "Baths"})
print(baths.text.strip())

sqft = soup.find("li", {"data-label": "Sqft"})
print(sqft.text.strip())

details = soup.find_all("dt")
dd = soup.find_all("dd")

detail_headings = []
for d in details:
    detail_headings.append(d.text)

detail_values = []
for d in dd:
    detail_values.append(d.text.strip())

all_details = (dict(zip(detail_headings, detail_values)))