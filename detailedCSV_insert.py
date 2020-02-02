#Write csv to Summary Table
import psycopg2 as pg
import csv

#Total_Housing , has_children_poverty, Total_family_Poverty, Tot_population, zipcode
file = 'census_detailed.csv'
sql_insert = """INSERT INTO poverty_level.poverty_detailed(Total_Housing,Median_Family_Income, Total_Family_Income, 
                Unemployed, Employed, Own_Cars, No_Car_Owned, Tot_House_Food_Stamps, Tot_disability,
                Total_Family_Poverty, Total_Population, zipcode)
                VALUES(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)"""
try:
    conn = pg.connect(user="josh",
        password="python",
        host="127.0.0.1",
        port="5432",
        database="census")
    cursor = conn.cursor()
    with open(file, 'r') as f:
        reader = csv.reader(f)
        #next(reader) # This skips the 1st row which is the header.
        for record in reader:
            cursor.execute(sql_insert, record)
            conn.commit()
except (Exception, pg.Error) as e:
    print(e)
finally:
    if (conn):
        cursor.close()
        conn.close()
        print("Connection closed.")
