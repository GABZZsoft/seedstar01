#from urllib.request import urlopen
#http://localhost:8080/api/json?pretty=true
#-u admin:073047e5982be1e8bc24e1c08777fc39
# object = urlopen("http://localhost:8080/api/json?pretty=true")
# print(object.read())
import jenkins
import sqlite3 as db
import datetime

def dbconn( jobStat, date):
    conn = db.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists jobStatus(status VARCHAR(10), date datetime);')
    cursor.execute('insert into jobStatus values(?,?);',[jobStat, date])
    cursor.execute("select * from jobStatus")
    ###For confirmation in the console###
    result = cursor.fetchall()
    for r in result:
        print(r)
    ################
    conn.commit()
    conn.close()

server = jenkins.Jenkins('http://localhost:8080', username='admin', password='073047e5982be1e8bc24e1c08777fc39')
job_count = server.jobs_count()
jobs = server.get_jobs()
dateTime = str(datetime.datetime.now())
for i in range(0,job_count):
    status = jobs[i]['color']
    dbconn(status, dateTime)
