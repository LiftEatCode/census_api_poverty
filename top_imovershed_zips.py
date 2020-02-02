# File for showing query data
import psycopg2
import pandas as pd

#connect to postgres database census
try:
	connection = psycopg2.connect(database="census", user = "josh", password = 'python', host= "127.0.0.1", port = "5432")
	
except pyscopg2.Error as err:
	print("An error was generated")

else:
	print("Connection to database was successful")

# Create cursor 
cursor = connection.cursor()

# Query the top 10 most impovershed zipcodes
cursor.execute("select zipcode, total_population, median_family_income, unemployed,tot_house_food_stamps, total_family_poverty from poverty_level.poverty_detailed order by total_family_poverty DESC limit 10;")

# fetch records from query:
records = cursor.fetchall()

# extract column names
col_names = []
for elt in cursor.description:
	col_names.append(elt[0])

#create a dataframe, passing in list of col_names
df = pd.DataFrame(records, columns=col_names)

#print dataframe to screen:
print(df)

#commit changes and close connection:
connection.commit()
connection.close()
