import os
from appium import webdriver
from Scripts.Public.TimeTemp import *


def img_name():
    img_name = time_temp() + ".jpg"
    return img_name
