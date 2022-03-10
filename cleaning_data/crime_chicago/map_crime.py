import plotly.express as px
import pandas as pd 
from crimes_chicago import crime_df

# convert data points in columns lon and lat of dataframe into floats for scatter_mapbox
# https://stackoverflow.com/questions/44522741/pandas-mean-typeerror-could-not-convert-to-numeric
crime_df["lon"] = pd.to_numeric(crime_df["lon"], downcast="float")
crime_df["lat"] = pd.to_numeric(crime_df["lat"], downcast="float")

fig = px.scatter_mapbox(crime_df, lat="lat", lon="lon", color_discrete_sequence=["fuchsia"])
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
