# Crime in Chicago (one year from the present)
import requests
import json 
import plotly.express as px
import pandas as pd 

url = "https://data.cityofchicago.org/resource/dfnk-7re6.json"
data_text = requests.get(url).text
json_data = json.loads(data_text)

# removing data dictionaries that doesn't have long and lat coordinates (removed 35 points out of 1000)
edited_data_set_list = []

for i in json_data: 
    if "location" in i: 
        edited_data_set_list.append(i)

# creating long and lat location list for crimes
location_list = []
for i in range(len(edited_data_set_list)): 
    temp_data_dict = edited_data_set_list[i]
    long = temp_data_dict["location"]["longitude"]
    lat = temp_data_dict["location"]["latitude"]
    location_row = [long, lat]
    location_list.append(location_row)

# plotting location_list (https://plotly.com/python/mapbox-layers/)

# turn the location_list into a dataframe
df = pd.DataFrame(location_list, columns=["lon", "lat"])

# convert data points in columns lon and lat of dataframe into floats for scatter_mapbox
# https://stackoverflow.com/questions/44522741/pandas-mean-typeerror-could-not-convert-to-numeric
df["lon"] = pd.to_numeric(df["lon"], downcast="float")
df["lat"] = pd.to_numeric(df["lat"], downcast="float")

fig = px.scatter_mapbox(df, lat="lat", lon="lon", color_discrete_sequence=["fuchsia"])
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
