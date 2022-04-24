# Crime in Chicago (one year from the present)
import requests
import json 
import pandas as pd 

url = "https://data.cityofchicago.org/resource/dfnk-7re6.json"
data_text = requests.get(url).text 
json_data = json.loads(data_text)

location_list = []
residential_list = ["APARTMENT", "APPLIANCE STORE", "ATHLETIC CLUB", "AUTO", "AUTO / BOAT / RV DEALERSHIP", "BANK", "BAR OR TAVERN", "BARBERSHOP", "BOWLING ALLEY", "CAR WASH", "CHA APARTMENT", "CHA HALLWAY / STAIRWELL / ELEVATOR", "CHA PARKING LOT", "CHA PARKING LOT / GROUNDS", "CHURCH / SYNAGOGUE / PLACE OF WORSHIP", "CLEANING STORE", "CLUB", "COMMERCIAL / BUSINESS OFFICE", "CONVENIENCE STORE", "DRIVEWAY RESIDENTIAL", "DRUG STORE", "GARAGE", "HOUSE", "RESIDENCE", "RESIDENCE - YARD (FRONT / BACK)", "RESIDENCE - GARAGE", "RESIDENCE - PORCH / HALLWAY", "SCHOOL - PUBLIC BUILDING", "SCHOOL - PRIVATE BUILDING"]
ward_list = []
lat_list = []
lon_list = []

# appending all of the crime locations 
for line in json_data:
    if "_location_description" in line: 
        location_list.append(line["_location_description"])
    else:
        continue

# walking through daddy array 
for i in range(len(location_list)): 
    if location_list[i] in residential_list: 
        data_list = json_data[i]
        if "location" in data_list:
            print(data_list)
            ward_list.append(data_list['ward'])
            lat_list.append(data_list['location']['latitude'])

print(len(lat_list))
