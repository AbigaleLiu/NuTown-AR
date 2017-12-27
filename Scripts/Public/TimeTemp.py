import datetime
import time


def time_temp():
    """
    当前时间
    :return:
    """
    temp = datetime.datetime.now().strftime("%Y-%m-%d _%H_%M_%S")
    return temp


def mail_time():
    """
    获取当前周几\几点
    :return:
    """
    mail_time = {}
    weekday = time.strftime("%a")
    hour = time.strftime("%H")
    mail_time["weekday"] = weekday
    mail_time['hour'] = hour
    return mail_time


if __name__ == '__main__':
    time_temp()
    print(mail_time())