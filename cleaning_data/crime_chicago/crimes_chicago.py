# Crime in Chicago (one year from the present)
import requests
import json 
import pandas as pd 

url = "https://data.cityofchicago.org/resource/dfnk-7re6.json"
data_text = requests.get(url).text 
json_data = json.loads(data_text)

# removing data dictionaries that doesn't have long and lat coordinates (removed 35 points out of 1000)
edited_data_set_list = []

for i in json_data: 
    if "location" in i and "ward" in i: 
        edited_data_set_list.append(i)

# turning data set into dataframe 
columnized_data_set_list = []
for i in range(len(edited_data_set_list)): 
    temp_data_dict = edited_data_set_list[i]
    lon = temp_data_dict["location"]["longitude"]
    lat = temp_data_dict["location"]["latitude"]
    ward = temp_data_dict["ward"]
    crime_type = temp_data_dict["_primary_decsription"]
    arrest = temp_data_dict["arrest"]
    columnized_data_set_list.append([lon, lat, ward, crime_type, arrest])

crime_df = pd.DataFrame(columnized_data_set_list, columns=["lon", "lat", "ward", "crime_type", "arrest"])
