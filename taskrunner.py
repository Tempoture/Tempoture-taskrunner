from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()
from weather import *
import os


@sched.scheduled_job('interval', hours=3)
def weatehrupdate():
    try:
        connection = psycopg2.connect(user = os.environ["DB_USER"],
                                  password = os.environ["DB_PASS"],
                                  host = os.environ["DB_HOST"],
                                  port = os.environ["DB_PORT"],
                                  database = os.environ["DB_NAME"] )

        cursor = connection.cursor()
        connection.autocommit = True
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)   
    finally:
        if(connection):
            cursor.close()
            connection.close()        
@sched.scheduled_job('interval', hours=16)
def timed_job2():
    
    print('This is the number in number.txt: {0}')

sched.start()
