import requests
from bs4 import BeautifulSoup

# Send a GET request to the website to fetch the HTML content
url = 'https://www.example.com/products'  # Replace with the URL of the website
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup and extract the desired data
soup = BeautifulSoup(html_content, 'html.parser')

# Find all product items on the page
product_items = soup.find_all('div', class_='product-item')

# Extract the title and price for each product item
for product_item in product_items:
    title = product_item.find('h3', class_='product-title').text.strip()
    price = product_item.find('span', class_='product-price').text.strip()
    
    # Print the extracted data
    print(f"Title: {title}")
    print(f"Price: {price}")
    print()

# Store the scraped data in a suitable format (e.g., CSV, database, JSON)
# Here, we'll store the data in a CSV file
import csv

filename = 'products.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])  # Write headers
    for product_item in product_items:
        title = product_item.find('h3', class_='product-title').text.strip()
        price = product_item.find('span', class_='product-price').text.strip()
        writer.writerow([title, price])  # Write data rows

print(f"Data has been scraped and stored in {filename}.")
