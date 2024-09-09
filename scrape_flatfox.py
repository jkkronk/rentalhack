from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up the Selenium WebDriver (ensure you have the correct path to the ChromeDriver)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to your ChromeDriver
webdriver_service = Service()  
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Navigate to Flatfox Zurich apartment listings
url = 'https://flatfox.ch/en/search/?east=8.577443&north=47.416916&query=Zürich%2C%20Zürich%2C%20Switzerland&south=47.342957&take=96&west=8.488767'
driver.get(url)

# Wait for the page to load the listings
time.sleep(60)  # Increased wait time

# Find apartment cards
apartment_cards = driver.find_elements(By.CLASS_NAME, 'listing-thumb')
print(f"Number of apartment cards found: {len(apartment_cards)}")

prices = []
info = []
links = []

for card in apartment_cards:
    # Extract price
    try:
        price = card.find_element(By.XPATH, './/span[contains(@class, "price")]').text.strip() + ' CHF'
        prices.append(price)
    except:
        prices.append('N/A')

    # Extract size
    try:
        size = card.find_element(By.XPATH, './/h2').text.strip()
        info.append(size)
    except:
        info.append('N/A')

    # Get Link 
    try:
        link_element = card.find_element(By.XPATH, './/a[contains(@class, "listing-thumb-title")]')
        link = link_element.get_attribute('href')
        links.append(link)
    except:
        links.append('N/A')

# Print out the results
for i in range(len(prices)):
    print(f"Apartment {i + 1}:")
    print(f"Price: {prices[i]}")
    print(f"Info: {info[i]}")
    print(f"Link: {links[i]}")
    print("-" * 20)

# Close the browser
driver.quit()