# Importing required libraries
import requests  
from bs4 import BeautifulSoup  

# Print the header for output
print("RENTAL TYPE | LOCATION | PRICE | AREA(sqft)")

for page in range(1, 14):
   
    url = f"https://www.nepalhomes.com/search?find_property_purpose=5d660baf7682d03f547a6c48&find_property_category=5d6643ed8f12c7035cd39316&page={page}&sort=1&find_selected_price_min=0&find_selected_price_max=5"
    
    # Send a GET request to the URL and fetch HTML content
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, "lxml")
    

    property_box = soup.find_all('div', class_='property__card')

 
    for property in property_box:

        prop_header = property.find('div', class_='property__card-header')

        price_tag = prop_header.find('span', class_="price-tag")
        
        sqft = "N/A"

        # Look for specifications like area in square feet
        spec_items = property.find_all('div', class_='spec-item')
        for item in spec_items:
            text = item.p.text.strip()
            # If the text includes 'Sq. Ft.', save it as area
            if 'Sq. Ft.' in text:
                sqft = text
                break  

        # Extract rental type, location, and price
        rentaltype = prop_header.h3.a.text.strip()
        location = prop_header.p.text.strip()
        price = price_tag.text.strip()

        # Print the extracted information
        print(f"{rentaltype} | {location} | {price} | {sqft}")
