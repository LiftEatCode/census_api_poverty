import psycopg2

#connect to postgres database census
try:
	connection = psycopg2.connect(database="census", user = "josh", password = 'python', host= "127.0.0.1", port = "5432")
	
except pyscopg2.Error as err:
	print("An error was generated")

else:
	print("Connection to database was successful")

# Create cursor 
cursor = connection.cursor()

# Create Table:
cursor.execute('''create table poverty_level.poverty_detailed
      (id SERIAL primary key,
       Total_Housing float not null,
       Median_Family_Income float not null,
       Total_Family_Income float not null,
       Unemployed float not null,
       Employed float not null,
       Own_Cars float not null,
       No_Car_Owned float not null,
       Tot_House_Food_Stamps float not null,
       Tot_disability float not null,
       Total_Family_Poverty float not null,
       Total_Population float not null,
       Zipcode varchar(50));''')
       
connection.commit()
 
connection.close() #close connection to database.
	

