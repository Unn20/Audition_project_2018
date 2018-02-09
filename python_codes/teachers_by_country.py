#this code search, how many people have a teacher depending on which country they are from and create a barchart

#learner_id  country   in_course   unit   avg_score    completion   inv_rate
import sqlite3
import bar_chart as bar
conn = sqlite3.connect('PearsonData.db')
cur = conn.cursor() 

not_significant_under = 200
country = []
people = []
with_teachers = []
percentage = []
others = 0


def autolabel(rects, ax):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.00*height,
                '{0}%'.format(int(height)),
                ha='center', va='bottom')

#All people
cur.execute("""SELECT COUNT(*) 
                 FROM  (SELECT 
                        DISTINCT learner_id
                        FROM data2018 )""")
all_people = cur.fetchall()[0][0]


#Give me distinct country
cur.execute("""SELECT 
               DISTINCT
               country FROM data2018
               ORDER BY country""")
distinct_country = cur.fetchall()
if distinct_country[0] == ('',): distinct_country = distinct_country[1:]


#Hom many people have teacher
    #Find all teachers
cur.execute("""SELECT COUNT(CASE in_course WHEN 't' THEN 1 ELSE null END) 
                     FROM  (SELECT 
                            DISTINCT learner_id, in_course
                            FROM data2018 )""")
all_teachers = cur.fetchall()[0][0]  
print(all_teachers)


#Search for number of people from cuntry X
#If number < 200 add this to others
for x in distinct_country:
    cur.execute("""SELECT COUNT(*) 
                     FROM  (SELECT 
                            DISTINCT learner_id
                            FROM data2018 
                            WHERE country=(?))""", (x) )
    how_many = cur.fetchall()
    if how_many[0][0] < not_significant_under:
        others += how_many[0][0]
        continue
    country.append(x[0])
    people.append(how_many[0][0])
country.append('Others')
people.append(others)
    

  
    
    

    #Search for number of people who use techer
distinct_country_BIG = country[:-1]
for x in distinct_country_BIG:    
    cur.execute("""SELECT COUNT(CASE in_course WHEN 't' THEN 1 ELSE null END) 
                     FROM  (SELECT 
                            DISTINCT learner_id, in_course
                            FROM data2018 
                            WHERE country=(?))""", (x,) )
    how_many = cur.fetchall()
    with_teachers.append(how_many[0][0])
    #Substract to get others
with_teachers.append(all_teachers - sum(with_teachers))


#Add data for all people
country.insert(0,'avg')
people.insert(0,all_people)
with_teachers.insert(0,all_teachers)


#Percentage teacher/all learners
for x in range(len(country)):
    percentage.append(with_teachers[x] / people[x])



for x in range(len(country)):
    print(country[x], people[x], with_teachers[x],percentage[x])
    
bar.bar_chart(country, people, with_teachers, "People with teachers")
    
    