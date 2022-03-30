import csv 
import plotly.express as px
import pandas as pd 
import geojson 

with open("../../data_set/Per_Capita_Income.csv", "r") as csvfile: 
    csv_reader = csv.reader(csvfile)
    community_number = []
    community_name = []
    housing_crowded = []
    below_poverty = []
    unemployment = []
    no_HS_diploma = []
    per_capita_income = []
    hardship_index = []
    for line in csv_reader:
        community_number.append(line[0])
        community_name.append(line[1])
        housing_crowded.append(line[2])
        below_poverty.append(line[3])
        unemployment.append(line[4])
        no_HS_diploma.append(line[5])
        per_capita_income.append(line[7])
        hardship_index.append(line[8])

# convert into float
for i in range(1,len(no_HS_diploma)-1):
    no_HS_diploma[i] = float(no_HS_diploma[i])

# creating the dataframe 
pci_df = pd.DataFrame()
pci_df['Community Area Number'] = community_number[1:-1]
pci_df['Community Area Name'] = community_name[1:-1]
pci_df['Percent of Housing Crowded'] = housing_crowded[1:-1]
pci_df['Percent of Households Below Poverty'] = below_poverty[1:-1]
pci_df['Percent Aged 16+ Unemployed'] = unemployment[1:-1]
pci_df['Percent Aged 25+ Without High School Diploma'] = no_HS_diploma[1:-1]
pci_df['Per Capita Income'] = per_capita_income[1:-1]
pci_df['Hardship Index'] = hardship_index[1:-1]

fig = px.choropleth_mapbox(pci_df, geojson='https://raw.githubusercontent.com/RandomFractals/ChicagoCrimes/master/data/chicago-community-areas.geojson', featureidkey='properties.area_numbe', locations='Community Area Number', opacity=0.5, center={"lat": 41.8390, "lon": -87.6298}, zoom=10, color='Percent Aged 25+ Without High School Diploma')
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
