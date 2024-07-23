import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL of the website
url = 'https://www.worldometers.info/coronavirus/'
page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')

    # Locate the table in the webpage
    table = soup.find('table', id='main_table_countries_today')

    if table:
        # Extract table headers
        headers = [header.text.strip() for header in table.find_all('th')]

        # Initialize dataframe with headers
        dataf = pd.DataFrame(columns=headers)

        # Extract table rows
        rows = table.find_all('tr')

        # Skip header row
        for row in rows[1:]:
            cells = row.find_all('td')
            # List comprehension to clean cell data
            cell_data = [cell.text.strip() for cell in cells]
            if len(cell_data) == len(headers):
                dataf.loc[len(dataf)] = cell_data

        # Debug: Print the first few rows of the dataframe to check data
        print("Dataframe head:\n", dataf.head())

        # Check if 'Continent' column exists
        if 'Continent' not in dataf.columns:
            print("Error: 'Continent' column not found in the data.")
        else:
            # List of categories
            categories = ['All', 'Europe', 'North America', 'Asia', 'South America', 'Africa', 'Oceania']

            # Save data for each category
            for category in categories:
                if category == 'All':
                    category_data = dataf
                else:
                    category_data = dataf[dataf['Continent'] == category]

                # Debug: Print the number of rows for each category
                print(f"Category: {category}, Number of rows: {len(category_data)}")

                # Check if the category_data is empty
                if category_data.empty:
                    print(f"Warning: No data found for category '{category}'.")

                # Save to CSV
                current_time = datetime.now()
                time_str = current_time.strftime("%H_%M_%S")
                file_name = f"worldometerdata_{category}_{time_str}.csv"
                category_data.to_csv(file_name, index=False)
                print(f"Saved to '{file_name}'")
    else:
        # Error message for table not found
        current_time = datetime.now()
        time_str = current_time.strftime("%H:%M:%S")
        print(f"--------\nTable not found on webpage.\nCurrent Time: {time_str}\n--------")
else:
    # Error message for failed webpage retrieval
    print(f"Failed to retrieve the webpage. Status code: {page.status_code}")
