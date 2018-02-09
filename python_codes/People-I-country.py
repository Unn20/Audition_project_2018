#this code searchs, how many people comes from different countries

#learner_id  country   in_course   unit   avg_score    completion   inv_rate
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pie_chart



conn = sqlite3.connect('PearsonData.db')
cur = conn.cursor() 
country = []
people = []
others = 0

#Give me distinct country
cur.execute("""SELECT 
               DISTINCT
               country FROM data2018
               ORDER BY country""")
distinct_country = cur.fetchall()
if distinct_country[0] == ('',): distinct_country = distinct_country[1:]


#Search for number of people from cuntry X
#If number < 200 add this to others
for x in distinct_country:
    cur.execute("""SELECT COUNT(*) 
                     FROM  (SELECT 
                            DISTINCT learner_id
                            FROM data2018 
                            WHERE country=(?))""", (x) )
    how_many = cur.fetchall()
    if how_many[0][0] < 200:
        others += how_many[0][0]
        continue
    country.append(x[0])
    people.append(how_many[0][0])
country.append('Others')
people.append(others)



for x in range(len(country)): 
    print(country[x], people[x])
pie_chart.pie_chart(tuple(country),people)
