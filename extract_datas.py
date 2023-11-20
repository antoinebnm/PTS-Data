import time, os
import requests
from bs4 import BeautifulSoup

# Navigate to the website
url = 'https://www.data.gouv.fr/fr/datasets/interventions-realisees-par-les-services-d-incendie-et-de-secours/'  # Replace with the URL of the website

# Create an empty list to store the extracted data
extracted_data = []

soup = BeautifulSoup('html.parser')

for link in soup.findAll('a'):
    data = str(link.get('href'))
    if data.endswith(".csv"):
        # Add the extracted data to the list
        extracted_data.append(data)

print(extracted_data)