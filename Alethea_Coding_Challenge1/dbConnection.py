import pymysql.cursors

import json


connection = pymysql.connect(host='',
                             user='',
                             password='',
                             db=''
                             )
print("connect successfull")

try:
    with connection.cursor() as cursor:
        sql1=("CREATE TABLE statepopulation Pop_Total_by_State varchar(255) ,average_pop_per_zip number, averege_pop_per_state number")

        sql2 =("INSERT INTO statepopulation (Pop_Total_by_State, average_pop_per_zip, averege_pop_per_state, json) VALUES (%s,%s,%s),(status.get('Pop_Total_by_State'), status.get('average_pop_per_zip'), status.get('averege_pop_per_state'))")
        cursor.execute(sql1)
        cursor.execute(sql2)
        connection.commit()

except Exception as e:
   print(str(e))

print ("inserted value")

