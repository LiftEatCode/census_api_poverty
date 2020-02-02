import requests
import pandas as pd
import csv
import time

API_KEY= "bffbee278915db059a4716c14cfe8ef40dd28e20"

#call the needed info from the census api
data_obj = requests.get("https://api.census.gov/data/2018/acs/acs5/profile?get=DP04_0001E,DP03_0120PE,DP05_0001E,DP03_0119PE&for=zip%20code%20tabulation%20area:*&key=bffbee278915db059a4716c14cfe8ef40dd28e20")


#check to make sure you are connected to API
# print(data.status_code)

# print(data_obj.text)

#create data variable to hold data from API call
data = data_obj.text

#get rid of all the junk formating from the API call
data_results = data.replace(']','')
data_results2 = data_results.replace('[', '')
data_results3 = data_results2.replace('"', "'")

# print(data_results3)


# write API call data to CSV
with open('census.csv', mode='w') as f:
    census_writer = csv.writer(f, delimiter=',')

    census_writer.writerow([data_results3])



#create data frame
# datax = pd.read_csv("census.csv")
# print(datax)



