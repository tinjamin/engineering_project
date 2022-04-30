import pandas as pd
import plotly.express as px
from crimes_chicago import crime_df

def crimetype_frequency(ward):
    '''This function calculates the frequency of each crime type in a specific ward and returns a dataframe with columns 'type' and 'frequency', where 'type' is the crime type and 'frequency' is the number of instances that the crime type occurred.

    The ward parameter must be a string type.'''

    # Search within the larger crime_df for only the specified ward
    search_string = "ward==" + f"'{ward}'"
    df_ward = crime_df.query(search_string)
    ward_crimetype_frequency_dict = {}

    # count the number of times a crime occurred within the specified ward
    for crimetype in df_ward['crime_type']: 
        if crimetype in ward_crimetype_frequency_dict:
            ward_crimetype_frequency_dict[crimetype] += 1
        else:
            ward_crimetype_frequency_dict[crimetype] = 1

    # turning it into a type, frequency dataframe
    df_crimetype_frequency = pd.DataFrame()

    keys = ward_crimetype_frequency_dict.keys()
    vals = ward_crimetype_frequency_dict.values()

    df_crimetype_frequency['type'] = keys
    df_crimetype_frequency['frequency'] = vals

    return df_crimetype_frequency

def ward_frequency_crimetype_pie(ward, df):
    '''Creates a pie graph of the ward crime type frequency dataframe returned by crimetype_frequency function. The function returns a pie graph object that must be captured in a variable.

    The ward parameter must be a string that represents the specific ward of the dataframe passed to the function. 

    The df parameter must be a dataframe with two columns named "frequency" and "type". '''

    return px.pie(df, values='frequency', names='type', title=f"Crime Type Breakdown for Ward {ward}")

def pie_show(ward):
    df_ward = crimetype_frequency(ward)
    fig = ward_frequency_crimetype_pie(ward, df_ward) 
    return fig.show()

usr_input = input("Ward (enter 'q' to quit): ")
while True:
    usr_input = input("Ward (enter 'q' to quit): ")
    if usr_input == 'q':
        break
    pie_show(usr_input)
