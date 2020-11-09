from apscheduler.schedulers.blocking import BlockingScheduler
import time
sched = BlockingScheduler()
from weather import *



@sched.scheduled_job('interval', hours=3)
def timed_job1():
    thedict=get_current_weather()
    print('This job is run every three hours.')

@sched.scheduled_job('interval', hours=3)
def timed_job2():
    
    print('This is the number in number.txt: {0}')

sched.start()
