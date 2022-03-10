import plotly.express as px
import pandas as pd 
import geojson 
from crimes_chicago import crime_df

# Calculating crime done in each ward
crime_per_ward_dict = {}
for ward in crime_df['ward']:
    if ward not in crime_per_ward_dict: 
        crime_per_ward_dict[ward] = 1
    else:
        crime_per_ward_dict[ward] += 1

# creating two columns for df: ward & frequency 
ward_frequency_dict = {}
ward_list = []
frequency_list = []
for key in crime_per_ward_dict: 
    ward_list.append(key)
    frequency_list.append(crime_per_ward_dict[key])
    ward_frequency_dict['ward'] = ward_list
    ward_frequency_dict['frequency'] = frequency_list
 
# making ward_frequency_dict into data frame with ward and frequency as columns 
crime_frequency_df = pd.DataFrame(ward_frequency_dict)

# https://medium.com/analytics-vidhya/create-geomaps-using-graph-objects-and-geojson-plotly-dcfb4067e3a6
# https://plotly.com/python/choropleth-maps/
# plotting the boundaries of the ward
fig = px.choropleth(crime_frequency_df, color="frequency", geojson="https://gist.githubusercontent.com/cgansen/6458644/raw/5a9ec31defab0073853831b7fc7de0f87eb66a2d/wards-from-city-unsimplified.geojson", featureidkey='properties.WARD', locations='ward')
fig.update_geos(fitbounds="locations", visible=False)
fig.show()
