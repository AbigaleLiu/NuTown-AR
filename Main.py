from Scripts.Mail.Mail import *
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from pymongo import MongoClient

from Scripts.Report.Html import *

os.system("appium server")  # 启动appium server

Html().html()

mail = Mail().mail

client = MongoClient("mongodb://localhost:27017/")

jobstores = {
    'mongo': MongoDBJobStore(collection='job', database='test', client=client),
    'default': MemoryJobStore()
}
executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}
scheduler = BlockingScheduler(jobstores=jobstores, executors=executors)
scheduler.add_job(mail, "cron", day_of_week="fri", hour=18)  # 每周五晚上六点发送邮件
# scheduler.add_job(mail, "interval", seconds=60)  # 每隔60秒发送邮件
try:
    scheduler.start()
except SystemExit as e:
    client.close()
    print(e)
