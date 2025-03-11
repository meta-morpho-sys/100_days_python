import pandas
import requests


# TASK
# 1. Get the squirrel data from
# 2. Read the file
# 3. Use only the Primary Fur Colour column
# 4. Create a new data frame with squirrels count per Fur Colour
# 5. Save it to a csv file

url = "https://data.cityofnewyork.us/resource/vfnx-vebw.csv"
filename = 'squirrel_census_central_park_2018.csv'
query_params = {"$limit": '4000'}
response = requests.get(url,params=query_params)

print(f"Status Code: {response.status_code}")

with open(filename, 'wb') as f:
    f.write(response.content)
    print(f"Finished downloading >> {filename}")

squirrel_raw_data = pandas.read_csv(filename)

count_grey = len(squirrel_raw_data[squirrel_raw_data.primary_fur_color == 'Gray'])
count_black = len(squirrel_raw_data[squirrel_raw_data.primary_fur_color == 'Black'])
count_cinnamon = len(squirrel_raw_data[squirrel_raw_data.primary_fur_color == 'Cinnamon'])

colours_dict = {
    "Fur Color": ['Grey', 'Cinnamon','Black'],
    'Count': [count_grey,count_cinnamon, count_black],
}

count_per_fur_colour  = pandas.DataFrame(colours_dict)
count_per_fur_colour.to_csv('squirrel_count.csv')
