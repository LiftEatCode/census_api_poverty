import psycopg2

#connect to census / postgres database
try:
	connection = psycopg2.connect(database="census", user = "josh", password = 'python', host= "127.0.0.1", port = "5432")
	
except pyscopg2.Error as err:
	print("An error was generated")

else:
	print("Connection to database was successful")

# Create cursor 
cursor = connection.cursor()

# Create Table -
#columns
#Total_Housing , has_children_poverty, Total_family_Poverty, Tot_population, zipcode

cursor.execute('''create table poverty_level.summary
      (id SERIAL primary key,
       Total_Housing float not null,
       With_Children_Poverty float not null,
       Total_Family_Poverty float not null,
       Total_Population float not null,
       Zipcode varchar(50));''')
       
connection.commit()
 
connection.close() #close connection to database.
	
