# Crime in Chicago (one year from the present)
import requests
import json 
import pandas as pd 

url = "https://data.cityofchicago.org/api/views/dfnk-7re6/rows.json"
data_text = requests.get(url).text 
json_data = json.loads(data_text)

# turning data set into dataframe 
columnized_data_set_list = []
for entry in json_data['data']: 
    if entry[22] != None and entry[23] != None and entry[18] != None and entry[12] != None:
        ward = entry[18]
        crime_type = entry[12]
        lon = float(entry[23])
        lat = float(entry[22])
        columnized_data_set_list.append([lon, lat, ward, crime_type])

crime_df = pd.DataFrame(columnized_data_set_list, columns=["lon", "lat", "ward", "crime_type"])
