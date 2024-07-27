import csv
import os

# Define the paths to the continent-specific CSV files
continent_files = {
    'Africa': 'worldometerdata_Africa.csv',
    'Asia': 'worldometerdata_Asia.csv',
    'Europe': 'worldometerdata_Europe.csv',
    'North America': 'worldometerdata_North America.csv',
    'Oceania': 'worldometerdata_Oceania.csv',
    'South America': 'worldometerdata_South America.csv'
}

# Function to read continent-specific CSV files and return a list of countries
def get_countries_from_continent(file_path):
    countries = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        # Print the column names for debugging
        print(f"Column names in {file_path}: {reader.fieldnames}")
        for row in reader:
            countries.append(row['Country,Other'])  # Update the column name here if necessary
    return countries

# Read the OWID COVID-19 data from the local CSV file
owid_data_path = './owid-covid-data.csv'
with open(owid_data_path, mode='r', newline='', encoding='utf-8') as csvfile:
    owid_data = list(csv.reader(csvfile))

# Read the header from the OWID data
header = owid_data[0]

# Create a directory to store the sorted CSV files
output_dir = 'sorted_by_continent'
os.makedirs(output_dir, exist_ok=True)

# Process each continent
for continent, file_path in continent_files.items():
    # Get the list of countries for the current continent
    countries = get_countries_from_continent(file_path)
    
    # Filter the OWID data for the countries in the current continent
    continent_data = [header]
    for row in csv.DictReader(owid_data[1:], fieldnames=header):
        if row['location'] in countries:
            continent_data.append(list(row.values()))
    
    # Save the filtered data to a new CSV file
    output_file = os.path.join(output_dir, f'OWID_{continent}.csv')
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(continent_data)
    
    print(f'Saved data for {continent} to {output_file}')
