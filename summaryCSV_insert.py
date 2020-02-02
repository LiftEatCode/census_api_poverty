#Write csv to Summary Table
import psycopg2 as pg
import csv

#Total_Housing , has_children_poverty, Total_family_Poverty, Tot_population, zipcode
file = 'census.csv'
sql_insert = """INSERT INTO poverty_level.summary(Total_Housing, With_Children_Poverty, Total_Family_Poverty,
                Total_Population, zipcode)
                VALUES(%s, %s, %s, %s, %s)"""
try:
    conn = pg.connect(user="josh",
        password="python",
        host="127.0.0.1",
        port="5432",
        database="census")
    cursor = conn.cursor()
    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader) # This skips the 1st row which is the header.
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
