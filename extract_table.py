import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = 'https://www.worldometers.info/coronavirus/'
page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')

    # Locate table in webpage
    table = soup.find('table', id='main_table_countries_today')

    if table:
        # Extract table headers(continent names)
        headers = [header.text.strip() for header in table.find_all('th')]

        # Initialize dataframe with headers
        dataf = pd.DataFrame(columns=headers)

        # Extract table rows
        rows = table.find_all('tr')

        # Skip header row
        for row in rows[1:]:
            cells = row.find_all('td')
            # List comprehension to clean cell data
            cell_data = [cell.text.strip().replace(',', '').replace('+', '').replace('N/A', '0') for cell in cells]
            if len(cell_data) == len(headers):
                dataf.loc[len(dataf)] = cell_data

        # Save to CSV
        current_time = datetime.now()
        time_str = current_time.strftime("%H_%M_%S")
        file_name = f"worldometerdata_{time_str}.csv"
        dataf.to_csv(file_name, index=False)
        print(f"Saved to '{file_name}'")
    else:
        # Error message for table not found
        current_time = datetime.now()
        time_str = current_time.strftime("%H:%M:%S")
        print(f"--------\nTable not found on webpage.\nCurrent Time: {time_str}\n--------")
else:
    # Error message for failed webpage msg
    print(f"Failed to retrieve the webpage. Status code: {page.status_code}")

