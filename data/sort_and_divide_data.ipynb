import csv
import os
from datetime import datetime

#output directory
output_dir = './sorted_data'
os.makedirs(output_dir, exist_ok=True)

#filter, write data for every continent, month, year
def sort_generate(continent, month, year, rows, header):
    month_name = datetime(year, month, 1).strftime('%B')
    filename = f'{output_dir}/OWID_{continent}_{month_name}_{year}.csv'
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)
    print(f'{filename} created successfully.')

#read master csv file
with open('./OWID Dataset/owid-covid-data-master-file.csv', mode='r') as master_dataset:
    owid_data = csv.reader(master_dataset)
    #temporarily get, store header row
    header = next(owid_data)
    
    #get index of relevant columns("continent" for continent AND "date" for timeframe)
    continent_idx = header.index('continent')
    date_idx = header.index('date')
    
    #initialize dictionaries to store rows for each continent, year, and month
    data = {continent: {year: {month: [] for month in range(1, 13)} for year in range(2020, 2025)} for continent in ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']}
    
    #process each row in csv file
    for row in owid_data:
        continent = row[continent_idx]
        date_str = row[date_idx]
        year_month_day_string = datetime.strptime(date_str, '%Y-%m-%d')
        year = year_month_day_string.year
        month = year_month_day_string.month

        if ((continent in data) and (year in data[continent]) and (month in data[continent][year])):
            (data[continent][year][month]).append(row)

    #write filtered data to new csv files
    for continent, years in data.items():
        for year, months in years.items():
            for month, rows in months.items():
                if rows:
                    sort_generate(continent, month, year, rows, header)

