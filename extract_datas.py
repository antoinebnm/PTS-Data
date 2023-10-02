import time, os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# Set up the WebDriver (make sure to specify the path to your WebDriver executable)
driver = webdriver.Chrome(executable_path=os.path.curdir + os.sep + "chromedriver.exe")

# Navigate to the website
url = 'https://www.data.gouv.fr/fr/datasets/interventions-realisees-par-les-services-d-incendie-et-de-secours/'  # Replace with the URL of the website
driver.get(url)

# You may need to interact with the page to load more content here
# For example, if there's a "Load More" button, click it in a loop
# until all desired data is loaded.

# Create an empty list to store the extracted data
extracted_data = []

# Scrape data from the page using BeautifulSoup
while True:
    # Get the page source after dynamic content has loaded
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract data from the page using BeautifulSoup
    # You'll need to inspect the page's HTML structure to locate the data you want
    # For example:
    data = soup.find_all('div', class_='your-data-class')

    # Add the extracted data to the list
    extracted_data.extend(data)

    # Check if there's a "Next" button or another way to navigate to the next page
    # If not, break out of the loop
    if not driver.find_element_by_xpath('//button[contains(text(), "Next")]'):
        break

    # Click the "Next" button to go to the next page
    next_button = driver.find_element_by_xpath('//button[contains(text(), "Next")]')
    next_button.click()

    # Wait for a few seconds (adjust as needed) to allow the next page to load
    time.sleep(5)

# Close the WebDriver when done
driver.quit()



CSV= []

html_page = requests.get('https://www.data.gouv.fr/fr/datasets/interventions-realisees-par-les-services-d-incendie-et-de-secours/').text

bs = BeautifulSoup(html_page, "lxml")
for link in bs.findAll('a'):
    href = str(link.get('href'))
    if href.endswith(".csv"):
        CSV.append(href)

print(CSV)