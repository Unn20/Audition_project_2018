#code that shows scores depending on teacher presence

#learner_id  country   in_course   unit   avg_score    completion   inv_rate
#wynik od teachera
import sqlite3
import bar_chart_one_value as bar
conn = sqlite3.connect('PearsonData.db')
cur = conn.cursor() 

cur.execute("""SELECT AVG(avg_score)
                    FROM (SELECT avg_score FROM data2018 WHERE in_course='f')""")
wynik_f = cur.fetchall()
wynik_f = float(str(wynik_f)[2:-3])
wynik_f = float(format(wynik_f, '.4f')) * 100
print(wynik_f)


cur.execute("""SELECT AVG(avg_score)
                    FROM (SELECT avg_score FROM data2018 WHERE in_course='t')""")
wynik_t = cur.fetchall()
wynik_t = float(str(wynik_t)[2:-3])
wynik_t = float(format(wynik_t, '.4f')) * 100
print(wynik_t)


bar.bar_chart(('teacher', 'no teacher'),[wynik_t,wynik_f],"Score depending on teacher presence")
