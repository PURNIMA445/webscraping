import requests
from bs4 import BeautifulSoup


# properties = soup.find_all('div', class_='property__card-header')
# for prop in properties:
#     price_tag = prop.find('span', class_="price-tag")
#     rentaltype = prop.h3.a.text 
#     location = prop.p.text
#     price = price_tag.text 
#     print(f"{rentaltype} | {location} | {price}")

# Area=soup.find_all('div',class_='spec-item')
# for area in Area:
#     sqft=area.p.text
#     if 'Sq. Ft.' in sqft:
#         print(sqft)
print("RENTAL TYPE | LOCATION | PRICE | AREA(sqft)")
for page in range(1,14):
    url = f"https://www.nepalhomes.com/search?find_property_purpose=5d660baf7682d03f547a6c48&find_property_category=5d6643ed8f12c7035cd39316&page={page}&sort=1&find_selected_price_min=0&find_selected_price_max=5"
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, "lxml")
    
    property_box = soup.find_all('div', class_='property__card')

    for property in property_box:
        prop_header = property.find('div', class_='property__card-header')
        price_tag = prop_header.find('span', class_="price-tag")
        
        # Default value in case area is not found
        sqft = "N/A"

        # Find all spec-items (there may be more than one)
        spec_items = property.find_all('div', class_='spec-item')
        for item in spec_items:
            text = item.p.text.strip()
            if 'Sq. Ft.' in text:
                sqft = text
                break  # Stop after finding the first matching area

        rentaltype = prop_header.h3.a.text.strip()
        location = prop_header.p.text.strip()
        price = price_tag.text.strip()

        print(f"{rentaltype} | {location} | {price} | {sqft}")
