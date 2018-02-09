#this code searchs the ratio of people whos started some chapter to whole people and create a bar chart

#learner_id  country   in_course   unit   avg_score    completion   inv_rate
import sqlite3
import bar_chart as bar
conn = sqlite3.connect('PearsonData.db')
cur = conn.cursor() 

chapter = []
people = []
with_teachers = []
percentage = []

cur.execute("""SELECT COUNT(*)
                FROM (SELECT
                        DISTINCT learner_id
                        FROM data2018)""")
all_people = int(str(cur.fetchall())[2:-3])


#Give me distinct country
cur.execute("""SELECT 
               DISTINCT
               unit FROM data2018
               ORDER BY unit""")
distinct_chapter = cur.fetchall()

#Search for number of people from country X
for x in distinct_chapter:
    cur.execute("""SELECT COUNT(*) 
                     FROM  (SELECT 
                            DISTINCT learner_id
                            FROM data2018 
                            WHERE unit=(?))""", (x) )
    how_many = cur.fetchall()
    chapter.append(x[0])
    people.append(how_many[0][0])

a = 0
copy_people = people.copy()
print(chapter,people)
chapter[0] = 'nothing'
for i in range(1,18):
    if i <=12:
        chapter[i] = '{}'.format(i)
    elif i <=16:
        chapter[i] = 'R{}'.format(i-12)
    else:
        chapter[i] = 'POD'
for i in range(2,13):
    if i <=9:
        people[i] = copy_people[i+3]
    elif i<=12:
        people[i] = copy_people[i-8]
        
print(chapter,people)
        
bar.bar_chart(chapter, (all_people for i in range(len(chapter))), people, "The ratio of people to chapters")        

        
        
        